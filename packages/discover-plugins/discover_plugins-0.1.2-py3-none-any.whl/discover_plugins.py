import argparse
import sys

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name")
    parser.add_argument("--value")
    parser.add_argument("--group")

    options = parser.parse_args()
    print(discover(name=options.name, value=options.value, group=options.group))


def discover(name: str | None = None, value: str | None = None, group: str | None = None):
    kwargs = {}
    if name:
        kwargs.update(name=name)
    if value:
        kwargs.update(value=value)
    if group:
        kwargs.update(group=group)
    eps = entry_points(**kwargs)
    return eps

if __name__ == "__main__":
    main()
