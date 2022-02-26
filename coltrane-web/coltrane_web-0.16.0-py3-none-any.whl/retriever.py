import json
import logging
import warnings
from pathlib import Path
from typing import Dict, Iterable

from .config.cache import DataCache
from .config.paths import get_content_directory, get_data_directory, get_data_json
from .utils import dict_merge


logger = logging.getLogger(__name__)


def get_data() -> Dict:
    """
    Get and merge data from `data.json` and any JSON files recursively found in the
    `data` directory.
    """

    data = {}
    data_cache = DataCache()
    cache_key = ""

    if data_cache.is_enabled:
        cache_key = f"{data_cache.cache_key_namespace}data"
        data = data_cache.cache.get(cache_key, {})

        if data:
            return data

    try:
        data = json.loads(get_data_json().read_bytes())

        warnings.warn(
            "Reading data.json will be deprecated in future versions; use the data directory instead."
        )
    except FileNotFoundError:
        logger.debug("Missing data.json file")

    data_directory = get_data_directory()

    for path in data_directory.rglob("*.json"):
        if path.is_file():
            directory_without_base_and_file_name = (
                (str(path)).replace(str(data_directory), "").replace(path.name, "")
            )

            file_name = path.name.replace(".json", "")
            new_data = {file_name: json.loads(path.read_bytes())}

            # For each part of the path between BASE_DIR/data and the JSON file,
            # add a new level (i.e. key) in the data dictionary; for example:
            # base_dir/data/some/new/test/here.json with {"one": "two"} ==
            # {"some": {"new": {"test": {"here": {"one": "two"}}}}}
            for key in reversed(directory_without_base_and_file_name.split("/")):
                if key:
                    new_data = {key: new_data}

            data = dict_merge(data, new_data)

    if data_cache.is_enabled:
        data_cache.cache.set(cache_key, data, timeout=data_cache.seconds)

    return data


def get_content_paths(slug: str = None) -> Iterable[Path]:
    """
    Yield `Path`s for all markdown content in the content directory.
    """

    directory = get_content_directory()

    if slug:
        directory = directory / slug

    if not directory.exists():
        raise FileNotFoundError(f"Directory does not exist: {directory}")

    paths = directory.rglob("*.md")

    for path in paths:
        if path.is_file():
            yield path
