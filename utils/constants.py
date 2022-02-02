"""Constants StatusCodes and Messages"""

# HTTP Status Codes
SUCCESS_FETCH = 200
SUCCESS_UPDATED = 200
SUCCESS_CREATED = 201
SUCCESS_DELETED = 204
ERROR_BAD_REQUEST = 400
ERROR_UNAUTHORIZED = 401
ERROR_FORBIDDEN = 403
ERROR_NOT_FOUND = 404
ERROR_INTERNAL_SERVER_ERROR = 501
ERROR_FOUND = 302

# Success constants
SUCCESS_USER_FLOW_CREATED = "User Flow Created"
SUCCESS_KYC_DETAILS = "KYC Details"
SUCCESS_KYC_DETAILS_UPDATED = "KYC Details Updated"
SUCCESS_OTHER_USER_FLOW_CREATED = "Other User Flow Created"
SUCCESS_ADDRESS_MAPPING = "Autocomplete Address Mapping"
SUCCESS_BANK_MAPPING = "Autocomplete Bank Mapping"
SUCCESS_BROKER_MAPPING = "Autocomplete Broker Mapping"
SUCCESS_RATE_MAPPING = "Autocomplete Rate Mapping"
SUCCESS_DEMAT_PDF = "Demat PDF Created"
SUCCESS_ORGANIZATION_MAPPING = "Autocomplete Organization Mapping"
SUCCESS_KYC_LISTING = "KYC Listing"
SUCCESS_KYC_DETAILS_ARCHIVED = "KYC Details Archived"
SUCCESS_KYC_DETAILS_ACCEPTED = "KYC Details Accepted"
SUCCESS_KYC_DETAILS_REJECTED = "KYC Details Rejected"
SUCCESS_EMAIL_SEND = "Email Send"
SUCCESS_SMS_SEND = "SMS Send"
SUCCESS_STATISTICS = "Statistics extracted successfully"
SUCCESS_PAYMENT = "Payment extracted successfully"


# Error constants
ERROR_USER_EXIST = "User Exist"
ERROR_SERVER_DOWN = "Server Down"
ERROR_USER_DOES_NOT_EXIST = "KYC Details Doesn't Exist"
ERROR_MINOR_STATE = "Minor state cannot be updated at this point"
ERROR_EMAIL_EXISTS = "User with this Email already Exists"
ERROR_PHONE_EXISTS = "User with this Phone Number already Exists"
ERROR_QUERY_PARAMS_REQUIRED = "Query Params Required"
ERROR_ORDER_BY_NOT_FOUND = "Order by param is required"
ERROR_CASE_IS_REQUIRED = "Operation type is required"
ERROR_ACCOUNT_TYPE_MESSAGE_AND_STATUS_REQUIRED = (
    "Account type, message and status is required"
)
ERROR_PHONE_NUMBER_SAME_REFERENCE_NUMBER = "Alternate and Phone Number cannot be same"
ERROR_MINOR_NOMINEE_DETAILS_SAME_GUARDIAN_DETAILS = (
    "Nominee and Guardian cannot be same"
)
ERROR_STATUS_NOT_FOUND = "Status not found"
ERROR_ACCOUNT_TYPE_NOT_FOUND = "Account Type not found"
ERROR_REJECTION_REASON_REQUIRED = "Rejection reason is required"
