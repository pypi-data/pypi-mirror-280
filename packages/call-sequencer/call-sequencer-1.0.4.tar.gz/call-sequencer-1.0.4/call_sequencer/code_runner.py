from call_sequencer import CallSequencer
import subprocess
import sys
from typing import Any, Dict, Optional


@CallSequencer.with_args
def run_python_code(code: str, **globals_dict) -> Any:
    """
    Runs a given Python code string and returns the result.
    """
    if globals_dict is None:
        globals_dict = {}
    try:
        exec(code, globals_dict)
        return globals_dict
    except Exception as e:
        return str(e)


@CallSequencer.simple
def run_shell_command(command: str) -> Dict[str, Any]:
    return _internal_run_shell_command(command)

def _internal_run_shell_command(command: str) -> Dict[str, Any]:
    """
    Runs a shell command and returns the output.
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }
    except Exception as e:
        return {"error": str(e)}


@CallSequencer.simple
def evaluate_expression(expression: str) -> Any:
    """
    Evaluates a Python expression and returns the result.
    """
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)


@CallSequencer.simple
def install_package(package_name: str) -> Dict[str, Any]:
    """
    Installs a Python package using pip and returns the output.
    """
    command = f"{sys.executable} -m pip install {package_name}"
    return _internal_run_shell_command(command)


@CallSequencer.simple
def uninstall_package(package_name: str) -> Dict[str, Any]:
    """
    Uninstalls a Python package using pip and returns the output.
    """
    command = f"{sys.executable} -m pip uninstall -y {package_name}"
    return _internal_run_shell_command(command)


@CallSequencer.simple
def list_installed_packages(_: None = None) -> Dict[str, Any]:
    """
    Lists all installed Python packages using pip.
    """
    command = f"{sys.executable} -m pip list"
    return _internal_run_shell_command(command)


@CallSequencer.simple
def get_package_info(package_name: str) -> Dict[str, Any]:
    """
    Gets information about a Python package using pip show.
    """
    command = f"{sys.executable} -m pip show {package_name}"
    return _internal_run_shell_command(command)


@CallSequencer.simple
def read_file(file_path: str) -> Optional[str]:
    """
    Reads the content of a file and returns it as a string.
    """
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except Exception as e:
        return str(e)


@CallSequencer.with_args
def write_file(content: str, *args) -> Optional[str]:
    """
    Writes a string content to a file.
    """
    try:
        with open(args[0], "w") as file:
            file.write(content)
        return None
    except Exception as e:
        return str(e)


@CallSequencer.with_args
def append_to_file(content: str, *args) -> Optional[str]:
    """
    Appends a string content to a file.
    """
    try:
        with open(args[0], "a") as file:
            file.write(content)
        return None
    except Exception as e:
        return str(e)
