from typing import Optional, List, Literal
from pydantic import BaseModel


class ArgSpec(BaseModel):
    name: str
    type: Literal["positional", "vararg", "kwonlyarg", "kwarg"]
    annotation: Optional[str] = None
    default: Optional[str] = None


class ReturnSpec(BaseModel):
    name: str
    annotation: Optional[str] = None


class FuncSpec(BaseModel):
    name: str
    doc: Optional[str]
    arg_specs: Optional[List[ArgSpec]] = None
    return_specs: Optional[List[ReturnSpec]] = None

