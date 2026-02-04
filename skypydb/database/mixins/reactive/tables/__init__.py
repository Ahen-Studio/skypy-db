"""
tables module.
"""

from .syscreate import SysCreate
from .sysdelete import SysDelete
from .sysget import SysGet
from .audit import AuditTable

__all__ = [
    "SysCreate",
    "SysDelete",
    "SysGet",
    "AuditTable"
]
