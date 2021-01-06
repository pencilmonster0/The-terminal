#Kodda sürekli boşluk şeyini düzeltmemek için gereksiz bir if koyuyorum.
boşluk=0
isim=input("Lütfen isminizi girin.")
if boşluk==0:
    print("Sayın ",isim,", SSAL Hazırlık Python Terminali 2.1'e Hoşgeldiniz...")
    print("Bu terminalde bilişim dersi için yapılmış olan projelere ulaşabilirsiniz.")
    istenen= input ("""
     Lütfen istediğiniz işlemin adını giriniz.
Seçenekleriniz şunlardır:
İşlem , Sınav Ortalaması Hesaplama,Tahmin Oyunu,Sana göre en iyi ABBA şarkısı,Değer Çevirici,Vücut Kitle Endeksi,Kronometre ve Saat,Passcode Generator, Emeği Geçenler, Güncelleme Notları, Yeni Yıl Müziği
""")
    if istenen=="İşlem":
        islem=str(input("Şimdi bu sayıyla ne yapmak istediğinizi giriniz.Seçenekleriniz şunlardır:\n Toplama, çıkartma, çarpma, bölme, üs alma, karekök alma.\t"))
        if islem=="Toplama" and "çıkartma" and "çarpma" and "bölme" and "üs alma":       
            sayi1=int(input("Lütfen bir sayı giriniz."))
            sayi2=int(input("Lütfen bir sayı daha giriniz"))
        if islem=="Toplama":
            toplam=sayi1+sayi2
            print("İşlemin sonucu ",toplam,"dır.")
        if islem=="çıkartma":
            fark=sayi1-sayi2
            print("İşlemin sonucu ",fark,"dır.")
        if islem=="çarpma":
            carpim=sayi1*sayi2
            print("İşlemin sonucu ",carpim,"dır.")
        if islem=="bölme":
            bölüm=sayi1/sayi2
            print("İşlemin sonucu ",bölüm,"dür.")
        if islem=="üs alma":
            üs=sayi1**sayi2
            print("İşlemin sonucu ",üs,"tür.")
        if islem=="karekök alma":
           num=float(input('Sayı girin:'))
           num_sqrt=num**0.5
           print("",num,"in karekökü",num_sqrt," dir.")
           

            
            
    if istenen=="Sınav Ortalaması Hesaplama":  
            sinav=int(input("lütfen sınav notunu gir.\t"))
            if sinav>100:
                print("Geçersiz sayı girdiniz.Lütfen 100 veya ondan düşük bir sayı giriniz.")
                sinav=int(input("lütfen sınav notunu gir.\t"))
            sozlu=100-sinav
            (sinav*50/100)+(sozlu*50/100)==50
            if sozlu>100:
                print("Geçme şansın yok")
            else:
                print("Sözlülerle geçmen için en az",sozlu," puan gerekiyor")
            cevap=str(input("Ortalama hesaplamak ister misin?\n Eğer istiyorsan evet,\n Eğer istemiyorsan hayır yazmalısın.\t"))
            if cevap==("evet"):
               sozlu2=int(input("Tamam öyleyse, sınav notunu önceden girdiğin için tekrar sormayacağım.Lütfen öğretmeninin sana vereceği sözlü notunu gir.\t"))
               if sozlu2<=100:
                  ortalama=(sinav/2)+(sozlu2/2)
                  print("Ortalamanız ",ortalama,"dır.")
               if ortalama>=50:
                  print("Tebrikler, sınıfı geçtiniz.")
               if 70<=ortalama<85:
                  print("Tebrikler, teşekkür belgesi kazandınız.")
               if 85<=ortalama<100:
                  print("Tebrikler, Takdir Belgesi kazandınız.")
               if ortalama==100:
                  print("Tebrikler, Onur Belgesi kazandınız.")
               if ortalama<50:
                  print("Maalesef sınıfı geçemediniz.")
               if sozlu2>100:
                  print("Yanlış girdiniz iyi günler")
    
    
            if cevap==("hayır"):
               print ("Tamam iyi günler")

    if istenen=="Sana göre en iyi ABBA şarkısı":
        abba=str(input("Bugün Nasıl hissediyorsun? \n Enerjik hissediyorsan enerjik \n üzgün hissediyorssan üzgün, \n heyecanlıysan heyecanlı,\n sinirli isen sinirli, \n mutlu isen mutlu yaz.\t"))
        if abba==("enerjik"):
           print("Senin için en uygun abba şarkısı Waterloo.\n dinlemek için https://www.youtube.com/watch?v=Sj_9CiNkkn4 bu linki kopyalayabilirsin.")
           import pyglet
           sound = pyglet.media.load('Abba - Waterloo.mp3', streaming=False)
           sound.play()
           pyglet.app.run()
        if abba==("üzgün"):
           print("Senin için en uygun abba şarkısı The Winner Takes it All.\n dinlemek için https://www.youtube.com/watch?v=iyIOl-s7JTU bu linki kopyalayabilirsin.")
           import pyglet
           sound = pyglet.media.load('abba-the-winner-takes-it-all-1980-hd-0815007.mp3', streaming=False)
           sound.play()
           pyglet.app.run()
        if abba==("heyecanlı"):
           print("senin için en uygun abba şarkısı dancing queen.\n https://www.youtube.com/watch?v=xFrGuyw1V8s dinlemek için bu linke tıklayabilirsin.")
           import pyglet
           sound = pyglet.media.load('Abba - Dancing Queen.mp3', streaming=False)
           sound.play()
           pyglet.app.run()
        if abba==("sinirli"):
           print("senin için en uygun abba şarkısı gimme gimme.\n https://www.youtube.com/watch?v=XEjLoHdbVeE dinlemek için bu linke tıklayabilirsin.")
           import pyglet
           sound = pyglet.media.load('ABBA - Gimme! Gimme! Gimme! (A Man After Midnight).m4a', streaming=False)
           sound.play()
        if abba==("mutlu"):
           print("Senin için en uygun abba şarkısı take a chance on me. \n https://www.youtube.com/watch?v=-crgQGdpZR0 dinlemek için bu linke tıklayabilirsin.")
           import pyglet
           sound = pyglet.media.load('Abba - Take A Chance On Me (Official Video).m4a', streaming=False)
           sound.play()

    if istenen=="Tahmin Oyunu":
        #Bu programda bilgisayarın rastgele belirlediği sayıyı bulmaya çalışıyoruz
        from random import randint
        rastgele=randint(1,50)
        sayaç=0

        while True:
            sayaç+=1
            sayi=int(input("1 ile 50 arasında bir tahmin girin(0 girerseniz kod kapanır.)"))
            if sayi==0:
               print("tekrar görüşmek dileğiyle.")
               break
            elif sayi<rastgele:
               print("Tahmininiz gerçek sayıdan küçük.")
               continue
            elif sayi>rastgele:
               print("Tahmininiz gerçek sayıdan büyük.")
            elif sayi==rastgele:
               print("Rastgele seçilen sayi {}".format(rastgele))
               print("Şu kadar seferde sayıyı buldunuz: {}".format(sayaç))
               break
    
          


    if istenen=="Vücut Kitle Endeksi":
        kilogram=float(input("Lütfen kilonuzu giriniz."))
        boy=float(input("Lütfen boyunuzu giriniz."))
        endeks=(kilogram)/((boy/100)**2)
        if endeks<=18.4:
            print("Zayıfsınız. Vücut kitle endeksiniz:",endeks)
        elif endeks<=24.9:
            print("Normal Kilodasınız. Vücut kitle endeksiniz:",endeks)
        elif endeks<=29.9:
            print("Fazla Kilodasınız. Vücut kitle endeksiniz:",endeks)
        elif endeks<=34.9:
            print("Şişmansınız. Birinci derece obeziteniz var. Vücut kitle endeksiniz:",endeks)
        elif endeks<=44.9:
            print("Şişmansınız. İkince derece obeziteniz var. Vücut kitle endeksiniz:",endeks)
        else:
            print("Aşırı fazla ultra mega olağanüstü şişmansınız. Üçüncü derece obeziteniz var. Az yiyin biraz. Vücut kitle endeksiniz:",endeks)
    if istenen=="Kronometre ve Saat":
        import time 
        sayi=0
        kronometreDakika=0
        kronometreSaniye=0
        sonsuz=float('inf')

        a=input("Kronometre mi saat mi istediğinizi yazın. (kronometre, saat):")
        if a=="saat":
           saat=int(input("Şimdiki saati yazın. Örnek: (4,7,12):"))
           dakika=int(input("Şimdiki dakikayı yazın. Örnek: (7,15,46):"))
           while float(sayi < sonsuz):
               if dakika<10:
                   print("{}:0{}".format(saat,dakika))
               else:
                   print("{}:{}".format(saat,dakika))
                   if dakika==60:
                       dakika=0
                       saat=saat+1
                       sayi=sayi+1        
               time.sleep(60)
               dakika=dakika+1
        elif a=="kronometre":
            while float(sayi < sonsuz):
                kronometreSaniye=kronometreSaniye+1
                time.sleep(1)
                if kronometreSaniye==60:
                   kronometreSaniye=0
                   kronometreDakika=kronometreDakika+1
                if kronometreSaniye<10:
                   print("{}:0{}".format(kronometreDakika,kronometreSaniye))
                else:
                   print("{}:{}".format(kronometreDakika,kronometreSaniye))

        else:
          print("Kronometre veya saat dışında bir kelime yazdığınız için program başlatılamıyor.")
          time.sleep(3)
    if istenen=="Değer Çevirici":
        istenen1=input("""
Sistemimize hoş geldiniz. Hangi sistemi seçmek istediğinizi lütfen belirtin.
fahrenheit-celsius 1
mil-km için 2
inch-cm için 23
galon-litre için 4
feet-metre için 5
m/sn-km/h için 6'ya basıp entera tıklayın.
""")
#buraya eklemeler yapılacak
        if istenen1=="1":
             taraf1=input("Hangi taraftan çevirmek istediğinizi lütfen belirtin.")
             if taraf1=="celsius":
                 celsius=float(input("Lütfen kaç dereceyi çevirmek istediğinizi yazın."))
                 fahrenheit=(celsius*9/5)+32
                 print("{} celsius derece {} fahrenheit dereceye eşittir.".format(celsius, fahrenheit))
             elif taraf1=="fahrenheit":
                 fahrenheit=float(input("Lütfen kaç dereceyi çevirmek istediğinizi yazın."))
                 celsius=(fahrenheit-32)*5/9
                 print("{} fahrenheit derece {} celsius dereceye eşittir.".format(fahrenheit, celsius))
             else:
                 print("Ne dediğini anlayamadık. Tekrar dene.")
        
        if istenen1=="2":
            taraf1=input("Hangi taraftan çevirmek istediğinizi lütfen belirtin.")
            if taraf1=="km":
               km=float(input("Lütfen kaç kilometreyi çevirmek istediğinizi yazınız."))
               mil=km/1.609
               print("{} kilometre {} mile eşittir.".format(km, mil))
            elif taraf1=="mil":
               mil=float(input("Lütfen kaç mili çevirmek istediğinizi yazınız."))
               km=mil*1.609
               print("{} mil {} kilometreye eşittir.".format(mil, km))
            else:
                print("Ne dediğinizi anlayamadık. Tekrar dene.")

        if istenen1=="3":
            taraf1=input("Hangi taraftan çevirmek istediğinizi lütfen belirtin.")
            if taraf1=="cm":
               cm=float(input("Lütfen kaç santimetretyi çevirmek istediğinizi yazınız."))
               inch=cm/2.54
               print("{} santimetre {} inchtir.".format(cm, inch))
            elif taraf1=="inch":
               inch=float(input("Lütfen kaç inchi çevirmek istediğinizi belirtin."))
               cm=inch*2.54
               print("{} inch {} santimetreye eşittir.".format(inch, cm))
            else:
               print("Ne dediğini anlayamadık. Tekrar dene.")

        if istenen1=="4":
            taraf1=input("Hangi taraftan çevirmek istediğinizi lütfen belirtin.")
            if taraf1=="galon":
               galon=float(input("Lütfen kaç galonu çevirmek istediğinizi yazınız."))
               litre=galon*3.78
               print("{} galon {} litredir.".format(galon, litre))
            elif taraf1=="litre":
               litre=float(input("Lütfen kaç litreyi çevirmek istediğinizi giriniz."))
               galon=litre/3.78
               print("{} litre {} galondur.".format(litre, galon))
            else:
               print("Ne dediğinizi anlayamadık. Tekrar dene.")
        
        if istenen1=="5":
            taraf1=input("Hangi taraftan çevirmek istediğinizi lütfen belirtin.")
            if taraf1=="feet":
               feet=float(input("Lütfen ne kadar çevirmek istediğinizi lütfen belirtin."))
               metre=feet/3.281
               print("{} feet {} metreye eşittir.".format(feet, metre))
            elif taraf1=="metre":
               metre=float(input("Lütfen ne  kadar çevirmek istediğinizi lütfen belirtin."))
               feet=metre*3.281
               print("{} metre {} feete eşittir.".format(metre, feet))
            else:
               print("Ne dediğinizi anlayamadık. Tekrar dene.")
        
        if istenen1=="6":
            taraf1=input("Hangi taraftan çevirmek istediğinizi lütfen belirtin.")
            if taraf1=="m/sn":
               msn=float(input("Lütfen ne kadar çevirmek istediğinizi belirtin."))
               kmh=msn*3.6
               print("{} m/sn {} km/h e eşittir.".format(msn, kmh))
            elif taraf1=="km/h":
                 kmh=float(input("Lütfen ne kadar çevirmek istediğinizi belirtin."))
                 msn=kmh/3.6
                 print("{} km/h {}m/sn e eşittir.".format(kmh, msn))
            else:
                 print("Ne dediğinizi anlayamadık. Tekrar dene.")
    
        
        
    

    if istenen=="Passcode Generator":
        import random
        karakterler='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%*&"'
        sayi=input("Kaç tane şifre üretilsin?: ")
        sayi=int(sayi)
        uzunluk=input("Şifre uzunluğunu yazınız: ")
        uzunluk=int(uzunluk)
        for s in range(sayi):
            sifre=''
            for k in range(uzunluk):
                sifre += random.choice(karakterler)
            print(sifre)
    if istenen=="Yeni Yıl Müziği":
        print("3 saniye sonra müzik başlayacaktır.")
        import pyglet
        sound = pyglet.media.load('ABBA - Happy New Year 1980 (High Quality).m4a', streaming=False)
        sound.play()
        pyglet.app.run()
        
        
    
                    

    

    if istenen=="Emeği Geçenler":
        print("""
\tAli Gürlek
                \tArden Zeyfiyan
\tHabib Doğanay Dönmez
                   \tDoruk Çerit
""")
#buraya sonra ekleme yapılacak


    if istenen=="Güncelleme Notları":
        print("""
1.0
Terminal Giriş Eklendi
Ortalama SÖzlü Hesaplama Eklendi
Ruh Haline Göre En iyi Abba Şarkısı eklendi
Hesap Makinesi Eklendi
1.01
Bug fix
1.1
Abba şarkısı kısmına ekleme yapıldı
1.2
Karekök ve Üs Alma Eklendi
1.3
Vücut Kitle Endeksi Eklendi
Emeği Geçenler Bölümü Eklendi
Güncelleme Notları Bölümü Eklendi
Bazı Boşluk Hataları Giderildi
2.0
Kullanıcı adı şifre kaldırıldı
isim soyisim eklendi
kronometre ve saat eklendi
ses dosyaları eklendi
şifre generator eklendi
2.1
""")

import msvcrt
char = 0
print ('Devam etmek için bir tuşa basınız.')
while not char:
    char = msvcrt.getch()


   

    
