
import sqlite3


def kopektablosunagir():
    try:
        sqliteConnection = sqlite3.connect('canlilar.db')
        cursor = sqliteConnection.cursor()
        
        kopekid=str(input("Lütfen Köpek id sini giriniz id uniqe olmalı!= "))
        cinsi=str(input("Lütfen Köpek cinsini giriniz= "))
        ysmsrs=str(input("Lütfen Köpek yaşam süresini giriniz= "))
        koken=str(input("Lütfen Köpek kökenini giriniz= "))
        sqlite_insert_query = """INSERT INTO kopek
                            (Kopekid, Cinsi, OrtalamaYasamSuresi, Koken) 
                            VALUES (?, ?, ?, ?);"""
        data_tuple = (kopekid, cinsi, ysmsrs, koken)
        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        print("Girdiler başarıyla köpek tablosuna kaydedildi ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            


def mantartablosunagir():
    try:
        sqliteConnection = sqlite3.connect('canlilar.db')
        cursor = sqliteConnection.cursor()
        mantarid=str(input("Lütfen Mantar id sini giriniz id uniqe olmalı!= "))
        latincead=str(input("Lütfen Mantarın Latince adını giriniz = "))
        bilinenad=str(input("Lütfen Mantarın bilinen adını giriniz= "))
        yenilebilir=str(input("Mantar yenilebilir mi EVET/HAYIR= "))
        degeri=str(input("Mantarın değeri? = "))

        sqlite_insert_query = """INSERT INTO mantar
                            (Mantarid, Latinceadi, Bilinenadi, Yenilebilir, Degeri) 
                            VALUES (?, ?, ?, ?, ?);"""
        data_tuple = (mantarid,latincead,bilinenad,yenilebilir,degeri)
        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        print("Girdiler başarıyla mantar tablosuna kaydedildi ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
           

def cicektablosunagir():
    try:
        sqliteConnection = sqlite3.connect('canlilar.db')
        cursor = sqliteConnection.cursor()
        cicekid=str(input("Lütfen Çiçek id sini giriniz id uniqe olmalı!= "))
        cicekad=str(input("Lütfen Çiçeğin ismini= "))
        cicekbolge=str(input("Lütfen Çiçeğin yetiştiği bölgeyi giriniz= "))
        sqlite_insert_query = """INSERT INTO cicek
                            (Cicekid, Ad, Bolge) 
                            VALUES (?, ?, ?);"""
        data_tuple = (cicekid,cicekad,cicekbolge)
        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        print("Girdiler başarıyla cicek tablosuna kaydedildi ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            

def kustablosunagir():
    try:
        sqliteConnection = sqlite3.connect('canlilar.db')
        cursor = sqliteConnection.cursor()
        kusid=str(input("Lütfen Kuş id sini giriniz id uniqe olmalı!= "))
        kusad=str(input("Lütfen Kuşun ismini giriniz= "))
        kusbolge=str(input("Lütfen Kuşun yetiştiği bölgeyi giriniz= "))
        kusiklim=str(input("Lütfen Kuşun iklimini giriniz= "))
        evdebeslenme=str(input("Kuş evde beslenebilir mi EVET/HAYIR= "))
        sqlite_insert_query = """INSERT INTO kus
                            (Kusid, Ad, Bolge, iklim, Evdebeslenmesi) 
                            VALUES (?, ?, ?, ?, ?);"""
        data_tuple = (kusid,kusad,kusbolge,kusiklim,evdebeslenme)
        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        print("Girdiler başarıyla kus tablosuna kaydedildi ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            
while 1:
    print("""
    **** Veri Tabanına bilgi girişi ****
    1-) Kuş bilgileri Gir
    2-) Köpek bilgileri Gir
    3-) Çiçek bilgileri Gir
    4-) Mantar bilgileri Gir
    5-) Çıkış....

    """)
    secim=int(input("Lütfen bir seçim yapınız= "))
    if secim==1:
        kustablosunagir()
    elif secim==2:
        kopektablosunagir()
    elif secim==3:
        cicektablosunagir()
    elif secim==4:
        mantartablosunagir()
    elif secim==5:
        break
    else:
        print("Hata lütfen geçerli  bir sonuç giriniz")