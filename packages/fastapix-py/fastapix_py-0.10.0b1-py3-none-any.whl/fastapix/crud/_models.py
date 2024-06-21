# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : zhangzhanqi
# @FILE     : _models.py
# @Time     : 2023/10/29 15:45
from typing import Type, Optional, List

from pydantic import BaseModel
from sqlmodel import SQLModel

from fastapix.common.pydantic import (
    PYDANTIC_V2, ModelField, FieldInfo,
    create_model_by_fields, model_fields
)

FOREIGN_FIELD_NAME = "x_foreign"


def create_schema_read(model: Type[SQLModel], foreign_models: Optional[List[Type[SQLModel]]] = None) -> Type[BaseModel]:
    fields = [
        field
        for name, field in model_fields(model).items()
        if getattr(field.field_info, 'read', True)
    ]
    if foreign_models:
        foreign_class = create_model_by_fields(
            name=f"{model.__name__}ReadForeign",
            fields=[ModelField(
                field_info=FieldInfo(default=None, annotation=Optional[create_schema_read(foreign_model)]),
                name=foreign_model.__tablename__
            ) for foreign_model in foreign_models],
        )
        fields.append(ModelField(
            name=FOREIGN_FIELD_NAME,
            field_info=FieldInfo(default=None, annotation=Optional[foreign_class]),
        ))
    return create_model_by_fields(
        name=f"{model.__name__}Read",
        fields=fields,
        orm_mode=True,
        extra="allow",
        mode="read",
        __config__=model.model_config if PYDANTIC_V2 else model.Config
    )


def create_schema_update(model: Type[SQLModel]) -> Type[BaseModel]:
    fields = [
        field
        for name, field in model_fields(model).items()
        if getattr(field.field_info, 'update', True)
    ]
    return create_model_by_fields(
        name=f"{model.__name__}Update",
        fields=fields,
        set_none=True,
        __config__=model.model_config if PYDANTIC_V2 else model.Config
    )


def create_schema_create(model: Type[SQLModel]) -> Type[BaseModel]:
    fields = [
        field
        for name, field in model_fields(model).items()
        if getattr(field.field_info, 'create', True)
    ]
    return create_model_by_fields(
        name=f"{model.__name__}Create",
        fields=fields,
        __config__=model.model_config if PYDANTIC_V2 else model.Config
    )
