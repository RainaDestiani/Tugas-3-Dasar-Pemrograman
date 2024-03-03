Algoritma = 84
Perancangan_objek = 88
Kalkulus = 89
Etika_profesi = 80
Database = 85
English = 79

def SkorToBobot (nilai) :
    if nilai >= 90:
        return 4
    elif nilai >= 85:
        return 3.75
    elif nilai >= 80:
        return 3.5
    elif nilai >= 75:
        return 3.25
    elif nilai >= 70:
        return 3
    elif nilai >= 65:
        return 2.75
    elif nilai >= 60:
        return 2.50
    elif nilai >= 55:
        return 2.25
    elif nilai >= 50:
        return 2
    elif nilai >= 45:
        return 1.75
    elif nilai >= 40:
        return 1.50
    elif nilai >= 35:
        return 1.25
    elif nilai >= 30:
        return 1
    else :
        return 0
    

sks_Algoritma = 4
sks_PerancanganObjek = 3
sks_Kalkulus = 3
sks_EtikaProfesi = 2
sks_Database = 3
sks_English = 2

total_Algoritma        = sks_Algoritma * SkorToBobot(Algoritma)
total_PerancanganObjek = sks_PerancanganObjek * SkorToBobot(Perancangan_objek)
total_Kalkulus         = sks_Kalkulus * SkorToBobot(Kalkulus)
total_EtikaProfesi     = sks_EtikaProfesi * SkorToBobot(Etika_profesi)
total_Database         = sks_Database * SkorToBobot(Database)
total_English          = sks_English * SkorToBobot(English)

total_sks = sks_Algoritma + sks_PerancanganObjek + sks_Kalkulus +  sks_EtikaProfesi + sks_Database  + sks_English 

IPK = ( total_Algoritma + total_PerancanganObjek + total_Kalkulus + total_EtikaProfesi + total_Database +  total_English ) / total_sks

print(" IPK anda adalah :" , IPK )







