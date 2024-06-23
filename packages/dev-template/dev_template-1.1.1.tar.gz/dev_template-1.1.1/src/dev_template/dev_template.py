import argparse
import configparser
import importlib.resources as package_resources
import logging
import os
import platform
import shutil
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Dict, List, Optional

from colorama import Fore, Style, init
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.formatted_text import HTML
from pydantic import BaseModel, DirectoryPath, ValidationError, field_validator
from tqdm import tqdm

CYAN = Fore.CYAN
PURPLE = Fore.MAGENTA
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

CONFIG = {}
DEFAULT_PACKAGES = []
DEFAULT_PROJECT_PATH = ""
CREATE_SETUP = False
CREATE_PYPROJECT = False
TEMPLATES_COPIED = False
RESERVED_FILE_NAMES = set()


class ProjectConfig(BaseModel):
    project_path: DirectoryPath
    project_name: str
    successful_packages: List[str]

    @field_validator("project_name")
    def project_name_valid(cls, project_name):
        if project_name.upper() in RESERVED_FILE_NAMES:
            raise ValueError(
                f"Project name '{project_name}' is reserved... Please choose a different name.\n"
            )
        return project_name


def format_text(text: str, color: str) -> str:
    return f"<{color}>{text}</{color}>"


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def initialize_globals() -> None:
    global \
        CONFIG, \
        DEFAULT_PACKAGES, \
        DEFAULT_PROJECT_PATH, \
        CREATE_SETUP, \
        CREATE_PYPROJECT, \
        TEMPLATES_COPIED, \
        RESERVED_FILE_NAMES

    CONFIG["config_dir"] = get_config_path()
    CONFIG["config_path"] = os.path.join(CONFIG["config_dir"], "config.ini")

    config_path = CONFIG["config_path"]
    if not os.path.exists(config_path):
        default_config_path = os.path.join(
            os.path.dirname(__file__), "config", "config.ini"
        )
        os.makedirs(CONFIG["config_dir"], exist_ok=True)
        shutil.copy(default_config_path, config_path)

    config = configparser.ConfigParser()
    config.read(config_path)

    DEFAULT_PACKAGES = config.get("DEFAULT", "default_packages", fallback="").split(",")
    DEFAULT_PROJECT_PATH = config.get("DEFAULT", "default_project_path", fallback="")
    CREATE_SETUP = config.getboolean("DEFAULT", "create_setup", fallback=False)
    CREATE_PYPROJECT = config.getboolean("DEFAULT", "create_pyproject", fallback=False)
    TEMPLATES_COPIED = config.getboolean("DEFAULT", "templates_copied", fallback=False)
    RESERVED_FILE_NAMES = set(
        name.strip().upper()
        for name in config.get("DEFAULT", "reserved_file_names", fallback="").split(",")
    )

    if not TEMPLATES_COPIED:
        copy_templates()


def get_config_path() -> str:
    if platform.system() == "Windows":
        config_dir = os.path.join(os.getenv("LOCALAPPDATA"), "dev_template")
    else:
        config_dir = os.path.join(os.path.expanduser("~"), ".config", "dev_template")
    return config_dir


def setup_logging(log_id: str, max_log_files: int, debug: bool = False) -> None:
    logs_dir = os.path.join(CONFIG["config_dir"], "logs")
    os.makedirs(logs_dir, exist_ok=True)
    log_file = os.path.join(logs_dir, f"{log_id}.log")

    log_level = logging.DEBUG if debug else logging.INFO

    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    log_files = sorted(
        (os.path.join(logs_dir, f) for f in os.listdir(logs_dir)),
        key=os.path.getmtime,
    )
    while len(log_files) > max_log_files:
        oldest_log = log_files.pop(0)
        os.remove(oldest_log)
        logging.info(f"Removed old log file: {oldest_log}")

    logging.info("Logging is set up.")


def get_bool_input(prompt_text: str, default: str = "no") -> str:
    while True:
        value = prompt_with_simple_completion(prompt_text).strip().lower()
        if value == "":
            value = default.lower()
        if value in {"yes", "y", "no", "n"}:
            return "1" if value in {"yes", "y"} else "0"
        print(f"{RED}Invalid input. Please enter Yes/Y or No/N.{RESET}")


def setup_logo() -> None:
    print(
        f"{CYAN}{'=' * 23}{RESET}\n"
        f"{CYAN}| dev_template config |{RESET}\n"
        f"{CYAN}{'=' * 23}{RESET}"
    )


