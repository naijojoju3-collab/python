from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(choices=[(i, f"{i}%") for i in range(0, 101, 10)])

    def __str__(self):
        return self.name
