from enum import Enum


class PassfortConfigCheckType(Enum):
    CompanyCustom = "COMPANY_CUSTOM"
    IdentityCheck = "IDENTITY_CHECK"
    IndividualCustom = "INDIVIDUAL_CUSTOM"
    DocumentVerification = "DOCUMENT_VERIFICATION"
    DocumentFetch = "DOCUMENT_FETCH"
    CompanyData = "COMPANY_DATA"


class PassfortConfigCheckTemplateType(Enum):
    OneTimeSynchronous = "ONE_TIME_SYNCHRONOUS"
    OneTimeCallback = "ONE_TIME_CALLBACK"


class ProviderDataType(Enum):
    DEMO_RESULT = "Demo Result"


class PassfortConfigSupportedFeatures(Enum):
    ExternalEmbed = "EXTERNAL_EMBED"
    CompanySearch = "COMPANY_SEARCH"


class CheckErrorTypes(Enum):
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"
    MISSING_QUERY_PARAMS = "MISSING_QUERY_PARAMS"
    SIGNATURE_ERROR = "SIGNATURE_ERROR"
    INVALID_CONFIG = "INVALID_CONFIG"
    INVALID_CHECK_INPUT = "INVALID_CHECK_INPUT"
    MISSING_CHECK_INPUT = "MISSING_CHECK_INPUT"
    UNSUPPORTED_COUNTRY = "UNSUPPORTED_COUNTRY"
    PROVIDER_CONNECTION = "PROVIDER_CONNECTION"
    PROVIDER_MESSAGE = "PROVIDER_MESSAGE"
    UNSUPPORTED_DEMO_RESULT = "UNSUPPORTED_DEMO_RESULT"
