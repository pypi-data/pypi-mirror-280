import json
from datetime import timedelta
from typing import Annotated, Any, Iterable

from jwt import PyJWT
from nestipy.common import Injectable
from nestipy.ioc import Inject

from .jwt_builder import JWT_OPTION_TOKEN, JwtOption


@Injectable()
class JwtService(PyJWT):
    _options: Annotated[JwtOption, Inject(JWT_OPTION_TOKEN)]

    def __init__(self):
        super().__init__()

    def encode(
            self,
            payload: dict[str, Any],
            key: str | bytes | None = None,
            algorithm: str | None = None,
            headers: dict[str, Any] | None = None,
            json_encoder: type[json.JSONEncoder] | None = None,
            sort_headers: bool = True
    ):
        return super().encode(
            payload,
            key or self._options.secret,
            algorithm or self._options.algorithms or "HS256",
            headers,
            json_encoder, sort_headers
        )

    def decode(
            self,
            jwt: str | bytes,
            key: str | bytes | None = None,
            algorithms: list[str] | None = None,
            options: dict[str, Any] | None = None,
            verify: bool | None = None,
            detached_payload: bytes | None = None,
            audience: str | Iterable[str] | None = None,
            issuer: str | None = None,
            leeway: float | timedelta = 0,
            **kwargs: Any,
    ) -> Any:
        return super().decode(
            jwt,
            key or self._options.secret,
            algorithms or ["HS256"],
            options,
            verify,
            detached_payload,
            audience,
            issuer,
            leeway,
            **kwargs
        )
