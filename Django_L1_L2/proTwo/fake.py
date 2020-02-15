from faker import Faker
import random
def fData():

    fk = Faker()
    id = ["@gmail.com","@yahoo.com","@hotmail.com","@outlook.com"]
    num = random.randint(1,100)
    mail = random.choice (id)
    uname = fk.name().split()
    final = (uname[0].lower()+str(num)+mail)
    list = [final,uname[0],uname[1]]
    return list
