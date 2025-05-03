import uuid
from django.db import models

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
