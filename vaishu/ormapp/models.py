from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # e.g., 8.5
    description = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"{self.title} ({self.release_date.year})"
