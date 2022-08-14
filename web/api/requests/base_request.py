from __future__ import annotations

from drf_yasg.openapi import Schema
from pydantic import BaseModel


class BaseRequest(BaseModel):
    """Represents a base request."""

    @classmethod
    def get_request_schema(cls: BaseModel) -> Schema:
        """
        Return schema of response.

        Returns:
            Schema
        """
        return Schema(**cls.schema())
