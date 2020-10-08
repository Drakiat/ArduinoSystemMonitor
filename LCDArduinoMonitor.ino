
//Library version:1.1
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // set the LCD address to 0x27 for a 16 chars and 2 line display
int incomingByte = 0;
String data;
String a;
String b;
String c;
String d;
void setup()
{
  lcd.init();                      // initialize the lcd
  // Print a message to the LCD.
  lcd.backlight();
  lcd.print("Loading...");
  Serial.begin(9600);
  //start serial
}

void loop()
 {
  while (Serial.available()) {
    data = Serial.readString(); // read the incoming data as string
    int a1 = data.indexOf("a");
    int b1 = data.indexOf("b");
    int c1 = data.indexOf("c");
    int d1 = data.indexOf("d");
    int e1 = data.indexOf("e");
    a = data.substring(a1 + 1, b1);
    b = data.substring(b1 + 1, c1);
    c = data.substring(c1 + 1, d1);
    d = data.substring(d1 + 1, e1);
  }
while(!Serial.available());{
  lcd.setCursor(0, 0);
  lcd.print("VRAM"+c+"%"+"GPU:" + a + ((char)223)+"C");
  lcd.setCursor(0, 1);
  lcd.print("RAM:" + b + "%CPU:"+ d + ((char)223) + "C");
  
}
}
