from django.db import models
import string
import random


# Create your models here.

#create Room model

#generate unique code for each room

def generate_unique_code(): #create a function called generate_unique_code
    length = 6 #create a variable called length, with a value of 6
    while True: #create a while loop
        code = ''.join(random.choices(string.ascii_uppercase, k=length)) #create a variable called code, with a value of a random string of 6 characters
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

class Room(models.Model): #inherit from models.Model
    code = models.CharField(max_length=8, default="", unique=True) #create a field called code, with a max length of 8 characters, default value of empty string, and unique
    host = models.CharField(max_length=50, unique=True) #create a field called host, with a max length of 50 characters, and unique
    guest_can_pause = models.BooleanField(null=False, default=False) #create a field called guest_can_pause, with a default value of False
    votes_to_skip = models.IntegerField(null=False, default=1) #create a field called votes_to_skip, with a default value of 1
    created_at = models.DateTimeField(auto_now_add=True) #create a field called created_at, with a default value of the current time

    # def is_host_this(host): #create a function called is_host_this, with a parameter called host
    #     return host == self.host