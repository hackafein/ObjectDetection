#include <Servo.h>

Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;

int servo1 = 90;
int servo2 = 90;
int servo3 = 90;
int servo4 = 90;
int servo1_1, servo1_2, servo2_1, servo2_2, servo3_1, servo3_2,servo4_1,servo4_2;
int deger = 0;
int sayac = 0;
int tus_bilgisi;
void servo_home()
{
  myservo1.write(90); delay(25);
  myservo2.write(90); delay(25);
  myservo3.write(90); delay(25);
}
void setup()
{
  Serial.begin(9600);
  myservo1.attach(4); // yatay tabla servo
  myservo2.attach(5); // tabla üstü servo
  myservo3.attach(6); // kol servo
  myservo4.attach(7);
  servo_home();
}

void loop()
{
  if (Serial.available())
  {
  if(Serial.available()){
    tus_bilgisi=Serial.read();
  }
  if (tus_bilgisi == 11)
  {
    for (servo1_1 = servo1; servo1_1 < 179; servo1_1++)
    {
      if (Serial.available())
      {
        tus_bilgisi = Serial.readStringUntil('*').toInt();
        Serial.println(tus_bilgisi);
      }
      myservo1.write(servo1_1);
      delay(100);
      if (tus_bilgisi == 3) {
        sayac = 1;
        break;
      }
    }
  }
  else if (tus_bilgisi == 12)
  {
    for (servo1_2 = servo1;  servo1_2 > 0; servo1_2--)
    {
      if (Serial.available())
      {
        tus_bilgisi = Serial.readStringUntil('*').toInt();
        Serial.println(tus_bilgisi);
      }
      myservo1.write(servo1_2);
      delay(100);
      if (tus_bilgisi == 3) {
        sayac = 2;
        break;
      }
    }
  }
  else if (tus_bilgisi == 21)
  {
    for (servo2_1 = servo2; servo2_1 < 179; servo2_1++)
    {
      if (Serial.available())
      {
        tus_bilgisi = Serial.readStringUntil('*').toInt();
        Serial.println(tus_bilgisi);
      }
      myservo2.write(servo2_1);
      delay(100);
      if (tus_bilgisi == 3) {
        sayac = 3;
        break;
      }
    }
  }
  else if (tus_bilgisi == 22)
  {
    for (servo2_2 = servo2;  servo2_2 > 0; servo2_2--)
    {
      if (Serial.available())
      {
        tus_bilgisi = Serial.readStringUntil('*').toInt();
        Serial.println(tus_bilgisi);
      }
      myservo2.write(servo2_2);
      delay(100);
      if (tus_bilgisi == 3) {
        sayac = 4;
        break;
      }
    }
  }
  else if (tus_bilgisi == 31)
  {
    for (servo3_1 = servo3; servo3_1 < 179; servo3_1++)
    {
      if (Serial.available())
      {
        tus_bilgisi = Serial.readStringUntil('*').toInt();
        Serial.println(tus_bilgisi);
      }
      myservo3.write(servo3_1);
      delay(100);
      if (tus_bilgisi == 3) {
        sayac = 5;
        break;
      }
    }
  }
  else if (tus_bilgisi == 32)
  {
    for (servo3_2 = servo3;  servo3_2 > 0; servo3_2--)
    {
      if (Serial.available())
      {
        tus_bilgisi = Serial.readStringUntil('*').toInt();
        Serial.println(tus_bilgisi);
      }
      myservo3.write(servo3_2);
      delay(100);
      if (tus_bilgisi == 3) {
        sayac = 6;
        break;
      }
    }
  }
    else if (tus_bilgisi == 41)
  {
    for (servo4_1 = servo4; servo4_1 < 179; servo4_1++)
    {
      if (Serial.available())
      {
        tus_bilgisi = Serial.readStringUntil('*').toInt();
        Serial.println(tus_bilgisi);
      }
      myservo4.write(servo4_1);
      delay(100);
      if (tus_bilgisi == 3) {
        sayac = 7;
        break;
      }
    }
  }
  else if (tus_bilgisi == 42)
  {
    for (servo4_2 = servo4;  servo4_2 > 0; servo4_2--)
    {
      if (Serial.available())
      {
        tus_bilgisi = Serial.readStringUntil('*').toInt();
        Serial.println(tus_bilgisi);
      }
      myservo4.write(servo4_2);
      delay(100);
      if (tus_bilgisi == 3) {
        sayac = 8;
        break;
      }
    }
  }
  if (tus_bilgisi == 3)
  {
    if (sayac == 1) servo1 == servo1_1;
    else if (sayac == 2) servo1 = servo1_2;
    else if (sayac == 3) servo2 = servo2_1;
    else if (sayac == 4) servo2 = servo2_2;
    else if (sayac == 5) servo3 = servo3_1;
    else if (sayac == 6) servo3 = servo3_2;
    else if (sayac == 7) servo4 = servo4_1;
    else if (sayac == 8) servo4 = servo4_2;
  }
}