#!/usr/bin/env python3
"""
Base Node class

Contains boilerplate for all nodes to ensure consistency.



Copyright (c) 2024 ROX Automation - Jev Kuznetsov

"""

import asyncio
import logging
import time
from typing import List, Callable

from .adapters.mqtt_adapter import MqttAdapter
from .config import MqttConfig

HEATBEAT_PERIOD = 1  # seconds


class Node:
    """base Node class

    Functionality:
        * logging `self._log`
        * mqtt interface `self.mqtt`
        * periodic heartbeat
        * cancellation of all tasks on .stop()
        * lock to avoid starting a node multple times

    How to use:
        * create a Node child class, optionally provide a name
        * add coroutines to `self._coros` list in __init__

    """

    def __init__(self, name: str | None = None) -> None:
        self.name = name or self.__class__.__name__
        self._log = logging.getLogger(self.name)
        self.mqtt = MqttAdapter(self)

        # error and warning counters. Will be sent with heartbeat.
        # increment on exceptions or warnings.
        self.nr_errors = 0
        self.nr_warnings = 0

        # list of coroutines to run in main(). Append to this list in __init__ of derived class. Provide as a reference to the coro, not a call.
        self._coros: List[Callable] = [
            self.mqtt.main,
            self._heartbeat,
        ]

        self._lock = asyncio.Lock()
        self._tasks: List[asyncio.Task] = []

    async def _heartbeat(self) -> None:
        """periodic heartbeat"""
        t_start = time.time()
        cfg = MqttConfig()

        while True:
            uptime = int(time.time() - t_start)
            await self.mqtt.publish(
                cfg.heartbeat_topic,
                {
                    "name": self.name,
                    "errors": self.nr_errors,
                    "warnings": self.nr_warnings,
                    "uptime": uptime,
                },
            )
            await asyncio.sleep(HEATBEAT_PERIOD)

    async def main(self) -> None:
        """main coroutine"""
        self._log.debug("starting main")

        if self._lock.locked():
            raise RuntimeError("Node is already running")

        await self._lock.acquire()

        async with asyncio.TaskGroup() as tg:
            for coro in self._coros:
                self._log.info(f"starting {coro}")
                task = tg.create_task(coro())
                self._tasks.append(task)

        self._log.info("Main coroutine finished")

    async def stop(self) -> None:
        """cancel all running tasks"""
        self._log.info("Stopping Node...")
        for task in self._tasks:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                self._log.info(f"Task {task} cancelled")
        self._log.info("Node stopped")
        self._lock.release()
