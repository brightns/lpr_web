from django.db import models
from django.utils.timezone import now
# Create your models here.
class Record(models.Model):
    create_date_time = models.DateTimeField(blank=False, default=now)
    update_date_time = models.DateTimeField(auto_now=True, blank=False)
    json = models.JSONField(null=True)
    is_processed = models.BooleanField(default=False)

