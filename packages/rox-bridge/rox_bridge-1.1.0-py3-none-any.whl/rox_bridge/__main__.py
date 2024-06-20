""" main entry point for rox_bridge. """

from rox_bridge.bridge_node import main
from rox_bridge.utils import run_main_async
from rox_bridge import __version__


if __name__ == "__main__":
    print(f"Starting rox_bridge version: {__version__}!")
    run_main_async(main())
