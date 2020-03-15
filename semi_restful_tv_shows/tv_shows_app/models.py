from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=250)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __repr__(self):
        return f"Show ID: ({self.id}) | Title: {self.title} | Network: {self.network} | Release Date: {self.release_date} | Description: {self.description} ||"