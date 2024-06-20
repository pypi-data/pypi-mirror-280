# mqtt-bridge



Bridge mqtt <--> websocket



Docker image:

    docker run --network=host registry.gitlab.com/roxautomation/components/mqtt-bridge

**Configuration**

override these environment variables if desired

* `WS_PORT=9095`
* `MQTT_HOST=localhost`
* `MQTT_PORT=1883`


## How it works

* web ui connects to websocket. It then subscibes to topics or publishes data.
* messages are forwarded between websocket and mqtt.


**Note** current implementation is quite simple, there is in distinction between topic subscriptions from clients. All clients will receive all subscriptions.

## Protocol
The protocol is subset of [rosbridge protocol](https://github.com/biobotus/rosbridge_suite/blob/master/ROSBRIDGE_PROTOCOL.md)

* subscribe `{"op":"subscribe", "topic":<string>}"`
* publish `{"op":"publish", "topic": <string>, "msg":<json>}`




## Quick start

1. open in VSCode devcontainer, develop.
2. use `invoke` to lint, build etc.

## Tooling

* Verisoning : `bump2version`
* Linting and formatting : `ruff`
* Typechecking: `mypy`

## What goes where
* `src/rox_bridge` app code. `pip install .` .
* `docker` folder contains dockerfiles for images.
* `.gitlab-ci.yml` takes care of the building steps.
