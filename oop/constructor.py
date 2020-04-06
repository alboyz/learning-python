class Person:
    __umur = 23  # disebut enkapulasi karena tidak bisa di rubah nilainya
    # cara merubahnya dengan setter dan getter

    def __init__(self, name, umur):  # def__init__ adalah constructor
        self.__name = name
        self.__setUmur(umur)

    def getName(self):
        return self.__name

    def getUmur(self):
        return self.__umur

    def __setUmur(self, umur):
        self.__umur = umur if umur > 0 else 0


def main():
    p = Person("adi", -43)
    print(p.getName())
    print(p.getUmur())


main()
