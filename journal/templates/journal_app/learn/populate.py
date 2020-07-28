import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learn.settings')

import django
# Import settings
django.setup()

from learn_app.models import Kid,Student
from faker import Faker
import random

fakegen = Faker()


def populate(N=5):
    '''
    Create N Entries
    '''
    c=1
    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.name()
        fake_dob = fakegen.date()

        # Create new Kid Entry
        kid = Kid.objects.get_or_create(name=fake_name,
                                        dob=fake_dob)[0]

        # Create Fake Data for entry

        fake_marks = random.randint(0,100)

        # Create new Student Entry

        stud = Student.objects.get_or_create(marks=fake_marks,
                                             roll_no=Kid(id=c))[0]
        c=c+1



if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
