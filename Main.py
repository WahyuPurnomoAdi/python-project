import datetime as dt

print("\nsilahkan masukan tanggal, \nbulan dan tahun lahir anda\n")
tanggal = int(input("tanggal \t:"))
bulan = int(input("bulan \t\t:"))
tahun = int(input("tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"\ntanggal lahir : {tanggal_lahir}")
print(f"hari lahir : {tanggal_lahir:%A}")


hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"umur sekarang : {umur_tahun} tahun, {umur_bulan_sisa} bulan\n")
print("\nsu(minggu) mo(senin) tu(selasa) we(rabu) th(kamis) fr(jum'at) sa(sabtu)\n")
