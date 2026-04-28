"""Serializers for the students app."""

from rest_framework import serializers
from .models import Student


class StudentListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for list endpoints (mobile-friendly)."""

    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "courses",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        # Only nest objects for JSON responses, so the HTML form doesn't break
        if request and getattr(request.accepted_renderer, 'format', '') != 'html':
            from courses.serializers import CourseListSerializer
            representation['courses'] = CourseListSerializer(instance.courses.all(), many=True).data
        return representation


class StudentDetailSerializer(serializers.ModelSerializer):
    """Full serializer for detail/create/update endpoints."""

    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "courses",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        # Only nest objects for JSON responses, so the HTML form doesn't break
        if request and getattr(request.accepted_renderer, 'format', '') != 'html':
            from courses.serializers import CourseListSerializer
            representation['courses'] = CourseListSerializer(instance.courses.all(), many=True).data
        return representation
