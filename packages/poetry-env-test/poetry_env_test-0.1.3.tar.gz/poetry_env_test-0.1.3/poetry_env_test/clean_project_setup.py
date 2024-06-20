import os
import logging
import subprocess
from poetry_env_test.utils.utils import unset_python_path, run_command


def get_poetry_env_path():
    result = subprocess.run(
        "poetry env info --path", shell=True, capture_output=True, text=True
    )
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        logging.error("Failed to get Poetry environment path: %s", result.stderr)
        return None


def is_pyenv_virtualenv(env_path):
    pyenv_root = os.getenv("PYENV_ROOT", os.path.expanduser("~/.pyenv"))
    return env_path.startswith(pyenv_root)


def clean_project():
    unset_python_path()

    logging.info("Removing existing Poetry environment")
    env_path = get_poetry_env_path()
    if env_path:
        if not run_command(f"poetry env remove {env_path}"):
            if is_pyenv_virtualenv(env_path):
                env_name = os.path.basename(env_path)
                if not run_command(f"pyenv virtualenv-delete -f {env_name}"):
                    return
            else:
                return

    logging.info("Reinstalling dependencies with Poetry")
    if not run_command("poetry install"):
        return

    logging.info("Environment setup completed successfully")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    clean_project()
