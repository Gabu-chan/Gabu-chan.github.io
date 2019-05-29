#include <LiquidCrystal.h>
#include "DHT.h"
#define DHTPIN 8    // what pin we're connected to
#define DHTTYPE DHT11   // DHT 11 

DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal lcd(2, 3, 4, 5, 6, 7); // Creates an LC object. Parameters: (rs, enable, d4, d5, d6, d7) 

void setup() {
  Serial.begin(9600); 
  
  lcd.begin(16,2);
  
  Serial.println("DHTxx test! NOW WITH LCD!!!!!!!!!");
 
  dht.begin();
}

void loop() {
  delay(2000);

