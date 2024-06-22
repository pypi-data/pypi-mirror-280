import ctypes
import platform
import os
from pathlib import Path

# https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives

lib_path = Path(__file__).parent / "./debugbreak.dll"
lib = ctypes.CDLL(lib_path.as_posix())


# NOTE: I gave on trying to name it __debugbreak in Python too
# as double underscore starting name gets mangled inside classes
# making it not universal enough.
def debugbreak() -> None:
    """Execute `__debugbreak` from C extension, triggering Visual Studio popup."""
    current_system = platform.system()
    if current_system != "Windows":
        raise Exception(f"Unsupported platform: {current_system}.")

    # If it will stop working, we can use VSCODE_INJECTION = 1.
    if os.getenv("TERM_PROGRAM") == "vscode":
        msg = "Cannot trigger __debugbreak running python script from VS Code, try to run it outside of VS Code."
        raise Exception(msg)

    lib.start_debug()
