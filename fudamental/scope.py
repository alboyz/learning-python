
namaMahasiswa = 'Taufiq'
nimMahasiswa = 11621005

# scope local


def changeName(newName):
    namaMahasiswa = newName
    print('Nama yang baru adalah', namaMahasiswa)

# global


def changeNim(newNim):
    global nimMahasiswa
    nimMahasiswa = newNim
    print("nim yang baru adalah", nimMahasiswa)


changeName('Ali')
changeNim(5003)
print('$'*100)
print('nama yang baru menjadi', namaMahasiswa)  # tidak berubah
print("="*100)
print('nim yang baru adalah', nimMahasiswa)
