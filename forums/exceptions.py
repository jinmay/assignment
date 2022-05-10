from rest_framework.exceptions import APIException


class PermissionDenied(APIException):
    status_code = 403
    default_detail = 'You don\'t have permission for this.'