def setup_config() -> None:
    try:
        config_path = CONFIG["config_path"]
        config = configparser.ConfigParser()
        config.read(config_path)

        def get_current_value(section: str, option: str, default: str = "") -> str:
            return config.get(section, option, fallback=default)

        clear_screen()
        setup_logo()
        logging.info("Setting up configuration...")
        default_packages_current = get_current_value("DEFAULT", "default_packages", "")
        if default_packages_current:
            logging.info("Current default packages to be installed in each project:")
            print(
                f"{GREEN}Current default packages to be installed in each project:{RESET}"
            )
            for package in default_packages_current.split(","):
                print(f"- {package.strip()}")
                logging.info(f"- {package.strip()}")
            print()
        default_packages_prompt = (
            "<yellow>Enter default packages to install (comma delimited): </yellow>"
        )
        default_packages_response = prompt_with_simple_completion(
            default_packages_prompt
        )
        if not default_packages_response and default_packages_current:
            clear_default_packages = get_bool_input(
                "Do you want to clear the default packages? (Yes/Y or No/N) or press 'Enter' for [No]: ",
                "no",
            )
            default_packages = (
                "" if clear_default_packages == "1" else default_packages_current
            )
        else:
            default_packages_list = [
                package.strip()
                for package in (
                    default_packages_response or default_packages_current
                ).split(",")
            ]
            default_packages = ", ".join(sorted(set(default_packages_list)))

        clear_screen()
        setup_logo()
        session = PromptSession()
        default_project_dir_current = get_current_value(
            "DEFAULT", "default_project_path", ""
        )
        if default_project_dir_current:
            logging.info(
                f'Current default project directory = "{default_project_dir_current}"'
            )
            print(
                f'{GREEN}Current default project directory ={RESET} "{default_project_dir_current}"\n'
            )
        default_project_dir_prompt = HTML(
            "<yellow>Enter absolute path for default project directory: </yellow>"
        )

        while True:
            response = session.prompt(
                default_project_dir_prompt, completer=PathCompleter()
            )
            if not response.strip() and default_project_dir_current:
                clear_default_project_dir = get_bool_input(
                    "Do you want to clear the default project directory? (Yes/Y or No/N) or press 'Enter' for [No]: ",
                    "no",
                )
                default_project_dir = (
                    ""
                    if clear_default_project_dir == "1"
                    else default_project_dir_current
                )
            else:
                default_project_dir = response.strip() or default_project_dir_current
            if default_project_dir or default_project_dir == "":
                break

        clear_screen()
        setup_logo()
        create_setup_current = (
            "Yes" if get_current_value("DEFAULT", "create_setup", "0") == "1" else "No"
        )
        create_setup = get_bool_input(
            f"<yellow>Create setup.py? (Yes/Y or No/N) or press 'Enter' for [{create_setup_current}]: </yellow>",
            create_setup_current,
        )

        clear_screen()
        setup_logo()
        create_pyproject_current = (
            "Yes"
            if get_current_value("DEFAULT", "create_pyproject", "0") == "1"
            else "No"
        )
        create_pyproject = get_bool_input(
            f"<yellow>Create pyproject.toml? (Yes/Y or No/N) or press 'Enter' for [{create_pyproject_current}]: </yellow>",
            create_pyproject_current,
        )

        config["DEFAULT"]["default_packages"] = default_packages
        config["DEFAULT"]["default_project_path"] = default_project_dir
        config["DEFAULT"]["create_setup"] = create_setup
        config["DEFAULT"]["create_pyproject"] = create_pyproject

        with open(config_path, "w") as f:
            config.write(f)

        clear_screen()
        logging.info(
            f"New configuration: default_packages={config['DEFAULT']['default_packages']}, "
            f"default_project_path={config['DEFAULT']['default_project_path']}, "
            f"create_setup={config['DEFAULT']['create_setup']}, "
            f"create_pyproject={config['DEFAULT']['create_pyproject']}"
        )
        logging.info(f"Configuration updated at {config_path}")
        print(f"\n{PURPLE}Configuration updated at {config_path}{RESET}")
    except KeyboardInterrupt:
        print(f"{RED}Operation cancelled by user. Exiting...{RESET}")
        logging.info("Operation cancelled by user.")
        sys.exit(0)


