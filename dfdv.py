a=int(input("Sayıyı Girin : "))
if a == 2 or a >2:
  for i in range(2,a):
   if (a % i) == 0:
     print(a," Asal Sayi Değildir.")
     break
   else:
       print(a," Asal Sayıdır.")
else:
   print(a," Asal Sayı Değildir.")
