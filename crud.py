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

        phrase = 'name :', self.name, ' address :', self.address
        print(phrase)
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

class Delete:
    """ delete member """

    def __init__(self, name):
        """ member name delete """

        self.name = name

    def showdata(self):
        """ print before delete """

        phrase = 'name :', self.name
        print(phrase)
        self.delindb()

    def delindb(self):
        """ delete member in db """

        before = {"name": self.name}
        before = json.dumps(before)
        beforein = json.loads(before)
        print(before)
        print(beforein)
        now = { "$set": { "is_deleted": "true" } }
        MYCOL.update_one(beforein,now)
        print('record deleted')



def main():
    """
    fill here
    """
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

    

if __name__ == '__main__':
    main()