def copy_templates() -> None:
    template_dest_path = Path(CONFIG["config_dir"]) / "templates"

    if not template_dest_path.exists():
        template_dest_path.mkdir(parents=True)

    with package_resources.path("dev_template", "templates") as template_src_path:
        for item in template_src_path.rglob("*"):
            relative_path = item.relative_to(template_src_path)
            dest_path = template_dest_path / relative_path
            if item.is_dir():
                dest_path.mkdir(parents=True, exist_ok=True)
            else:
                shutil.copy2(item, dest_path)

    config_path = CONFIG["config_path"]
    config = configparser.ConfigParser()
    config.read(config_path)
    config.set("DEFAULT", "templates_copied", "1")
    with open(config_path, "w") as configfile:
        config.write(configfile)


def prompt_with_path_completion(prompt_text: str, default_value: str = "") -> str:
    session = PromptSession()
    response = session.prompt(HTML(prompt_text), completer=PathCompleter())
    return response.strip() if response.strip() else default_value


def prompt_with_simple_completion(prompt_text: str) -> str:
    session = PromptSession()
    return session.prompt(HTML(prompt_text))


def get_project_name() -> str:
    while True:
        project_name = prompt_with_simple_completion(
            format_text("Enter the project name: ", "yellow")
        )
        if project_name.strip():
            try:
                _ = ProjectConfig(
                    project_name=project_name,
                    project_path="/",
                    successful_packages=[],
                )
                return project_name
            except ValidationError as e:
                logging.error(f"Error: {e.errors()[0]['msg']}")
                print(f"{RED}Error: {e.errors()[0]['msg']}{RESET}")
        else:
            logging.error("Error: Project name cannot be empty")
            print(f"{RED}Error: Project name cannot be empty...{RESET}\n")


def get_project_path(
    default_project_path: str,
    project_name: Optional[str] = None,
    allow_empty: bool = False,
) -> str:
    if default_project_path:
        prompt_message = format_text(
            f"Press Enter to use default path '<green>{default_project_path}</green>' or enter new absolute path: ",
            "yellow",
        )
    else:
        prompt_message = format_text(
            "Enter absolute path to create the project: ", "yellow"
        )

    while True:
        project_path = prompt_with_path_completion(prompt_message, default_project_path)

        if project_path or allow_empty:
            full_project_path = os.path.join(project_path, project_name)
            if os.path.exists(full_project_path):
                logging.error(
                    f'The project "{project_name}" already exists at "{project_path}"'
                )
                print(
                    f"{RED}Error: The project {RESET}'{project_name}' {RED}already exists at {RESET}'{project_path}'{RED}. Please choose a different path or project name.{RESET}\n"
                )
                return None
            if project_path and (
                os.path.exists(project_path) and os.access(project_path, os.W_OK)
            ):
                return project_path
            elif allow_empty:
                return project_path

        error_message = (
            f"Error: The path '{project_path}' does not exist"
            if not os.path.exists(project_path)
            else f"Error: You do not have write permissions for the path... '{project_path}'"
        )
        logging.error(error_message)
        print(f"{RED}{error_message}{RESET}")


def get_packages() -> List[str]:
    default_packages_str = ", ".join(package.strip() for package in DEFAULT_PACKAGES)
    prompt_text = "Enter packages to install (comma delimited): "

    session = PromptSession()
    successful_packages = session.prompt(
        HTML(format_text(prompt_text, "yellow")), default=default_packages_str
    ).split(",")

    return [package.strip() for package in successful_packages if package.strip()]


def create_project_structure(config: ProjectConfig) -> None:
    init(autoreset=True)

    full_project_path = os.path.join(config.project_path, config.project_name)

    logging.info(f"Creating project directory '{full_project_path}'")
    print(f"{CYAN}Creating project directory...{RESET}")
    create_project_directory(full_project_path)
    logging.info("Creating project directory - Done")
    print(f"{PURPLE}Creating project directory - Done{RESET}\n")

    logging.info(f"Creating subdirectories in '{full_project_path}'")
    print(f"{CYAN}Creating subdirectories...{RESET}")
    create_subdirectories(full_project_path, config.project_name)
    logging.info("Creating subdirectories - Done")
    print(f"{PURPLE}Creating subdirectories - Done{RESET}\n")

    create_basic_files(full_project_path, config.project_name)

    create_virtualenv(full_project_path, config.project_name)

    successful_packages = install_packages(
        full_project_path, config.project_name, config.successful_packages
    )

    if successful_packages:
        write_successful_packages_to_files(
            full_project_path,
            config.project_name,
            successful_packages,
        )


def create_project_directory(full_project_path: str) -> None:
    try:
        os.makedirs(full_project_path, exist_ok=True)
    except Exception as e:
        logging.error(f"Could not create project directory: {e}")
        raise ValueError(f"Could not create project directory: {e}")


