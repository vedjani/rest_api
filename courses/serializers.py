"""Serializers for the courses app."""

from rest_framework import serializers
from .models import Course


# ── Course Serializers ────────────────────────────────────────────

class CourseListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for list endpoints."""

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "code",
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    """Full serializer for detail/create/update endpoints."""

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "code",
        ]
