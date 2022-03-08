from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Make(models.Model):
      name = models.CharField(max_length=200, 
      			      validators=[MinLengthValidator(2, "Name must be greater than 1 character")],
      			      help_text="Enter a Make ex: Dodge"
      			      )
      
      def __str__(self):
          '''String to represent the model'''
          return self.name
          
          
          
class Autos(models.Model):
      nickname = models.CharField(max_length=200,
      				   validators=[MinLengthValidator(2, "Enter more than 1 character")]
      				  )
      mileage = models.PositiveIntegerField()
      comments = models.CharField(max_length=300)
      make = models.ForeignKey("Make", on_delete=models.CASCADE, null=False)	
      
      
      def __str__(self):
          return self.nickname
      
      
#models are registered in admin list

