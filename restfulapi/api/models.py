from django.db import models

# Create your models here.

class Word(models.Model):
    name = models.CharField(blank=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Word"
        verbose_name_plural = "Words"

    def __str__(self):
        return self.name

