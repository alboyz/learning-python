class Person:
    def __init__(self, nama="no name", umur=0):
        self.__nama = nama
        self.__umur = umur

    def getNama(self):
        return self.__nama

    def getUmur(self):
        return self.__umur

    def perkenalanDiri(self):
        return "saya adalah :" + self.__nama + "\n berumur :"+str(self.__umur) + "tahun"


# inharitence/pewarisan
class Student (Person):
    def __init__(self, nama='no name', umur=0, id="S0000"):
        super().__init__(nama=nama, umur=umur)
        self.__id = id
    
    #overiding yaitu tindakan menimpa method
    def perkenalanDiri(self):
        return super().perkenalanDiri()+"\n saya memiliki id"+self.__id


def main():
    s = Student("Adi", 12)
    print(s.perkenalanDiri())


main()
