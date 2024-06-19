from http import HTTPStatus
from re import Pattern
from typing import Callable, Optional, Union

from galileo_core.constants.request_method import RequestMethod
from galileo_core.helpers.dependencies import is_dependency_available

if is_dependency_available("pytest") and is_dependency_available("respx"):
    from pytest import fixture
    from respx import MockRouter, Route

    @fixture
    def mock_request(respx_mock: MockRouter) -> Callable:
        def curry(
            method: RequestMethod,
            path: Union[str, Pattern],
            params: Optional[dict] = None,
            status_code: int = HTTPStatus.OK,
            json: Optional[dict] = None,
            text: Optional[str] = None,
        ) -> Route:
            if isinstance(path, str):
                path = "/" + path
            if not text and not json:
                json = {}
            return respx_mock.request(
                method=method,
                # Match any URL that ends with the path.
                url=path,
                params=params,
            ).respond(status_code=status_code, text=text, json=json)

        return curry
