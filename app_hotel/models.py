from django.db import models

# Create your models here.
class RoomCategory(models.Model):
    name = models.CharField(max_length=255)
    base_price = models.FloatField()

    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.IntegerField(unique=True)
    category = models.ForeignKey(RoomCategory,on_delete=models.CASCADE,null=True,blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.room_number)

class Reservation(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True,blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    customer_name = models.CharField(max_length=255)
    total_price = models.FloatField()

    def __str__(self):
        return self.customer_name

class SpecialRate(models.Model):
    room_category = models.ForeignKey(RoomCategory,on_delete=models.CASCADE,null=True,blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    rate_multiplier = models.FloatField()

    def __str__(self):
        return str(self.rate_multiplier)