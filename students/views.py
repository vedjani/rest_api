"""ViewSets for the students app."""

from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend

from .models import Student
from .serializers import StudentListSerializer, StudentDetailSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    CRUD ViewSet for Students.

    list:   GET    /api/students/
    create: POST   /api/students/
    read:   GET    /api/students/{id}/
    update: PUT    /api/students/{id}/
    delete: DELETE /api/students/{id}/

    Query params:
      ?search=john          — search by first_name, last_name, email
      ?courses=3            — filter students enrolled in course id 3
    """

    http_method_names = ["get", "post", "put", "delete", "head", "options"]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["courses"]
    search_fields = ["first_name", "last_name", "email"]
    ordering_fields = ["first_name", "last_name"]
    ordering = ["first_name", "last_name"]

    def get_queryset(self):
        return Student.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return StudentListSerializer
        return StudentDetailSerializer


