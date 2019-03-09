import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
# Import settings
django.setup()

from second_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        # Create new Webpage Entry

        user_dict = User.objects.get_or_create(user_first_name = fake_first_name,
                                                user_last_name = fake_last_name,
                                                user_email = fake_email)[0]
# Could add more of these if you wanted...

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
