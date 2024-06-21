from typing import Any, AsyncGenerator, Literal, Type, TypeVar
from .models import *
from .client import BaseClient

TModel = TypeVar("TModel", bound=BaseApiModel)


class ApiObjectManager[TModel]:
    def __init__(self, client: BaseClient, model_factory: Type[TModel]):
        self.client = client
        self.model_factory = model_factory

    async def get_by_id(self, id: str) -> TModel | None:
        results = await self.model_factory.from_request(self.client, ids=[id], limit=1)
        if len(results) > 0:
            return results[0]
        return None

    async def find(
        self,
        ids: list[int] | None = None,
        filter: str | None = None,
        sort_field: str | None = None,
        sort_direction: Literal["asc", "desc"] = "asc",
        search: str | None = None,
        limit: int = 10,
        offset: int = 0,
    ) -> list[TModel]:
        return await self.model_factory.from_request(
            self.client,
            ids=ids,
            filter=filter,
            sort_field=sort_field,
            sort_direction=sort_direction,
            search=search,
            limit=limit,
            offset=offset,
        )

    async def find_one(
        self,
        ids: list[int] | None = None,
        filter: str | None = None,
        sort_field: str | None = None,
        sort_direction: Literal["asc", "desc"] = "asc",
        search: str | None = None,
    ) -> TModel | None:
        results = await self.find(
            ids=ids,
            filter=filter,
            sort_field=sort_field,
            sort_direction=sort_direction,
            search=search,
        )
        if len(results) > 0:
            return results[0]
        return None

    async def find_paginated(
        self,
        ids: list[int] | None = None,
        filter: str | None = None,
        sort_field: str | None = None,
        sort_direction: Literal["asc", "desc"] = "asc",
        search: str | None = None,
        start_offset: int = 0,
        per_page: int = 10,
    ) -> AsyncGenerator[list[TModel], None]:
        offset = start_offset
        while True:
            page_results = await self.find(
                ids=ids,
                filter=filter,
                sort_field=sort_field,
                sort_direction=sort_direction,
                search=search,
                limit=per_page,
                offset=offset,
            )
            if len(page_results) == 0:
                return
            yield page_results
            offset += per_page

    async def find_all(
        self,
        ids: list[int] | None = None,
        filter: str | None = None,
        sort_field: str | None = None,
        sort_direction: Literal["asc", "desc"] = "asc",
        search: str | None = None,
    ) -> AsyncGenerator[TModel, None]:
        async for page in self.find_paginated(
            ids=ids,
            filter=filter,
            sort_field=sort_field,
            sort_direction=sort_direction,
            search=search,
        ):
            for item in page:
                yield item
