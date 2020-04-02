# class


class Mahasiswa():
    __nilai = 0

    def __init__(self, input_nama):
        self.nama = input_nama

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def checkStatus(self):
        if self.__nilai < 200:
            print(self.nama, "Tidak Lulus")
        else:
            print(self.nama, "Lulus")

# main programnya


name = Mahasiswa("Ali")


print(name.nama)
name.uts(100)
name.uas(100)
name.checkStatus()
name.nama = "sueb"
print(name.nama)
