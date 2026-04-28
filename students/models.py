"""
Student model for EduTracker platform.

Stores student profile data and links to enrolled courses.
"""

from django.db import models


class Student(models.Model):
    """Represents a student on the EduTracker platform."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    courses = models.ManyToManyField(
        "courses.Course",
        related_name="students",
        blank=True
    )

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


