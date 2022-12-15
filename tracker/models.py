from django.db import models
from django.contrib.auth.models import User


###########################################################################


class Industry(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


###########################################################################


class Interview(models.Model):
    company_name = models.CharField(max_length=200)

    industry = models.ForeignKey(
        Industry,
        related_name="interview",
        on_delete=models.CASCADE,
        null=True,
    )

    position = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    responded = models.BooleanField(default=False)
    notes = models.TextField()
    job_link = models.URLField(null=True)

    user = models.ForeignKey(
        User,
        related_name="interview",
        on_delete=models.CASCADE,
        null=True,
    )
