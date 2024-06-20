from typing import Any, Optional
from pydantic import BaseModel, Json

from pfpy.types.check_types import CheckErrorTypes


class PassFortEntityDataCheckWarning(BaseModel):
    type: CheckErrorTypes
    message: str


class PassFortEntityDataCheckError(PassFortEntityDataCheckWarning):
    subType: Optional[str] = None
    data: Optional[Json[Any]] = None
