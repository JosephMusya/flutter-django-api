from django.db import models

# Create your models here.
class Book(models.Model):
    cover_image = models.ImageField(upload_to = 'books',null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    quantity = models.IntegerField()
    stock = (
        ('In Stock','In Stock'),
        ('Out of Stock','Out of Stock')
    )
    status = models.CharField(choices=stock, default='In Stock',max_length=50) 
    
    def __str__(self):
        return str(self.title)