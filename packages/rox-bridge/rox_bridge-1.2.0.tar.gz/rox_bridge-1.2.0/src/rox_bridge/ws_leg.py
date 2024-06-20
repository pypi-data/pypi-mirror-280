#!/usr/bin/env python3
"""
websocket server

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

from typing import TYPE_CHECKING, Optional

import asyncio
import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
import orjson
import websockets
from websockets.legacy.server import WebSocketServerProtocol

from rox_bridge import base
from rox_bridge.utils import run_main_async

if TYPE_CHECKING:
    from rox_bridge.mqtt_leg import MqttLeg


log = logging.getLogger()


class WsConfig(BaseSettings):
    """Websocket related settings"""

    model_config = SettingsConfigDict(env_prefix="ws_")

    address: str = "0.0.0.0"
    port: int = 9095


CFG = WsConfig()


class WsLeg(base.BridgeLeg):
    """websocket facing side of the bridge"""

    def __init__(self) -> None:
        super().__init__()

        self.mqtt_leg: "Optional[MqttLeg]" = None
        # all current connections
        self._connections: set[WebSocketServerProtocol] = set()
        # keep running tasks to avoid garbage collection
        self._tasks: list[asyncio.Task] = []

    async def _handle_connection(self, websocket: WebSocketServerProtocol) -> None:
        """pass this to websockets.serve"""
        self._log.debug("Established connection")

        self._connections.add(websocket)
        self._tasks.append(asyncio.create_task(self._receive_handler(websocket)))

        try:
            await websocket.wait_closed()
        finally:
            self._connections.remove(websocket)

    async def subscribe(self, topic: str) -> None:
        """subscribe to a topic"""
        if self.mqtt_leg is None:
            raise RuntimeError("MQTT leg not initialized")

        await self.mqtt_leg.subscribe(topic)

    async def unsubscribe(self, topic: str) -> None:
        """unsubscribe from a topic"""
        if self.mqtt_leg is None:
            raise RuntimeError("MQTT leg not initialized")

        await self.mqtt_leg.unsubscribe(topic)

    async def _receive_handler(self, websocket: WebSocketServerProtocol) -> None:
        """handle incoming messages"""
        if self.mqtt_leg is None:
            raise RuntimeError("MQTT leg not initialized")

        async for message in websocket:
            self._log.debug(f"<{message!r}")
            try:
                data = orjson.loads(message)
                operation = data["op"]

                if operation == "subscribe":
                    await self.subscribe(data["topic"])
                elif operation == "unsubscribe":
                    await self.unsubscribe(data["topic"])
                elif operation == "publish":
                    msg = data["msg"]
                    msg_out = base.Message(data["topic"], orjson.dumps(msg))
                    self.mqtt_leg.publish(msg_out)
                else:
                    self._log.error(f"Unknown operation {operation}")

            except (
                orjson.JSONEncodeError,
                orjson.JSONDecodeError,
                KeyError,
                ValueError,
            ) as e:
                self._log.error(f"{e=} {message=!r}")
            except Exception as e:
                # print exception traceback
                self._log.exception(e)

    async def _send_messages(self) -> None:
        """send queue items to clients"""

        while True:
            msg = await self._out_q.get()

            if self._connections:
                self._log.debug(f">{msg=}")

                out = orjson.dumps(
                    {
                        "op": "publish",
                        "topic": msg.topic,
                        "msg": orjson.loads(msg.payload),
                    }
                ).decode("utf-8")

                websockets.broadcast(self._connections, out)
            else:
                self._log.debug(f"Dropped {msg=}")

            self._log.debug(f"queue length = {self._out_q.qsize()}")
            self._out_q.task_done()

    async def main(self) -> None:
        if self.mqtt_leg is None:
            raise RuntimeError("MQTT leg not initialized")
        await websockets.serve(self._handle_connection, CFG.address, CFG.port)
        await self._send_messages()


if __name__ == "__main__":
    logging.info("Starting websocket server")
    server = WsLeg()

    run_main_async(server.main())
