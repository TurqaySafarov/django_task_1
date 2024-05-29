from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Movie(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Müəllif")
    title = models.CharField(max_length=200, verbose_name="Başlıq")
    director = models.CharField(max_length=200, verbose_name="Rejissor")
    description = models.TextField(verbose_name="Təsvir")
    release_date = models.DateField(verbose_name="Çıxış Tarixi")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma Tarixi")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə Tarixi")
    
    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmlər"
        ordering = ['-created_date']
    
    def __str__(self):
        return f"{self.title} by {self.director}"

    def get_summary(self):
        return self.description[:100]  # Returns the first 100 characters of the description

    def was_released_recently(self):
        from datetime import date
        return self.release_date >= date.today()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('movie_detail', kwargs={'pk': self.pk})
