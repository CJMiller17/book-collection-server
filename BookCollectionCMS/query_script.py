import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "BookCollectionCMS.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW

from BookManager.models import *

# book_list = Book.objects.bulk_create([
#           Book(user= "codymiller", title="To Kill a Mockingbird", author= "Harper Lee", genre= "Fiction", favorite= True, rating= 5,),
#           Book(user="codymiller", title= "1984", author= "George Orwell", genre= "SciFi", favorite= True, rating= 5,),
#           Book(user="codymiller", title= "Pride and Prejudice", author= "Jane Austen", genre= "Romance", favorite= False, rating= 3,),
#           Book(user="codymiller", title= "The Great Gatsby", author= "F. Scott Fitzgerald", genre= "Boring", favorite= False, rating= 1,),
#           Book(user="codymiller", title= "The Little Developer That Couldn't Even...", author= "Hell Itself", genre= "Non-Fiction", favorite= False, rating= 2,),
#           Book(user="codymiller", title= "How to Authenticate Users and Cry", author= "Me, Its Me", genre= "Psychological Thriller", favorite= True, rating= 4,),
#           Book(user="codymiller", title= "Scream Therapy", author= "Cody Miller", genre= "Self Help", favorite= True, rating= 4,),
#           Book(user="codymiller", title= "The Grapes of Wrath", author= "John Steinbeck", genre= "Fiction", favorite= False, rating= 3,),         
# ])

# user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
#     title = models.TextField()
#     author = models.TextField()
#     genre = models.TextField()      # Come back and limit the Genre's
#     favorite = models.BooleanField()
#     rating = models.TextField()