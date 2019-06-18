from django.db import models

# Create your models here.



class Genre(models.Model):
    " " " Model represenitng a book genre. " " "
    name = models.CharField(max_length=200, help_text='Enter a book genere (e.g. Science Fiction)')

    def __str__(self):
        " " " String for representing the Model object. " " "
        return self.name 

