class Hero:
    """
    nyoba private var
    """
    __jumlah = 10 #class variable, yg emang ketutup kan

    def __init__(self, name, health):
        self.__name = name
        self.__health = health
        Hero.__jumlah += 2
        self.__private = "private" #ini private, gabisa akses sembarang
        self._protected = "protected" #masih agak bingung tp katanya konvensi

    def get_name(self):
        """
        getter
        """
        return self.__name

    def get_health(self):
        """
        getter jugak, btw method yang dalamnya ada tulisan self ini hanya berlaku untuk object
        """
        return self.__health

    def attacked(self, attack):
        """
        setter
        """
        self.__health -= attack

    def get_jumlah():
        """
        method tanpa tulisan self, ga bisa buat object tp bisa untuk kelas
        """
        return Hero.__jumlah

    @staticmethod
    def get_jumlah2():
        """
        dengan static method, bisa 2 2nya
        """
        return Hero.__jumlah

    @classmethod
    def get_jumlah3(cls):
        """
        dia bisa ubah kata self diatas incase class Hero diganti namanya
        """
        return cls.__jumlah


lina = Hero("lina", 100)

print(lina.__dict__)
#print(lina.__private) #munculnya jadi has no attribute
print(lina._protected)
lina.protected = "change"
print(lina._protected)

#liat nama ajah pake getter
print(lina.get_name())

#setter kekuatan yg berkurang
print(lina.get_health())
lina.attacked(5)
print(lina.get_health())
print(Hero.get_jumlah2())

print(lina.get_jumlah2())
print(Hero.get_jumlah2())

print(__file__)
print(__name__)
print(lina.__info)