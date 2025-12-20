from django.db import models
CATEGORY_CHOICES = [
    ('makeup', 'Makeup'),
    ('skincare', 'Skincare'),
    ('fragrance', 'Fragrance'),
    ('haircare', 'Haircare'),
    ('sunscreen', 'Sunscreen'),
    ('other', 'Other'),
]

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


