from django.db import models

# Create your models here.
class Scrot(models.Model):
    domain = models.CharField(max_length=80, blank=False)
    scrot_file = models.ImageField(blank=False)
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.domain, self.date_taken.strftime('%H'))