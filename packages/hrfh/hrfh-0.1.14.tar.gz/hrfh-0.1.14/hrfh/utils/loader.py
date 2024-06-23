import glob
import json
from typing import Generator

from hrfh.models import HTTPResponse
from hrfh.utils.parser import (
    create_http_response_from_bytes,
    create_http_response_from_json,
)


def yield_http_response_from_json(
    folder, limit=4
) -> Generator[HTTPResponse, None, None]:
    for index, path in enumerate(glob.glob(f"{folder}/**/*.json", recursive=True)):
        with open(path) as f:
            if index > limit:
                break
            yield create_http_response_from_json(json.load(f))


def yield_http_response_from_plain(
    folder, limit=4
) -> Generator[HTTPResponse, None, None]:
    for index, path in enumerate(glob.glob(f"{folder}/**/*.txt", recursive=True)):
        with open(path, mode="rb") as f:
            if index > limit:
                break
            yield create_http_response_from_bytes(f.read())
