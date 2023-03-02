from django.db import models
from django.urls import reverse


##Rule for vehicular number:-
#The first two letters are the state/union territory code followed by the RTO (district) code.
# The following six characters (two alphabets and four numbers) are your vehicle's unique code.
#ex,KA01AB1234

class Vehicle(models.Model):
    VEHICLE_TYPE = [
        ('two wheeler', 'Two Wheeler'),
        ('three wheeler', 'Three Wheeler'),
        ('four wheeler', 'Four Wheeler'),
        # Three allowed vehicular types
    ]
    Vehicle_Number = models.CharField(max_length=10)
    Vehicle_Type = models.CharField(max_length=20, choices=VEHICLE_TYPE)
    Vehicle_Model = models.CharField(max_length=50)
    Vehicle_Description = models.TextField()

    def __str__(self):
        return f'self.Vehicle_Number,self.Vehicle_Type,self.Vehicle_Model,self.Vehicle_Description'

    def get_absolute_url(self):
        return reverse("vehicle_detail",kwargs={"pk":self.pk})



