from enum import Enum

# Don't remove. Import for not repetitive implementation
from sqlexecutorx import DBError


class MapperError(DBError):
    pass


class NotFoundError(DBError):
    pass


class SqlAction(Enum):
    CALL = 'call'
    INSERT = 'insert'
    UPDATE = 'update'
    DELETE = 'delete'
    SELECT = 'select'
