from django.db import models

# Create your models here.
class bookss(models.Model):
    book_id=models.CharField(max_length=10);
    book_name=models.CharField(max_length=35);
    photo=models.ImageField(upload_to='images');
    def __str__(self):
        return self.book_name

