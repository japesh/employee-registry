
# Create your models here.
from django.db import models
from uuid import uuid4
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
import re

class Employee(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    salary = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(default=timezone.now)

    def clean(self):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, self.email):
            raise ValidationError("Invalid email format")

    def save(self, *args, **kwargs):
        self.full_clean()
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.position})"
