from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

from pfpy.types.check_types import ProviderDataType
from pfpy.types.error_types import (
    PassFortEntityDataCheckError,
    PassFortEntityDataCheckWarning,
)


class ExternalResourceType(Enum):
    EMBED = "EMBED"


class ExternalResources(BaseModel):
    type: Optional[ExternalResourceType] = None
    url: Optional[str] = None
    id: Optional[str] = None
    label: Optional[str] = None


class ResultDecisionType(Enum):
    PASS = "PASS"
    PARTIAL = "PARTIAL"
    FAIL = "FAIL"
    ERROR = "ERROR"


class ResultDecisionSummaryType(Enum):
    PASS = "The custom check has passed"
    FAIL = "The custom check has failed"
    FAIL_NO_ENTITY_FOUND = "No entity record found"
    DATA_INCONCLUSIVE = "Data inconclusive for this check"
    ERROR = "This check ERRORED please try again shortly"


class ResultDecision(BaseModel):
    decision: ResultDecisionType
    summary: ResultDecisionSummaryType


class PassFortEntityDataCheck(BaseModel):
    provider_data: ProviderDataType | str | int
    result: ResultDecision
    external_resources: Optional[List[ExternalResources]] = None
    warnings: Optional[List[PassFortEntityDataCheckWarning]] = None
    errors: Optional[List[PassFortEntityDataCheckError]] = None
