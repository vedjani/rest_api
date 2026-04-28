"""ViewSets for the courses app."""

from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend

from .models import Course
from .serializers import CourseListSerializer, CourseDetailSerializer


# ── Course ViewSet ────────────────────────────────────────────────

class CourseViewSet(viewsets.ModelViewSet):
    """
    CRUD ViewSet for Courses.

    list:   GET    /api/courses/
    create: POST   /api/courses/
    read:   GET    /api/courses/{id}/
    update: PUT    /api/courses/{id}/
    delete: DELETE /api/courses/{id}/

    Query params:
      ?search=python        — search by title, code
    """

    http_method_names = ["get", "post", "put", "delete", "head", "options"]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = []
    search_fields = ["title", "code"]
    ordering_fields = ["title", "code"]
    ordering = ["title"]

    def get_queryset(self):
        return Course.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CourseListSerializer
        return CourseDetailSerializer





