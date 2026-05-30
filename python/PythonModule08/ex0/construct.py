import os
import sys
import site


def is_virtual_env() -> bool:
    in_venv = hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )
    if in_venv:
        return True
    venv = os.environ.get("VIRTUAL_ENV", "")
    if venv and os.path.isdir(venv) and sys.executable.startswith(venv):
        return True
    return False


def get_venv_name() -> str:
    if hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    ):
        return os.path.basename(sys.prefix)
    venv = os.environ.get("VIRTUAL_ENV", "")
    if venv and sys.executable.startswith(venv):
        return os.path.basename(venv)
    return ""


def get_package_path() -> str:
    packages = site.getsitepackages()
    return packages[0] if packages else "unknown"


def main() -> None:
    python_path = sys.executable

    if is_virtual_env():
        venv_name = get_venv_name()
        venv_path = sys.prefix
        pkg_path = get_package_path()

        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(pkg_path)
    else:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
