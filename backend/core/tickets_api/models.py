from django.db import models

# Create your models here.

Class Tickets(model.Models)
    Title = models.CharField (max_length=30)
    Description = models.TextField ()
    Date_of_log =models.DateTimeField (auto_now = True)


    def__str__(self)
      return self.Title
