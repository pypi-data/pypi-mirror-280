

from ..copier import *
from peewee import Database
from typing import Any, Self, List
from starlette.datastructures import QueryParams
from starlette.applications import Request as StarletteRequest
from ..api.exception import EntityNotFoundException, InvalidArgumentException


class QueryArmoury:
    _db: Database = None
    PERCENTAGE_CHANGE_RELAY_KEY: str = "___percentage_change____"
    BARMOURY_RAW_SQL_PARAMETER_KEY: str = "___BARMOURY__RAW__SQL___"
    
    def __init__(self: Self, db: Database = None):
        self._db = db
    
    async def page_query[T](self: Self, request: StarletteRequest, model: T, resolve_sub_entities: bool = True, pageable: bool = False, logger: Any = None) -> Any:
        count = 0
        result = []
        page_filter = self.build_page_filter(model, model.select(), request.query_params)
        if pageable:
            count = model.select().count()
        page_filter["count"] = count
        rows = page_filter["model_select"].dicts()
        for row in rows:
            model_resource = model()
            Copier.copy(model_resource, row, copy_property=CopyProperty({ "enable_dictionary_lookup": True }))
            result.append(model_resource)
        return self.paginate_result(result, page_filter) if pageable else result
    
    def build_page_filter(self: Self, model: Any, model_select: Any, query: QueryParams):
        order_bys = []
        sorted = False
        paged = "page" in query
        limit = query.get("size")
        page = int(query.get("page") or "1")
        sorts = query.getlist("sort") if "sort" in query else []
        offset = (page - 1) * (int(limit or "10"))
        
        if limit != None:
            model_select = model_select.limit(int(limit))
        if len(sorts) > 0:
            sorted = True
        for sort in sorts:
            sort_parts = sort.split(",")
            field_name = sort_parts[0]
            if field_name not in model.__dict__:
                raise InvalidArgumentException(f"Unknown field '{field_name}' in sort parameter")
            if len(sort_parts) > 1 and sort_parts[1].lower() == "desc":
                order_bys.append(-getattr(model, field_name))
            else:
                order_bys.append(getattr(model, field_name))
        return {
            "page": page,
            "paged": paged,
            "offset": offset,
            "sorted": sorted,
            "limit": int(limit),
            "model_select": model_select.offset(offset).order_by(*order_bys),
        }
    
    def paginate_result(self: Self, rows: List[Any], page_filter: Dict[str, Any]):
        rows_count = len(rows)
        sort = {
            "empty": rows_count == 0,
            "sorted": page_filter["sorted"],
            "unsorted": not page_filter["sorted"],
        }
        return {
            "content": rows,
            "pageable": {
                "sort": sort,
                "offset": page_filter["offset"],
                "page_number": page_filter["page"],
                "page_size": page_filter["limit"],
                "paged": page_filter["paged"],
                "unpaged": not page_filter["paged"],
            },
            "last": page_filter["offset"] >= (page_filter["count"] - page_filter["limit"]),
            "total_pages": int((page_filter["count"] / page_filter["limit"]) + 1),
            "total_elements":     page_filter["count"],
            "first":              page_filter["offset"] == 0,
            "size":               page_filter["limit"],
            "number":             page_filter["page"],
            "sort":               sort,
            "number_of_elements": rows_count,
            "empty":              rows_count == 0,
            
        }
    
    async def get_resource_by_column[T](self: Self, model: T, column: Any, value: Any, message: str) -> T:
        query = {}
        query[column] = value
        resource = model.select().where(column==value).limit(1).dicts()
        if resource != None and len(resource) > 0:
            model_resource = model()
            Copier.copy(model_resource, resource[0], copy_property=CopyProperty({ "enable_dictionary_lookup": True }))
            return model_resource
        raise EntityNotFoundException(message)
    
    async def get_resource_by_id[T](self: Self, model: T, value: Any, message: str) -> T:
        return await self.get_resource_by_column(model, model.id, value, message)