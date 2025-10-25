import re
from datetime import datetime,date

product_list=[]

def name_validator(name):
    if not re.match(r"^[A-Za-z\s]{3,30}$", name):
       raise ValueError("Invalid name!!!!")


def brand_validator(brand):
    if not re.match(r"^[A-Za-z\s]{3,30}$", brand):
        raise ValueError("Invalid brand!!!!")

def quantity_validator(quantity):
    if not(type(quantity) == int and 0 < quantity):
        raise ValueError("Invalid quantity!!!!")

def price_validator(price):
    if not(type(price) == int and 0 < price):
        raise ValueError("Invalid price!!!!")

def expire_date_validator(expire_date):
    try:
        return datetime.strptime(expire_date, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Invalid date!!!!")