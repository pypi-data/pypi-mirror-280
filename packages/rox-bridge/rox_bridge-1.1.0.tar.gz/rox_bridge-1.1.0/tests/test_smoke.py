# basic tests


def test_main() -> None:
    from rox_bridge.mqtt_leg import MqttLeg

    MqttLeg()

    from rox_bridge.ws_leg import WsLeg

    WsLeg()
