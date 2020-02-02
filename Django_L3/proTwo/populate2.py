import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proTwo.settings')

import django
# Import settings
django.setup()

import random
from appTwo.models import User
from faker import Faker
from fake import fData

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''
    for entry in range(N):
        # Create Fake Data for entry
        newlist = fData()
        # Create new User Entry
        data = User.objects.get_or_create(fName=newlist[1],lName=newlist[2],email=newlist[0])[0]

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(30)
    print('Populating Complete')
