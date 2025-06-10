from django.db import models

class Reservation(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    menu = models.ForeignKey('menus.DailyMenu', on_delete=models.CASCADE)  # Changed from DailyMenu to Menu
    category = models.CharField(
        max_length=20,
        choices=[('student', 'Student'), ('teacher', 'Teacher')],
    )
    tickets_or_plates = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('completed', 'Completed')],
        default='pending',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.menu.name}"