#!/usr/bin/env python3
"""CMK Dashboard

- [ ] Job overview
- [ ] Ticket overview
- [ ] Activity from FS
- [ ] Not Picked
- [ ] Local mon
- [ ] stale branches
- [ ] VPN status

Copyright (C) 2024 Checkmk GmbH - License: GNU General Public License v2
This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
conditions defined in the file COPYING, which is part of this source code package.
"""

# pylint: disable=too-many-locals
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-branches
# pylint: disable=unnecessary-lambda

import argparse
import asyncio
import json
import logging
import time
from collections.abc import (
    Callable,
    Iterable,
    MutableMapping,
    MutableSequence,
    Sequence,
)
from contextlib import suppress
from pathlib import Path

import chime  # type: ignore[import]

# from dbus import DBusException  # type: ignore[import-untyped]
from notify2 import Notification  # type: ignore[import]
from notify2 import init as notify2_init

# from pydantic import BaseModel
# from requests import ConnectionError as RequestsConnectionError
# from rich.align import Align
# from rich.style import Style
from rich.text import Text

# from rich_pixels import Pixels
from textual import on, work
from textual.app import ComposeResult
from textual.binding import Binding

# from textual.containers import Grid
from textual.widgets import RichLog, Static, Tree
from textual.widgets.tree import TreeNode
from trickkiste.base_tui_app import TuiBaseApp
from trickkiste.misc import date_str

from cmk_dev.jenkins_utils import AugmentedJenkinsClient, extract_credentials

# import jenkins  # type: ignore[import]
# from utils import RemoteExecutor, get_load_values, mon_df, mon_load, mon_ram
__version__ = "0.1.63"


def log() -> logging.Logger:
    """Returns the logger instance to use here"""
    return logging.getLogger("trickkiste.cmk-dsh")


class CmkDsh(TuiBaseApp):
    """CI relevant dashboard for Checkmk developer"""

    CSS = """
      #logo {background: $panel;}
      Grid {
        grid-size: 2;
        grid-columns: 1fr 60;
      }
      #event_log {
        background: $panel;
        padding: 1;
      }
      Tree > .tree--guides {
        color: $success-darken-3;
      }
      Tree > .tree--guides-selected {
        text-style: none;
        color: $success-darken-1;
      }
      #app_log {height: 10;}
    """

    BINDINGS = [
        Binding("m", "update_monitoring", "Update Monitoring Tree"),
        Binding("j", "update_jobs", "Update Job Tree"),
    ]
    CONFIG_FILE = "sheriff-state.json"

    def __init__(self) -> None:
        super().__init__(logger_funcname=False)
        cli_args = self.parse_arguments()
        self.set_log_level(cli_args.log_level)

        self.event_log = RichLog(id="event_log")
        self.event_log.border_title = "Events"
        self.event_messages: MutableSequence[tuple[int, str]] = []

        # self.job_tree_widget: Tree[None] = Tree("CI Jobs")
        notify2_init("Test")

    async def initialize(self) -> None:
        """UI entry point"""
        self.set_log_level("INFO")
        log().setLevel(logging.INFO)

        # with suppress(FileNotFoundError):
        # with open(self.CONFIG_FILE, encoding="utf-8") as config_file:
        # self.config = json.load(config_file)

        # if self.enable_micromonitoring:
        # self.monitor_node = self.job_tree_widget.root.add(
        # "[bold spring_green1]Infrastructure[/]", expand=False
        # )
        # self.monitor_node_state = self.set_monitor_node_state(0)

        # self.node_usage_node = self.job_tree_widget.root.add(
        # "[bold spring_green1]Build node system load[/]", expand=False
        # )

        # self.job_tree_node = self.job_tree_widget.root.add(
        # "[bold spring_green1]CI-Jobs[/] [white](press 'j' to force update)[/]",
        # expand=True,
        # allow_expand=False,
        # )

        self.maintain_statusbar()

    def __enter__(self) -> "CmkDsh":
        return self

    def __exit__(self, *args: object) -> None:
        with open(self.CONFIG_FILE, "w", encoding="utf-8") as config_file:
            json.dump(self.config, config_file, indent=4, sort_keys=True)

    def parse_arguments(self) -> argparse.Namespace:
        """parse command line arguments and return argument object"""
        parser = argparse.ArgumentParser(description=__doc__)
        self.add_default_arguments(parser)
        parser.add_argument(
            "--chime-theme",
            type=str.lower,
            choices=chime.themes(),
            default="big-sur",
        )
        parser.add_argument("--json", action="store_true")
        parser.add_argument("job_pattern", nargs="*", type=str, default=["checkmk"])
        parser.add_argument("--no-monitoring", action="store_true")
        return parser.parse_args()

    def log_event(self, message: str) -> None:
        """Adds a message to the event log (i.e. not logging)"""
        # todo: add relative time (with auto-updating)
        self.event_messages.insert(0, (int(time.time()), message))
        self.event_messages = self.event_messages[:30]
        self.event_log.clear()
        for timestamp, text in self.event_messages:
            self.event_log.write(
                Text.from_markup(f"[white]{date_str(timestamp, '%H:%M:%S')}[/] [bold]{text}[/]")
            )

    def compose(self) -> ComposeResult:
        """Set up the UI"""
        # yield Static(
        # Align.center(
        # Pixels.from_image_path(Path(__file__).parent / "sauron.png", resize=(32, 10)),
        # vertical="middle",
        # ),
        # id="logo",
        # )
        # with Grid():
        # yield self.job_tree_widget
        # yield self.event_log
        yield from super().compose()

    @on(Tree.NodeSelected)
    def on_node_selected(self, event: Tree.NodeSelected) -> None:
        """React on clicking a node (links handled differently)"""
        log().info("NodeSelected: %s", event.node.label)
        # if event.node.data:
        # cmd, data = event.node.data
        # if cmd == "copy":
        # log().info("copied slack message to clipboard")
        # pyperclip.copy(data)
        # if self.monitor_node and event.node == self.monitor_node:
        # self.set_monitor_node_state(self.monitor_node_state + 1)

    @work(exit_on_error=True)
    async def maintain_job_tree(self) -> None:
        """Busy worker task continuously rebuilding the job tree"""
        log().info("use job pattern: %s", self.job_pattern_list)

    @work(exit_on_error=True)
    async def maintain_statusbar(self) -> None:
        """Status bar stub (to avoid 'nonsense' status)"""
        while True:
            self.update_status_bar(
                f"{len(asyncio.all_tasks())} async tasks" f" │ checkmk-dev-tools v{__version__}"
            )
            await asyncio.sleep(3)


def main() -> None:
    """The main function"""
    with CmkDsh() as tui:
        tui.execute()


if __name__ == "__main__":
    main()
