#!/usr/bin/env python3
"""
Created on Tue May 21 2024

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

from typing import NamedTuple

import asyncio
from abc import ABC, abstractmethod
import logging


Q_LENGTH = 20  # message queue length


class Message(NamedTuple):
    topic: str
    payload: str | bytes


class BridgeLeg(ABC):
    """Base class for bridge legs"""

    def __init__(self) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._out_q: asyncio.Queue[Message] = asyncio.Queue(Q_LENGTH)

    def publish(self, message: Message) -> None:
        """publish message to the leg"""
        self._log.debug(f"Publishing {message}")
        try:
            self._out_q.put_nowait(message)
        except asyncio.QueueFull:
            self._log.warning("Queue full, dropping message")

    @abstractmethod
    async def subscribe(self, topic: str) -> None:
        """subscribe to a topic"""

    @abstractmethod
    async def unsubscribe(self, topic: str) -> None:
        """unsubscribe from a topic"""

    @abstractmethod
    async def main(self) -> None:
        """main loop for the leg"""
