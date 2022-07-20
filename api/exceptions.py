from rest_framework import status
from rest_framework.exceptions import APIException


class NotExistException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'requested data not found'


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ''


class ServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'internal server error'


class PaymentError(APIException):
    status_code =  status.HTTP_402_PAYMENT_REQUIRED
    default_detail = 'problem with payment'
