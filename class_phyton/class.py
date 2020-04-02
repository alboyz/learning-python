# class


class Mahasiswa():
    def __init__(self, input_nama):
        self.nama = input_nama

    def belajar(self, kondisi):
        print(self.nama, 'sedang belajar', kondisi)


# main programnya


name = Mahasiswa("Ali")


print(name.nama)
name.belajar("python3")
name.nama = "sueb"
print(name.nama)

