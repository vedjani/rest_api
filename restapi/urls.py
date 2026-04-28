"""
URL configuration for restapi project – EduTracker API.

API endpoints:
    /                       — API root (endpoint directory)
    /api/students/          — Student CRUD
    /api/courses/           — Course CRUD

"""


from django.urls import path, include
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response



@api_view(["GET"])
@permission_classes([AllowAny])
def api_root(request):
    """Root endpoint — shows all available API routes."""
    return Response({
        "status": "success",
        "message": "Welcome to EduTracker API 🎓",
        "data": {
            "endpoints": {
                "students":     request.build_absolute_uri("/api/students/"),
                "courses":      request.build_absolute_uri("/api/courses/"),

            }
        },
    })


urlpatterns = [
    # Root
    path("", api_root, name="api-root"),





    # App endpoints
    path("api/students/", include("students.urls")),
    path("api/", include("courses.urls")),
]
