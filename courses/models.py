"""
Course models for EduTracker platform.

Courses hold academic content info.
"""

from django.db import models


class Course(models.Model):
    """Represents an academic course on the platform."""

    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.code} – {self.title}"


