from django.db import models
from django.utils import timezone
import os

def menu_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/menu_images/<type>/<filename>
    return f'menu_images/{instance.type}/{filename}'

class DailyMenu(models.Model):
    type = models.CharField(
        max_length=20,
        choices=[('student', 'Student'), ('teacher', 'Teacher')],
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=menu_image_path, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
    def delete(self, *args, **kwargs):
        # Delete the image file when the menu item is deleted
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


class TicketOrder(models.Model):
    PAYMENT_METHODS = [
        ('656910038', '656910038'),
        ('678789520', '678789520'),
    ]
    
    name = models.CharField(max_length=255)
    ticket_quantity = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    order_date = models.DateTimeField(default=timezone.now)
    is_confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name}'s order for {self.ticket_quantity} tickets"
    
    class Meta:
        ordering = ['-order_date']