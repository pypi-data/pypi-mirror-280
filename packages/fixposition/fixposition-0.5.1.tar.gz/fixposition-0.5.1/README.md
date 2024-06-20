# fixposition


Python driver for fixposition gps

**NOTE: work-in-progress**


## Usage


Message parsing:

```python


from fixposition import parser

msg = "$GPHDT,61.7,T*05\r\n"

data = parser.parse(msg)


```



## How it works
*or rather how it should work, working on it ...*

* message definitions are in `fixposition.messages`. Each submodule contains a `parse()`
function.
* `@validate_checksum` decorator adds nmea checksum to parse function.
* `parser.parse(msg)` returns `NamedTuple` of a message


## References

* [FP_A messages](https://docs.fixposition.com/fd/fp_a-messages)
* [FP_A-ODOMETRY](https://docs.fixposition.com/fd/fp_a-odometry)


## Development


1. develop and test in devcontainer (VSCode)
2. trigger ci builds by bumping version with a tag. (see `.gitlab-ci.yml`)

## Tooling

* Verisoning : `bump2version`
* Linting and formatting : `ruff`
* Typechecking: `mypy`

## What goes where
* `src/fixposition` app code. `pip install .` .
* `docker` folder contains dockerfiles for images.
* `.gitlab-ci.yml` takes care of the building steps.
