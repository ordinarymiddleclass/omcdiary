from datetime import datetime
from dateutil import relativedelta

def from_my_birthday (d):
    """
        Calculate time difference between given datetime d and 1986-4-23.
    """
    birthday = datetime(1986, 4, 23)
    return relativedelta.relativedelta(d, birthday)

def from_epoch (d):
    return (d - datetime(1970,1,1)).days

def from_gp (d):
    return (d - datetime(2019,9,28)).days

today = datetime.now()
age = from_my_birthday (today)

years = age.years
months = age.months
days = age.days

print('{} years {} months {} days'.format(years, months, days))
print(from_epoch(today))
print(from_gp(today))