def create_subdirectories(full_project_path: str, project_name: str) -> None:
    os.makedirs(os.path.join(full_project_path, "src", project_name), exist_ok=True)
    os.makedirs(os.path.join(full_project_path, "tests"), exist_ok=True)


def create_basic_files(full_project_path: str, project_name: str) -> None:
    template_dir = os.path.join(CONFIG["config_dir"], "templates")

    files_to_create = {
        "README.md": "README.md",
        ".gitignore": ".gitignore",
        "requirements.txt": "requirements.txt",
        "src/{project_name}/__init__.py": os.path.join("src", "__init__.py"),
        "src/{project_name}/main.py": os.path.join("src", "main.py"),
        "tests/__init__.py": os.path.join("tests", "__init__.py"),
        "tests/test_main.py": os.path.join("tests", "test_main.py"),
    }

    if CREATE_SETUP:
        files_to_create["setup.py"] = "setup.py"

    if CREATE_PYPROJECT:
        files_to_create["pyproject.toml"] = "pyproject.toml"

    with tqdm(
        total=len(files_to_create),
        desc=f"{CYAN}Creating basic files{RESET}",
        ncols=100,
        leave=True,
    ) as progress_bar:
        for dest_template, src_template in files_to_create.items():
            dest_file = os.path.join(
                full_project_path, dest_template.format(project_name=project_name)
            )
            src_file = os.path.join(template_dir, src_template)

            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            shutil.copyfile(src_file, dest_file)
            progress_bar.update(1)
    logging.info(f'Basic files created in "{full_project_path}"')
    print(f"{PURPLE}Creating basic files - Done{RESET}\n")


def create_virtualenv(full_project_path: str, project_name: str) -> None:
    venv_path = os.path.join(full_project_path, f"{project_name}_venv")
    with tqdm(
        total=1,
        desc=f"{CYAN}Creating virtual environment{RESET}",
        ncols=100,
        leave=True,
    ) as progress_bar:
        subprocess.check_call([sys.executable, "-m", "venv", venv_path])
        progress_bar.update(1)
    logging.info(f'Virtual environment created at "{venv_path}"')
    print(f"{PURPLE}Creating virtual environment - Done{RESET}\n")


