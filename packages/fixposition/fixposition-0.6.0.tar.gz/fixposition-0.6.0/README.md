# fixposition


Python driver for fixposition gps

**NOTE: work-in-progress**

Currently these messages are supported: **GGA,HDT,ODOMETRY**

## Functionality overview

* `parser.parse(msg: str, ignore: List[str] = []) -> FPX_Message | None:` - parse NMEA message to a NamedTuple
* record and replay messages with `fixposition` cli
* use `gps_node.FpxNode` class as async node to interface with fixposition device over socket.


## Usage


Message parsing:

```python


from fixposition import parser

msg = "$GPHDT,61.7,T*05\r\n"

data = parser.parse(msg)


```

## CLI tool

This package provides a command-line tool `fixposition`:

    Usage: fixposition [OPTIONS] COMMAND [ARGS]...

    Options:
    --version  Show the version and exit.
    --help     Show this message and exit.

    Commands:
    listen  Listen to messages and print them to stdout
    node    Start the gps node
    record  Record messages to file
    replay  Replay messages from a file or default data if not provided.

## How it works

* message definitions are in `fixposition.messages`. Each submodule contains a `parse()`
function.
* `@validate_checksum` decorator adds nmea checksum to parse function.
* `parser.parse(msg)` returns `NamedTuple` of a message

See `.messages` code, extending this should be easy.


## References

* [FP_A messages](https://docs.fixposition.com/fd/fp_a-messages)
* [FP_A-ODOMETRY](https://docs.fixposition.com/fd/fp_a-odometry)
* [HDT](https://docs.fixposition.com/fd/nmea-gp-hdt)
* [GGA](https://docs.fixposition.com/fd/nmea-gp-gga)


## Development


*  develop and test in devcontainer (VSCode)
*  devops are managed with `invoke` , see `tasks.py`


## Tooling

* Verisoning : `bump2version`
* Linting : `pylint`
* Formatting: `black`
* Typechecking: `mypy`
* scripting: `invoke` : see `tasks.py`

## What goes where
* `src/fixposition` app code. `pip install .` .
* `tasks.py` automates common tasks with `invoke`
