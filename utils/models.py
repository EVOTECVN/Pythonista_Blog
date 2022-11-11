from django.db import models
from datetime import datetime


class BaseModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)


class BaseModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BaseModelManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = datetime.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        ordering = ('-created',)
        abstract = True
