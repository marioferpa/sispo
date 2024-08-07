# SPDX-FileCopyrightText: 2021 Gabriel J. Schwarzkopf <sispo-devs@outlook.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Utils module contains functions possibly used by all modules."""

import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)

def check_dir(directory, create=True):
    """
    Resolves directory and creates it, if it doesn't existing.

    :type directory: Path or str
    :param directory: Directory to be created if not existing

    :type create: bool
    :param create: Set to false if directory should not be created and instead
                   an exception shall be raise
    """
    print(f"Checking if directory {directory} exists...")
    if isinstance(directory, str):
        directory = Path(directory)

    dir_resolved = directory.resolve()

    if not dir_resolved.exists():
        if create:
            print(f"{directory} does not exist. Creating it...")
            Path.mkdir(dir_resolved, parents=True)
            print("Done!")
        else:
            raise RuntimeError(f"Directory {directory} does not exist!")
    else:
        print("Exists!")

    return dir_resolved


def execute(args, exception):
    """Utility function to execute all terminal programs."""
    logger.debug(f"{args[0]} is running with arguments {args[1:]}")
    ret = subprocess.run(args, capture_output=True, text=True)
    logger.debug(f"{args[0]} returned:\n{ret.stdout}\n{ret.stderr}")

    try:
        ret.check_returncode()
    except subprocess.CalledProcessError as e:
        logger.debug(f"{str(e)}")
        raise exception(e)

    return ret
