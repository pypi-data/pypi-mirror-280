#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-3.0-or-later
# @authors: Runzhi He <rzhe@pku.edu.cn>
# @date: 2024-05-27

from typing import Iterable

from .local import WocMapsLocal


def format_map(key: str, map_objs: Iterable) -> str:
    return key + ";" + ";".join(map(str, map_objs))


if __name__ == "__main__":
    import argparse
    import logging
    import os
    import sys

    parser = argparse.ArgumentParser(description="Get record of various maps")
    parser.add_argument("type", type=str, help="The type of the object")
    parser.add_argument(
        "-p", "--profile", type=str, help="The path to the profile file", default=None
    )
    args = parser.parse_args()

    woc = WocMapsLocal(args.profile)
    for line in sys.stdin:
        try:
            key = line.strip()
            obj = woc.get_values(args.type, key)
            print(format_map(key, obj))
        except BrokenPipeError:
            # ref: https://docs.python.org/3/library/signal.html#note-on-sigpipe
            devnull = os.open(os.devnull, os.O_WRONLY)
            os.dup2(devnull, sys.stdout.fileno())
            sys.exit(1)  # Python exits with error code 1 on EPIPE
        except Exception as e:
            logging.error(f"Error in {key}: {e}", exc_info=True)
            continue
