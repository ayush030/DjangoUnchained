from django.db import models

# Create your models here.

from django.db import models
from django.core.validators import MinLengthValidator

class Breed(models.Model):
      name= models.CharField(max_length=200,
      			     validators=[MinLengthValidator(2,"Enter more than 1 character")]
      			     )
      
      def __str__(self):
          return self.name
          

class Cat(models.Model):
      nickname = models.CharField(max_length=200,
      				   validators=[MinLengthValidator(2, "Enter more than 1 character")]
      				   )
      
      weight = models.PositiveIntegerField()
      foods= models.CharField(max_length=300)
      breed= models.ForeignKey("Breed", on_delete=models.CASCADE, null= False)
      
      
      def __str__(self):
          return self.nickname 
