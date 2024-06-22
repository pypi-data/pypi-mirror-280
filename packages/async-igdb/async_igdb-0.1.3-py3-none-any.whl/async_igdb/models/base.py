from datetime import datetime
import math
from typing import (
    Annotated,
    Any,
    ClassVar,
    Literal,
    Self,
    Type,
    TypeVar,
    get_type_hints,
)
from pydantic import BaseModel, computed_field
from pydantic.functional_serializers import SerializeAsAny, field_serializer
from pydantic.functional_validators import model_validator
from ..client import BaseClient

TBase = TypeVar("TBase", bound="BaseApiModel")


class IDWrapper:
    def __init__(self, factory: TBase | str):
        self.factory = factory

    @property
    def type(self) -> str:
        if type(self.factory) == str:
            return self.factory
        else:
            return self.factory.type

    async def resolve(
        self, client: BaseClient, ids: list[int], step: int = 100
    ) -> list[TBase]:
        results = []
        _type = self.type
        for i in range(0, math.ceil(len(ids) / step)):
            results.extend(
                [
                    client.REGISTRY[_type](client=client, **i)
                    for i in await client.build_query(
                        _type, ids=ids, limit=step, offset=step * i
                    )
                ]
            )
        return results


def ids(base: Type[TBase] | str):
    if type(base) == str:
        return Annotated[list[int] | int, IDWrapper(base)] | None | Any
    else:
        return (
            Annotated[list[int | TBase] | TBase, IDWrapper(base)]
            | TBase
            | list[TBase | int]
            | TBase
            | None
            | Any
        )


class BaseApiModel(BaseModel):
    type: ClassVar[str | None] = None
    searchable: ClassVar[bool] = False
    fields: ClassVar[list[str] | Literal["*"]] = "*"
    _client: BaseClient
    model_config = {"arbitrary_types_allowed": True, "protected_namespaces": ()}

    model_type: str | None = None
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    checksum: str | None = None
    url: str | None = None

    def __init__(self, client: BaseClient = None, **data):
        super().__init__(client=client, **data)
        self._client = client

    @computed_field
    @property
    def uuid(self) -> str:
        return f"{self.type if self.type else self.model_type}:{self.id}"

    @field_serializer("model_type", when_used="always")
    def ser_model_type(self, value) -> str:
        if not self.model_type:
            return self.type
        return self.model_type

    @model_validator(mode="after")
    def swap_correct_models(self) -> Self:
        if not hasattr(self, "_client"):
            return self
        if not self.client:
            return self
        fields = self.id_fields
        for field in fields.keys():
            current = getattr(self, field)
            if type(current) == list:
                new_field = []
                for item in current:
                    if (
                        type(item) == dict
                        and "model_type" in item.keys()
                        and item["model_type"] in self.client.REGISTRY.keys()
                    ):
                        new_field.append(
                            self.client.REGISTRY[item["model_type"]](
                                client=self.client, **item
                            )
                        )
                    elif isinstance(item, BaseApiModel):
                        if item.model_type:
                            new_field.append(
                                self.client.REGISTRY[item.model_type](
                                    client=self.client, **item.model_dump()
                                )
                            )
                        else:
                            new_field.append(
                                self.client.REGISTRY[item.type](
                                    client=self.client, **item.model_dump()
                                )
                            )
                    else:
                        new_field.append(item)
                setattr(self, field, new_field)
            elif isinstance(current, BaseApiModel):
                if current.model_type:
                    setattr(
                        self,
                        field,
                        self.client.REGISTRY[current.model_type](
                            client=self.client, **current.model_dump()
                        ),
                    )
                else:
                    setattr(
                        self,
                        field,
                        self.client.REGISTRY[current.type](
                            client=self.client, **current.model_dump()
                        ),
                    )
            elif (
                type(current) == dict
                and "model_type" in current.keys()
                and current["model_type"] in self.client.REGISTRY.keys()
            ):
                setattr(
                    self,
                    field,
                    self.client.REGISTRY[current["model_type"]](
                        client=self.client, **current
                    ),
                )

        return self

    @classmethod
    async def from_request(
        cls: Type[TBase],
        client: BaseClient,
        ids: list[int] | None = None,
        filter: str | None = None,
        sort_field: str | None = None,
        sort_direction: Literal["asc", "desc"] = "asc",
        search: str | None = None,
        limit: int = 10,
        offset: int = 0,
    ) -> list[TBase]:
        if search and not cls.searchable:
            raise ValueError("This model is non-searchable.")
        result = await client.build_query(
            cls.type,
            fields=cls.fields,
            ids=ids,
            filter=filter,
            sort_field=sort_field,
            sort_direction=sort_direction,
            limit=limit,
            offset=offset,
        )
        return [cls(client=client, **r) for r in result]

    @property
    def client(self):
        return self._client

    @property
    def id_fields(self) -> dict[str, IDWrapper]:
        hints = get_type_hints(
            self,
            include_extras=True,
            globalns=dict(
                **globals(), **{v.__name__: v for v in self.client.REGISTRY.values()}
            ),
        )
        fields: dict[str, IDWrapper] = {}
        for key, value in hints.items():
            if getattr(value, "__name__", None) == "Annotated" and hasattr(
                value, "__metadata__"
            ):
                for i in value.__metadata__:
                    if isinstance(i, IDWrapper):
                        fields[key] = i

            if getattr(value, "__name__", None) == "Union":
                for i in value.__args__:
                    if getattr(i, "__name__", None) == "Annotated" and hasattr(
                        i, "__metadata__"
                    ):
                        for j in i.__metadata__:
                            if isinstance(j, IDWrapper):
                                fields[key] = j
                                break

        return fields
