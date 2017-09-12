hari = input ("Masukkan jumlah hari: ");
hari = int(hari);

tahun = hari / 365;
tahun = int(tahun);

bulan = (hari-tahun*365)/30;
bulan = int(bulan);

minggu = (hari-tahun*365-bulan*30)/7;
minggu = int(minggu);

sisa_hari = hari - (tahun*365+bulan*30+minggu*7); 
