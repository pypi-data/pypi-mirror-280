from typing import List, Tuple

from bs4 import BeautifulSoup

from hrfh.utils.hash import sha256sum
from hrfh.utils.mask import mask_sentence
from hrfh.utils.tokenize import tokenize_html

from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class HTTPResponse:
    ip: str = ""
    port: int = 80
    version: str = "HTTP/1.1"
    status_code: int = 200
    status_reason: str = "OK"
    headers: List[Tuple[str, str]] = field(default_factory=list)
    body: bytes = b""

    def __post_init__(self):
        if self.version == 10:
            self.version = "HTTP/1.0"
        if self.version == 11:
            self.version = "HTTP/1.1"
        self.masked: str = self._mask()

    def __repr__(self) -> str:
        return f"<HTTPResponse {self.ip}:{self.port} {self.status_code} {self.status_reason}>"

    def _mask(self) -> str:
        return self._preprocess()

    def dump(self) -> str:
        lines = [
            f"{self.version} {self.status_code} {self.status_reason}"
        ]
        for key, value in self.headers:
            lines.append(f"{key}: {value}")
        lines.append("")
        lines.append(self.body.decode("utf-8"))
        return "\r\n".join(lines)

    def fuzzy_hash(self, hasher=sha256sum) -> str:
        return hasher(self.masked)
    
    def get_tokenized_body(self) -> List[str]:
        soup = BeautifulSoup(self.body, "html.parser")
        masked_html_tokens = []
        for token in tokenize_html(soup):
            if token.startswith("<") and token.endswith(">"):
                # append html tags
                masked_html_tokens.append(token)
            else:
                # append masked text content
                # TODO: handle random string in javascript by create a abstract syntax tree [1] for <script> tag
                # [1] https://github.com/tree-sitter/py-tree-sitter
                masked_html_tokens.append(mask_sentence(token))
        return masked_html_tokens

    def _preprocess(self) -> str:
        header_lines = []
        strip_headers = [
            "Expires",
            "Date",
            "Content-Length",
            "Location",
            "Via",
            "via",
            "Last-Modified",
        ]
        shoud_not_mask_headers = [
            "Server",
            "Connection",
            "Content-Type",
            "Content-Encoding",
            "Cache-Control",
        ]
        headers = []
        if type(self.headers) is dict:
            headers = self.headers.items()
        else:
            headers = self.headers
        for key, value in headers:
            if key in strip_headers:
                value = "REMOVED"
            elif key in shoud_not_mask_headers:
                value = value
            else:
                value = mask_sentence(value)
            header_lines.append(f"{key}: {value}")
        lines = [f"{self.version} {self.status_code} {self.status_reason}"]
        lines += sorted(header_lines)
        lines.append("")
        lines += self.get_tokenized_body()
        return "\r\n".join(lines)
