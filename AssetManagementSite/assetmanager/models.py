from django.db import models

# Create your models here.
class Asset(models.Model):
    asset_tag = models.IntegerField()
    display_name = models.CharField(max_length = 50)
    serial_number = models.CharField(max_length = 15)
    purchase_date = models.DateField()
    purchase_cost = models.DecimalField(max_digits = 10, decimal_places = 2)
    assigned_to = models.CharField(max_length = 50, blank=True)    # blank=True allows for empty assigned_to
    warranty_expiration = models.DateField()
    notes = models.TextField(blank=True)    # blank=True allows for empty notes
    
    def __str__(self):
        return self.display_name