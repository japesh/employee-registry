# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

class RequestCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TimeOffRequest(models.Model):
    employee = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    request_category = models.ForeignKey(RequestCategory, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.request_category.name not in ['Work Remotely', 'Annual Leave']:
            overlapping_requests = TimeOffRequest.objects.filter(
                employee=self.employee,
                start_date__lte=self.end_date,
                end_date__gte=self.start_date
            ).exclude(request_category__name__in=['Work Remotely', 'Annual Leave'])

            if overlapping_requests.exists():
                raise ValidationError('Overlapping time off requests are not allowed.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.username} - {self.request_category.name} ({self.start_date} to {self.end_date})"
