#!/usr/bin/env python3
"""
Mqtt half of the bridge

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

from typing import TYPE_CHECKING, Optional
import asyncio
import aiomqtt as mqtt
from pydantic_settings import BaseSettings, SettingsConfigDict

from rox_bridge import base

if TYPE_CHECKING:
    from rox_bridge.ws_leg import WsLeg


class MqttConfig(BaseSettings):
    """MQTT related settings"""

    model_config = SettingsConfigDict(env_prefix="mqtt_")

    host: str = "localhost"
    port: int = 1883


CFG = MqttConfig()


class MqttLeg(base.BridgeLeg):
    """MQTT facing side of the bridge"""

    def __init__(self) -> None:
        super().__init__()

        self.ws_leg: "Optional[WsLeg]" = None
        self._client: mqtt.Client | None = None
        self._client_ready = asyncio.Event()

    async def subscribe(self, topic: str) -> None:
        """subscribe to a topic"""
        if self._client is None:
            raise RuntimeError("MQTT client not initialized")

        await asyncio.wait_for(self._client_ready.wait(), timeout=1)

        self._log.info(f"Subscribing to {topic}")
        await self._client.subscribe(topic)

    async def unsubscribe(self, topic: str) -> None:
        """unsubscribe from topic"""
        if self._client is None:
            raise RuntimeError("MQTT client not initialized")

        self._log.info(f"Unsubscribing from {topic}")
        await self._client.unsubscribe(topic)

    async def _publish_mqtt(self, client: mqtt.Client) -> None:
        """publish items from mqtt queue.
        an item must have .mqtt_message() and .mqtt_topic() methods"""

        while True:
            message = await self._out_q.get()

            # publish message
            self._log.debug(f"{message=}")
            await client.publish(message.topic, message.payload)
            self._out_q.task_done()

    async def _receive_mqtt(self, client: mqtt.Client) -> None:
        """receive velocity setpoint from mqtt"""
        if self.ws_leg is None:
            raise RuntimeError("Websocket leg not initialized")

        self._log.debug("Starting mqtt receive loop")
        async for message in client.messages:
            self._log.debug(f"{message.topic=}, {message.payload=}")

            if not isinstance(message.payload, (str, bytes)):
                raise TypeError(f"Unexpected payload type {type(message.payload)}")

            self.ws_leg.publish(base.Message(message.topic.value, message.payload))

    async def main(self) -> None:
        """starting point to handle mqtt communication, starts send and recieve coroutines"""
        if self.ws_leg is None:
            raise RuntimeError("Websocket leg not initialized")

        self._log.info(f"Connecting to {CFG.host}:{CFG.port}")

        async with mqtt.Client(CFG.host, port=CFG.port) as client:
            self._client = client
            self._client_ready.set()
            async with asyncio.TaskGroup() as tg:
                tg.create_task(self._receive_mqtt(client))
                tg.create_task(self._publish_mqtt(client))

        self._client = None
