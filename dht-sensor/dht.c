#include<stdio.h>
#include<DHT.h>
DHT dht(12, DHT11);

void setup(){
	Serial.begin(9600);
}

void loop(){
	delay(3000);
	int tem = dht.readTemperature();
	int hum = dht.readHumidity();
	print("tem"=%d, tem)

}