def install_packages(
    full_project_path: str, project_name: str, packages: list
) -> List[str]:
    venv_path = os.path.join(full_project_path, f"{project_name}_venv")
    bin_dir = "Scripts" if os.name == "nt" else "bin"
    packages = list(set(packages))

    if not packages:
        logging.info("No packages to install. Skipping")
        print(f"{YELLOW}No packages to install. Skipping...{RESET}")
        return []

    successful_packages = []
    failed_packages = []

    with tqdm(
        total=len(packages),
        desc=f"{CYAN}Installing packages{RESET}",
        ncols=100,
        leave=True,
    ) as progress_bar:
        for package in packages:
            try:
                subprocess.check_call(
                    [os.path.join(venv_path, bin_dir, "pip"), "install", package],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                successful_packages.append(package)
                logging.info(f'Successfully installed package "{package}"')
            except subprocess.CalledProcessError:
                failed_packages.append(package)
                logging.error(f'Failed to install package "{package}"')
            progress_bar.update(1)

    if successful_packages:
        installed_packages_str = ", ".join(
            [f"{CYAN}{package}{RESET}" for package in successful_packages]
        )
        logging.info(f"Successfully installed packages: {installed_packages_str}")
        print(
            f"{PURPLE}Successfully installed packages: {installed_packages_str}{RESET}"
        )

    if failed_packages:
        failed_packages_str = ", ".join(
            [f"{RED}{package}{RESET}" for package in failed_packages]
        )
        logging.error(f"Failed to install packages: {failed_packages_str}")
        print(f"{RED}Failed to install packages: {failed_packages_str}{RESET}")

    logging.info("Installing packages - Done")
    print(f"{PURPLE}Installing packages - Done{RESET}")
    return successful_packages


def get_installed_packages(venv_path: str) -> Dict[str, str]:
    bin_dir = "Scripts" if os.name == "nt" else "bin"
    freeze_output = subprocess.check_output(
        [os.path.join(venv_path, bin_dir, "pip"), "freeze"], text=True
    )
    return dict(line.split("==") for line in freeze_output.splitlines())


def update_requirements_txt(
    file_path: str, successful_packages: List[str], package_versions: Dict[str, str]
) -> None:
    with open(file_path, "a") as f:
        for package in successful_packages:
            if package in package_versions:
                f.write(f"{package}=={package_versions[package]}\n")
                logging.info(
                    f'Updated requirements.txt with package "{package}=={package_versions[package]}"'
                )


def update_pyproject_toml(
    file_path: str, successful_packages: List[str], package_versions: Dict[str, str]
) -> None:
    with open(file_path, "r") as f:
        lines = f.readlines()

    with open(file_path, "w") as f:
        for line in lines:
            f.write(line)
            if line.strip() == "dependencies = [":
                for package in successful_packages:
                    if package in package_versions:
                        f.write(f'    "{package}=={package_versions[package]}",\n')
                        logging.info(
                            f'Updated pyproject.toml with package "{package}=={package_versions[package]}"'
                        )


def write_successful_packages_to_files(
    full_project_path: str,
    project_name: str,
    successful_packages: List[str],
) -> None:
    venv_path = os.path.join(full_project_path, f"{project_name}_venv")
    package_versions = get_installed_packages(venv_path)

    files_to_update = {
        "requirements.txt": (
            update_requirements_txt,
            [successful_packages, package_versions],
        ),
        "pyproject.toml": (
            update_pyproject_toml,
            [successful_packages, package_versions],
        ),
    }

    file_paths = {
        "requirements.txt": os.path.join(full_project_path, "requirements.txt"),
        "pyproject.toml": os.path.join(full_project_path, "pyproject.toml"),
    }

    print()
    with tqdm(
        total=len(files_to_update),
        desc=f"{CYAN}Updating files{RESET}",
        ncols=100,
        leave=True,
    ) as progress_bar:
        for file, (update_function, args) in files_to_update.items():
            update_function(file_paths[file], *args)
            progress_bar.update(1)
    logging.info("Writing successful packages to files - Done")
    print(f"{PURPLE}Writing successful packages to files - Done{RESET}\n")


def parse_arguments():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument(
        "--config", "-c", action="store_true", help="Setup configuration"
    )
    parser.add_argument(
        "--debug", "-d", action="store_true", help="Enable debug logging"
    )
    return parser.parse_args()


def main():
    initialize_globals()
    args = parse_arguments()
    unique_id = str(uuid.uuid4())
    setup_logging(unique_id, debug=args.debug, max_log_files=7)

    if args.config:
        setup_config()
        return

    while True:
        try:
            init(autoreset=True)
            print(
                f"{CYAN}{'=' * 33}{RESET}\n"
                f"{CYAN}| setting up new Python project |{RESET}\n"
                f"{CYAN}{'=' * 33}{RESET}"
            )

            while True:
                project_name = get_project_name()
                project_path = get_project_path(DEFAULT_PROJECT_PATH, project_name)
                if project_path:
                    break

            packages = get_packages()
            config = ProjectConfig(
                project_name=project_name,
                project_path=project_path,
                successful_packages=packages,
            )

            if not project_path.endswith("/"):
                project_path += "/"

            full_project_path = os.path.join(project_path, project_name)

            logging.info(
                f'Setting up project "{project_name}" at "{full_project_path}"'
            )
            logging.info(
                f"Global variables: CONFIG={CONFIG}, DEFAULT_PACKAGES={DEFAULT_PACKAGES}, "
                f"DEFAULT_PROJECT_PATH={DEFAULT_PROJECT_PATH}, CREATE_SETUP={CREATE_SETUP}, "
                f"CREATE_PYPROJECT={CREATE_PYPROJECT}, TEMPLATES_COPIED={TEMPLATES_COPIED}, "
                f"RESERVED_FILE_NAMES={RESERVED_FILE_NAMES}"
            )

            print(
                f"{PURPLE}\nSetting up project '{CYAN}{project_name}{PURPLE}' at '{CYAN}{full_project_path}{PURPLE}'\n{RESET}"
            )

            create_project_structure(config)

            logging.info(
                f"Project '{project_name}' created successfully at '{full_project_path}'"
            )

            print(
                f"{PURPLE}\nProject '{CYAN}{project_name}{PURPLE}' created successfully at '{CYAN}{full_project_path}{PURPLE}'.{RESET}"
            )
            break

        except (ValidationError, ValueError) as e:
            print(f"{RED}Error: {str(e)}{RESET}")
            logging.error(f"Error: {str(e)}")
            input(f"{YELLOW}Press Enter to try again...{RESET}")
        except KeyboardInterrupt:
            print(f"{RED}Operation cancelled by user. Exiting...{RESET}")
            logging.info("Operation cancelled by user.")
            sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{RED}Operation cancelled by user. Exiting...{RESET}")
        logging.info("Operation cancelled by user.")
        sys.exit(0)
