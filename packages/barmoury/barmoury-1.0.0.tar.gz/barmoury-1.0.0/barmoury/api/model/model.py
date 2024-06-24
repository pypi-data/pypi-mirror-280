
from peewee import *
from ...copier import *
from ...eloquent import *
from ..timeo import resolve
from .user_details import *
from typing import Self, Any
from datetime import datetime
from peewee import Model as PeeweeModel
from ...util import json_property, MetaObject


def serializer(obj):
    return obj.__data__


@json_property(serializer=serializer)
class Model(PeeweeModel):
    
    id: BigAutoField = BigAutoField(unique=True, primary_key=True, null=True)
    created_at: DateTimeField = DateTimeField(default=datetime.now())
    updated_at: DateTimeField = DateTimeField(default=datetime.now())
    
    def resolve(self: Self, base_request: 'Request', query_armoury: QueryArmoury = None, user_details: UserDetails = None) -> Self:
        Copier.copy(self, base_request)
        resolve(self)
        return self


class Request(MetaObject):
    
    ___BARMOURY_UPDATE_ENTITY_ID___: Any = None