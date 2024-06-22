import http.client
import io

from hrfh.models import HTTPResponse


class FakeSocket:
    def __init__(self, bytes_stream):
        self._file = bytes_stream

    def makefile(self, *args, **kwargs):
        return self._file


def create_http_response_from_bytes(data: bytes) -> HTTPResponse:
    response_stream = FakeSocket(io.BytesIO(data))
    response = http.client.HTTPResponse(response_stream)
    response.begin()
    return HTTPResponse(
        ip="1.1.1.1",
        port=80,
        version=response.version,
        status_code=response.status,
        status_reason=response.reason,
        # NOTE: the order of headers will be lost if we insist to use response.getheaders()
        headers=response.getheaders(),
        body=response.read(),
    )


def create_http_response_from_json(data: dict):
    return HTTPResponse(
        ip=data.get("ip"),
        port=data.get("port", 80),
        status_code=data.get("status_code"),
        status_reason=data.get("status_reason"),
        headers=data.get("headers"),
        body=data.get("body"),
    )
