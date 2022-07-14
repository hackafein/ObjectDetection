import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('canlilar.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS kopek")

#Creating table as per requirement
sql ='''CREATE TABLE kopek(
   Kopekid INT NOT NULL,
   Cinsi CHAR(20),
   OrtalamaYasamSuresi INT,
   Koken CHAR(20)
)'''
cursor.execute(sql)

print("Table created successfully........")

cursor.execute("DROP TABLE IF EXISTS cicek")

#Creating table as per requirement
sql ='''CREATE TABLE cicek(
   Cicekid INT NOT NULL,
   Ad CHAR(20),
   Bolge CHAR(20)
)'''
cursor.execute(sql)
print("Table created successfully........")

cursor.execute("DROP TABLE IF EXISTS kus")

#Creating table as per requirement
sql ='''CREATE TABLE kus(
   Kusid INT NOT NULL,
   Ad CHAR(20),
   Bolge CHAR(20),
   iklim CHAR(20),
   Evdebeslenmesi CHAR(20)
)'''
cursor.execute(sql)
print("Table created successfully........")

cursor.execute("DROP TABLE IF EXISTS mantar")

#Creating table as per requirement
sql ='''CREATE TABLE mantar(
   Mantarid INT NOT NULL,
   Latinceadi CHAR(20),
   Bilinenadi CHAR(20),
   Yenilebilir CHAR(20),
   Degeri CHAR(20)
)'''
cursor.execute(sql)
print("Table created successfully........")

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()