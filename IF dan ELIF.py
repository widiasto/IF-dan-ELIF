nama = "Gama Widiasto"
nim = "04217017"
umur = 18
jeniskelamin = "L"

print("Namaku :" + nama)
print("Nim :" + nim)
print("Umur")
print(umur)
print("Jenis Kelamin :" + jeniskelamin)

if(jeniskelamin == "L"):
    sex = "LAKI-LAKI"
else:
    sex = "PEREMPUAN"

if(umur <= 3):
    print("Umurku:", umur, "Tahun ->", sex, "BATITA")
elif(umur <= 5):
    print("Umurku:", umur, "Tahun ->", sex, "BALITA")
elif(umur <=18):
    print("Umurku:", umur, "Tahun ->", sex, "REMAJA")
elif(umur <=40):
    print("Umurku:", umur, "Tahun ->", sex, "DEWASA")
elif(umur <=60):
    print("Umurku:", umur, "Tahun ->", sex, "TUA")
else:
    print("Umurku:", umur, "Tahun ->", sex, "MANULA")
