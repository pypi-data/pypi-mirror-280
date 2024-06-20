#!/usr/bin/env python3
"""
Bridge Node for MQTT and WebSocket communication.

Combines MQTT and WebSocket interfaces to facilitate communication between them.

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio
import logging

from rox_bridge.mqtt_leg import MqttLeg
from rox_bridge.ws_leg import WsLeg
from rox_bridge.utils import run_main_async


log = logging.getLogger("bridge")


async def main() -> None:
    mqtt = MqttLeg()
    ws = WsLeg()

    mqtt.ws_leg = ws
    ws.mqtt_leg = mqtt

    async with asyncio.TaskGroup() as tg:
        tg.create_task(mqtt.main())
        tg.create_task(ws.main())


if __name__ == "__main__":
    run_main_async(main())
