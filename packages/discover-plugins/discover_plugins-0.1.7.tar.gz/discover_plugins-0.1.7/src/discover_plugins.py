import argparse
import inspect
import json
import logging
import subprocess
import sys
from importlib.metadata import EntryPoints
from importlib.metadata import entry_points

logger = logging.getLogger("discover-plugins")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name")
    parser.add_argument("--value")
    parser.add_argument("--group")
    parser.add_argument("--verbose", "-v", action="store_true")

    options = parser.parse_args()
    if options.verbose:
        logging.basicConfig(
            stream=sys.stderr,
            level=logging.DEBUG,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
    eps = discover(name=options.name, value=options.value, group=options.group)
    print(json.dumps(entrypoints_to_dict(eps)))
    raise SystemExit(0)


def discover(
    name: str | None = None, value: str | None = None, group: str | None = None
):
    kwargs = {}
    if name:
        kwargs.update(name=name)
    if value:
        kwargs.update(value=value)
    if group:
        kwargs.update(group=group)
    logger.debug("discovering plugins for interpreter %s", sys.executable)
    eps = entry_points(**kwargs)
    return eps


def source_file():
    this = sys.modules[__name__]
    return inspect.getsourcefile(this)


def inject():
    parser = argparse.ArgumentParser(
        description="Discover entrypoints available for different python environments."
    )
    parser.add_argument("--name", help="filter entrypoints by name")
    parser.add_argument("--value", help="filter entrypoint by value")
    parser.add_argument("--group", help="filter entrypoints by group")
    parser.add_argument(
        "--interpreter",
        default="python",
        help="specify the python interpreter to use. Defaults to first python executable on PATH",
    )
    parser.add_argument("--verbose", "-v", action="store_true", default=False)

    options = parser.parse_args()

    code = source_file()
    cmd = [options.interpreter, code]
    if options.group:
        cmd.extend(["--group", options.group])
    if options.value:
        cmd.extend(["--value", options.value])
    if options.name:
        cmd.extend(["--name", options.name])
    if options.verbose:
        cmd.append("--verbose")
    if options.interpreter:
        out = subprocess.run(cmd, stdout=subprocess.PIPE)
        print(out.stdout.decode())
        raise SystemExit(out.returncode)

    eps = discover(name=options.name, value=options.value, group=options.group)
    print(json.dumps(entrypoints_to_dict(eps)))


def entrypoints_to_dict(eps: EntryPoints) -> dict:
    return {
        g: [
            dict(name=e.name, group=e.group, value=e.value) for e in eps.select(group=g)
        ]
        for g in eps.groups
    }


if __name__ == "__main__":
    main()
