"""
tiap abis kasih kelas, kasih spasi 2
"""
from bottle import run, route
from config.constants import SERVER, RANGE

class first_class:
    """class var bisa ketik disini
     ex: Jumlah = 0"""

    def __init__(self, inputit, numnum):
        """define dulu kalo mau lebih dr 1"""
        self.place = inputit
        self.number = numnum

    def dimana(self):
        """void function, method tnpa return"""
        print("aku dari " + self.place)

    def nambah_no(self, up):
        """method dengan argumen"""
        self.number += up

    def getplace(self):
        """method dengan return"""
        kalimat = 'dari :' + self.place
        return kalimat



class try_class:
    """coba init"""
    def __init__(self, num):
        print('hello', num)


class heroTry:
    """
    hero class
    """
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def fight(self):
        """
        bneran harus ketik semua
        """
        self.health -= 10


def main():
    """
    fungsi main
    """
    hero1 = heroTry('sniper', 100) #object/instance
    # hero2 = hero_try('manz', 200)
    # hero3 = hero_try('sven', 300)


    hero1.fight()

    print(hero1.health)
    # hero1.name = 'sniper'
    # hero1.health = 100

    # hero2.name = 'manz'
    # hero2.health = 200

    # hero3.name = 'sven'
    # hero3.health = 300

    print("\n", RANGE*"=", "\n")
    print(hero1.name)

    print("\n", RANGE*"=", "\n")

    hero4 = try_class(10) #hero4 setara dengan self
    print(hero4)

    hero5 = first_class('jakarta', 5)
    print(hero5.place)
    print(hero5.number)
    hero5.dimana()
    hero5.nambah_no(5)

    print(hero5.number)
    print(hero5.getplace())
    print(SERVER)
if __name__ == '__main__':
    run(host="127.0.0.1", port=18080)
    main()

    print(__name__)