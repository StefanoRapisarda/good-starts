import pytest
from pathlib import Path
from tempfile import TemporaryDirectory, NamedTemporaryFile
import os

from src.good_starts.main import FileSystemEntity

@pytest.fixture
def temp_file():
    with NamedTemporaryFile(delete=False) as tmp_file:
        yield tmp_file.name
    os.remove(tmp_file.name)

@pytest.fixture
def temp_directory():
    with TemporaryDirectory() as tmp_dir:
        yield tmp_dir

def test_filesystem_entity_file(temp_file):
    entity = FileSystemEntity(temp_file)
    assert entity.path == Path(temp_file)
    assert entity.name == Path(temp_file).name
    assert entity.type == 'File'

def test_filesystem_entity_directory(temp_directory):
    entity = FileSystemEntity(temp_directory)
    assert entity.path == Path(temp_directory)
    assert entity.name == Path(temp_directory).name
    assert entity.type == 'Directory'

def test_filesystem_entity_unknown():
    entity = FileSystemEntity('/path/to/nonexistent')
    assert entity.path == Path('/path/to/nonexistent')
    assert entity.name == 'nonexistent'
    assert entity.type == 'Unknown'