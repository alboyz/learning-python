class Person:
    def __init__(self, nama="no name", umur=0):
        self.__nama = nama
        self.__umur = umur

    def getNama(self):
        return self.__nama

    def getUmur(self):
        return self.__umur

    def perkenalanDiri(self):
        return "saya adalah :" + self.__nama +"\n berumur :"+str(self.__umur) + "tahun"
    
    # method overloading

    def __add__(self, other):
        n = Person(self.getNama() + other.getNama(),self.getUmur() + other.getUmur())
        return n

#overloading adalah gabungan
def main():
    p=Person("Dodi",  12)
    g=Person ("adi", 12)
    h =p +g
    print(h.perkenalanDiri())
main()
