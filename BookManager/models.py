from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile") # Related name is the backwards compatible name
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.user.username
    
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.TextField()
    author = models.TextField()
    genre = models.TextField()      # Come back and limit the Genre's
    favorite = models.BooleanField()
    rating = models.TextField()     # Come back and limit the ratings to 1 -5

# class Review(models.Model):
#     heading = models.TextField()
#     content = models.TextField()
#     reviewer = models.ForeignKey() 


# Create your models here.


#  First Time Around:
# "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzEwMzQxNSwiaWF0IjoxNzE3MDE3MDE1LCJqdGkiOiJhZTNiMzU3ZjRhNDI0ZjM5OTNhZGJiNjQ3NjU5YTdkNyIsInVzZXJfaWQiOjF9.SdxJvilcxMZxVC-tRYTSX6NCYYkQ7Et0Aymw7966NdQ",
# "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3MDE3MzE1LCJpYXQiOjE3MTcwMTcwMTUsImp0aSI6IjZkMDgxY2M2N2ZjODQwYzY4ZmQ0MjViZmMwZDMxMjYyIiwidXNlcl9pZCI6MX0.pBAa28P0GrcsYYgn_aI2LTZxTkDXK-OQke3S1ft9iMw"


# Second Time Around:
# "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3MDE3NTA1LCJpYXQiOjE3MTcwMTcwMTUsImp0aSI6IjJhYmVhOGU5OGMwMTQyOWViYTgzMGY2ZGQ0NDkyMTEwIiwidXNlcl9pZCI6MX0.mcYR8mfOr_16m__eNVm4iWLvczGQMjxfku0LDmd42Uo",
# "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzEwMzYwNSwiaWF0IjoxNzE3MDE3MjA1LCJqdGkiOiJjNzEzOTBiZDczMTY0MGI2OWNjMDkyZjk0OGUyZWI0YyIsInVzZXJfaWQiOjF9.IcWMCNTzP48GsKQmwKD0X_Vstg6ccqXh6lXivUb4dy8"