from django.db import models

class DailyMenu(models.Model):
    type = models.CharField(
        max_length=20,
        choices=[('student', 'Student'), ('teacher', 'Teacher')],
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_path = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name