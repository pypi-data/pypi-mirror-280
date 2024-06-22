import json
import subprocess
import sys
from importlib.metadata import entry_points

import pytest

from discover_plugins import entrypoints_to_dict


@pytest.fixture
def interpreter(tmp_path):
    path = tmp_path / "venv"
    out = subprocess.run([sys.executable, "-m", "virtualenv", path.as_posix()])
    assert out.returncode == 0
    return path / "bin/python"


def test_discover_plugins_returns_valid_json(interpreter):
    out = subprocess.run([interpreter, "-m", "pip", "install", "./testdata/packages/myplugin"])
    out = subprocess.run(["discover-plugins", "--interpreter", interpreter], stdout=subprocess.PIPE)
    json.loads(out.stdout)
    assert out.returncode == 0


def test_discover_plugins_for_specified_interpreter(interpreter):
    out = subprocess.run([interpreter, "-m", "pip", "install", "./testdata/packages/myplugin"])
    out = subprocess.run(["discover-plugins", "--interpreter", interpreter])
    assert out.returncode == 0


def test_discover_plugins_for_selected_groups(interpreter):
    out = subprocess.run([interpreter, "-m", "pip", "install", "./testdata/packages/myplugin"])
    out = subprocess.run(
        ["discover-plugins", "--interpreter", interpreter, "--group", "entry_point_name"], stdout=subprocess.PIPE
    )
    eps = json.loads(out.stdout)
    assert "entry_point_name" in eps
    assert len(eps) == 1
    assert len(eps["entry_point_name"]) == 1


def test_discover_plugins_for_selected_name(interpreter):
    out = subprocess.run([interpreter, "-m", "pip", "install", "./testdata/packages/myplugin"])
    out = subprocess.run(["discover-plugins", "--interpreter", interpreter, "--name", "name"], stdout=subprocess.PIPE)
    eps = json.loads(out.stdout)
    assert "entry_point_name" in eps
    assert len(eps) == 1
    assert len(eps["entry_point_name"]) == 1


def test_discover_plugins_for_selected_value(interpreter):
    out = subprocess.run([interpreter, "-m", "pip", "install", "./testdata/packages/myplugin"])
    out = subprocess.run(
        ["discover-plugins", "--interpreter", interpreter, "--value", "myplugin:main"], stdout=subprocess.PIPE
    )
    eps = json.loads(out.stdout)
    assert "entry_point_name" in eps
    assert len(eps) == 1
    assert len(eps["entry_point_name"]) == 1


def test_entrypoints_conversion_can_be_json_encoded():
    eps = entry_points()
    d = entrypoints_to_dict(eps)
    assert json.dumps(d)
