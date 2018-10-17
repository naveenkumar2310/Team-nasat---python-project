


#include <LiquidCrystal.h>

LiquidCrystal lcd(12,11,5,4,3,2);//configure the lcd

#define a A0 // analog input to read the voltage of the thermistor
double b;// an intermediate variable
double Vt;
double Rt;
int R=110;
int B=2800;
int R0=5;
int T0=25;
double T;
void setup() {
analogWrite(6,120);
lcd.begin(16,2);
Serial.begin(115200);
}

void loop() {
  b=analogRead(a);// get the value in the A0
  Vt= (b/1024)*5;
  Rt=(R*Vt)/(5-Vt);
  T=1/((log(Rt/R0)/B)+(1/(T0+273.15))); /
  Serial.println(T-273.15);
  
  // desplay the temperature in the lcd
  lcd.clear();
  lcd.print("temp is: ");
  lcd.print(T-273.15);
  lcd.print(" D");
  
  // trigger the security alarm if the temperature is higher than 60 degree
  if ((T-273.15)>60){
      digitalWrite(13,HIGH);
      delay(500);
      digitalWrite(13,LOW);
      delay(500);
  }
 else{
  delay(1000);
  }
  
 }
