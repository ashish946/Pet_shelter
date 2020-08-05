from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
import datetime

ANIMAL_CHOICES=(
    ('Cat','CAT'),
    ('Dog','DOG'),
)
AGE_CHOICES=(
    ('Young','YOUNG'),
    ('Old','OLD'),
)

GENDER_CHOICES=(
    ('Female','FEMALE'),
    ('Male','MALE'),
)

class Animal(models.Model):
    name=models.CharField(max_length=32)
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField(max_length=360,null=True)
    difficulty=models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)],default=0)
    animal=models.CharField(choices=ANIMAL_CHOICES,max_length=3,null=True)
    age=models.CharField(choices=AGE_CHOICES,max_length=5,null=True)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=6,null=True)
    Sheltered=models.DateTimeField()


    def __str__(self):
        return self.name
