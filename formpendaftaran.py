nama             = input("Masukan nama anda :")
Tempat_lahir     = input("Masukan tempat lahir anda :")
Tanggal_lahir    = int (input("Masukan tanggal lahir anda :"))
Tahun_lahir      = int (input("Masukan tahun lahir anda :"))
Tahun_Sekarang   = int (input("Masukan tahun sekarang :"))
Jenis_kelamin    = input ("Masukan jenis kelamin anda :")

Nilai_English    = float (input("Masukan nilai English anda :"))
Nilai_Mtk        = float(input("Masukan nilai mtk anda :"))
Nilai_Indonesia  = float(input("Masukan nilai Bahasa Indonesia anda :"))

nilai_rata_rata = (Nilai_English + Nilai_Mtk + Nilai_Indonesia)/3
if nilai_rata_rata >= 80 and Jenis_kelamin.lower() == "Laki-laki":
    print("Anda disarankan masuk Jurusan Teknik Informatika")
elif nilai_rata_rata >= 80 and Jenis_kelamin.lower() == "Perempuan":
    print("Anda disarankan masuk Jurusan Sistem Informasi")
else :
    print("Anda disarankan masuk Jurusan DKV") 

umur = Tahun_Sekarang - Tahun_lahir

if umur > 25:
    print("Maaf anda tidak memenuhi persyaratan untuk diterima di Universitas ini")