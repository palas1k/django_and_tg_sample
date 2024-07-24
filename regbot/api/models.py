from django.db import models
from django.utils import timezone


class SupportSoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True


class ReservedTime(SupportSoftDeleteModel):
    date_time = models.DateTimeField(default=None)
    user = models.ForeignKey("User", on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return str(self.date_time)
