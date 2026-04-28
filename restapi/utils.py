"""
Shared utilities for consistent API responses across all apps.
"""

from rest_framework.response import Response
from rest_framework import status as http_status


def success_response(data=None, message="", status=http_status.HTTP_200_OK):
    """Return a standard success envelope."""
    return Response(
        {
            "status": "success",
            "data": data,
            "message": message,
        },
        status=status,
    )


def error_response(
    message="Something went wrong.",
    errors=None,
    status=http_status.HTTP_400_BAD_REQUEST,
):
    """Return a standard error envelope."""
    return Response(
        {
            "status": "error",
            "data": errors,
            "message": message,
        },
        status=status,
    )
