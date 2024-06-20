import glob
import json
from typing import Generator

from hrfh.models import HTTPResponse
from hrfh.utils.parser import load_from_byte_stream


def yield_http_response_from_json(folder, limit=4) -> Generator[HTTPResponse, None, None]:
    for index, path in enumerate(glob.glob(f"{folder}/**/*.json", recursive=True)):
        with open(path) as f:
            if index > limit:
                break
            data = json.load(f)
            yield HTTPResponse(
                ip=data.get("ip"),
                port=data.get("port", 80),
                status_code=data.get("status_code"),
                status_reason=data.get("status_reason"),
                headers=data.get("headers"),
                body=data.get("body"),
            )


def yield_http_response_from_plain(folder, limit=4) -> Generator[HTTPResponse, None, None]:
    for index, path in enumerate(glob.glob(f"{folder}/**/*.txt", recursive=True)):
        with open(path, mode="rb") as f:
            if index > limit:
                break
            yield load_from_byte_stream(f.read())
