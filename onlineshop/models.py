from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    
    


class Products(models.Model):
    
    name = models.CharField(max_length=150)
    fk_categories = models.ForeignKey(Categories, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}-{self.fk_categories}'
    
    