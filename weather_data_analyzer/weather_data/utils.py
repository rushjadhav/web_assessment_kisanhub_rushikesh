import random
import string
import datetime

def get_random_string(length=6):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

def get_date_from_year_month(month, year):
    return datetime.datetime.strptime("{0}/{1}".format(month, year), "%m/%Y")