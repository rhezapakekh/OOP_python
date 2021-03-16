# OOP BASIC DENGAN CONSTRUCTOR
# class OOP:
#     # class variable
#     total = 0
#     # contructor
#     def __init__(self,inputNama,inputAlamat,inputGender):
#         # instance variable
#         self.nama = inputNama
#         self.alamat = inputAlamat
#         self.gender = inputGender
#         OOP.total += 1
#         print ("membuat objek dengan nama :",inputNama)

#     def getName(self):
#         return self.nama


# belajar_oop = OOP('belajar python','sby','L')
# print (belajar_oop.getName())




# INTERAKSI ANTAR OBJECT DENGAN IMPLEMENTASI GAME SEDERHANA
# class Hero:

#     def __init__(self, name, attack, health, defense):
#         self.name = name
#         self.attack = attack
#         self.health = health
#         self.defense = defense

#     def menyerang(self, lawan):
#         print(self.name + ' menyerang ' + lawan.name + ' dengan damage ' + str(self.attack))
#         lawan.diserang(self)

#     def diserang(self, lawan):
#         damage = lawan.attack/self.defense
#         self.health -=damage
#         print('damage yang masuk :' + str(damage))
#         print('sisa health '+ self.name +str(self.health))

# grock = Hero('grock',10,1000,100)
# clint = Hero('clint',100,300,50)

# clint.menyerang(grock)
# print('\n')
# grock.menyerang(clint)




# CLASS PRIVATE DAN PROTECTED
# class Data:

#     def __init__(self,nama):
#         self.nama = nama

#         # variable private
#         self.__nik = 3111

#         # variable protected
#         self._ttl = 'surabaya'

# data = Data('bayu')
# print (data.__dict__)




# ENKAPSULASI
# class Hero:

#     def __init__(self,attack,health):
#         self.__attack = attack
#         self.__health = health

#     # getter
#     def getAttack(self):
#         return self.__attack

#     def getHealth(self):
#         return self.__health

#     # setter
#     def diserang(self,attack_lawan):
#         self.__health -= attack_lawan

# minotour = Hero(10,500)
# print (minotour.getHealth())
# minotour.diserang(100)
# print (minotour.getHealth())

# # STATIC DAN CLASS METHOD
# class Data:

#     __listNama = []
#     __listNpm = []
    
#     def __init__(self,nama,npm):
#         self.__nama = nama
#         self.__npm = npm
#         Data.__listNama.append(nama)
#         Data.__listNpm.append(npm)



#     # method yang menempel pada class dan object
#     @staticmethod
#     def getJumlah():
#         jumlah = len(Data.__listNama)
#         return jumlah
#     # method yang menempel pada class saja

#     @classmethod
#     def cetakData(cls):
#         print(cls.__listNama[0:])
#         print(cls.__listNpm[0:])    
    
# data = Data('panji',3333)
# data = Data('mimi',1111)
# data.cetakData()
# print(Data.getJumlah())

# MERUBAH METHOD MENJADI VARIABLE DENGAN PROPERTY
# class Mahasiswa:
#     def __init__(self, nama, npm):
#         self.__nama = nama
#         self.__npm = npm
    
#     @property
#     def info(self):
#         return "nama : {} \nnpm : {}".format(self.__nama, self.__npm)

#     @property
#     def getNama(self):
#         return self.__nama

#     @property
#     def getNpm(self):
#         return self.__npm
    
#     @property
#     def deletNpm(self):
#         self.__npm = None
#         print('npm sudah dihapus')

# mhs = Mahasiswa('abah',888)
# print(mhs.info)


class Hero:
    def __init__(self,nama, attack, health, armor):
        self.__nama = nama
        self.__attackAwal = attack
        self.__healthAwal = health
        self.__armorAwal = armor
        self.__exp = 0
        self.__level = 1

        self.__healthMax = self.__healthAwal * self.__level
        self.__attack = self.__attackAwal * self.__level
        self.__armor = self.__armorAwal * self.__level

        self.__health= self.__healthAwal

    @property
    def info(self):
        return '{} level : {} \n\t health : {}/{} \n\t attack : {} \n\t armor : {}'.format(self.__nama, self.__level, self.__health, self.__healthMax, self.__attack, self.__attack)

    
    def gainExp(self, addExp):
        self.__exp +=addExp
        if (self.__exp >= 100):
            print('{} level up'.format(self.__nama))
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthAwal * self.__level
            self.__attack = self.__attackAwal * self.__level
            self.__armor = self.__armorAwal * self.__level
    
    def attackLawan(self,lawan):
        self.gainExp(50)

moskov = Hero('moskov', 100, 10, 1)
fanny = Hero('fanny', 100, 10, 1)

moskov.attackLawan(fanny)
moskov.attackLawan(fanny)
print(moskov.info)
