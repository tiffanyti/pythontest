""" crud test """
import json
from database import MYCOL

class Add:
    """ adding member """
    data = 0

    def __init__(self, name, address):
        """ member name and address """

        Add.data += 1
        self.name = name
        self.address = address

    def showdata(self):
        """ print before add """

        print('name :', self.name, ' address :', self.address)
        print(Add.data)
        self.addtodb()

    def addtodb(self):
        """ adding member to db """

        data = {"name": self.name, "address": self.address, "is_deleted" : "false"}
        data = json.dumps(data)
        datain = json.loads(data)
        print(datain)
        MYCOL.insert_one(datain)
        print('record added')

class Edit:
    """ Edit Collections """

    def __init__(self, name, key, prev_value, new_value):
        """ member name change """
        self.name = name
        self.key = key
        self.prev_value = prev_value
        self.new_value = new_value

    def showdata(self):
        """ print before change """

        print('name :', self.name, '\n', 'change ', self.key, ':', self.prev_value, ' ->', self.new_value)

    def changedata(self):
        """ change member in db """

        before = {self.key : self.prev_value}
        before = json.dumps(before)
        beforein = json.loads(before)

        now = {"$set": {self.key : self.new_value}}
        now = json.dumps(now)
        nowin = json.loads(now)

        MYCOL.update_one(beforein, nowin)
        print('record updated')

class Delete:
    """ delete member """

    def __init__(self, name):
        """ member name delete """

        self.name = name

    def showdata(self):
        """ print before delete """

        print('name :', self.name)
        self.delindb()

    def delindb(self):
        """ delete member in db """

        before = {"name": self.name}
        before = json.dumps(before)
        beforein = json.loads(before)
        print(before)
        print(beforein)
        now = {"$set": {"is_deleted": "true"}}
        MYCOL.update_one(beforein, now)
        print('record deleted')

def addordell():
    """add or delete options function"""
    addordel = str(input('Question : add or delete? (a/d)'))

    if addordel == 'a':
        print("add yaa")
        addname = str(input('name : '))
        addaddress = str(input('address : '))
        test = Add(addname, addaddress)
        test.showdata()

    elif addordel == 'd':
        print("delete yaa, ketik 1 nama")
        delname = str(input('name :'))
        test = Delete(delname)
        test.showdata()
    else:
        print('apa?')

def edit():
    """change data function"""

    print('Please write data you want to change')
    name = str(input('name : '))
    key = str(input('data you want to change (name/address)'))
    prev = str(input('previous data :'))
    new = str(input('new data :'))

    editrecord = Edit(name, key, prev, new)
    editrecord.showdata()

    question = (str(input('change? (y/n)')))
    if question == 'y':
        editrecord.changedata()
    else:
        print('edit cancelled')


def view():
    """ View database costumer (mycol) """

    print("here is the list of our 'costumer' in mydatabase :")
    collections = MYCOL.find()
    for record in collections:
        print(record)


def main():
    """ fill here """

    view()
    print("\n", 22*"=", "\n")

    i = 0
    while i < 5:
        adddelq = str(input('Question : want to delete/add? (y/n)'))
        if adddelq == "y":
            addordell()
        elif adddelq == 'n':
            print('okay')
            break
        else:
            print('so....')

    print("\n", 22*"=", "\n")

    while i < 5:
        editrecord = str(input('Question : want to change record? (y/n)'))
        if editrecord == 'y':
            edit()
        elif editrecord == 'n':
            print('okay')
            break
        else:
            print('so....')

    print("\n", 22*"=", "\n")

    print('thank you')

if __name__ == '__main__':
    main()
