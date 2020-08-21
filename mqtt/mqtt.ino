#include <PubSubClient.h>
#include "WiFi.h"

#include "DHT.h"
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN,DHTTYPE);

const char* ssid = "IOT CLOCK";
const char* password = "12345678";

const char* mqttServer = "13.233.38.1";
const int mqttPort = 1883;
WiFiClient espClient;
PubSubClient client(espClient);

void setup(void){
  dht.begin();
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to the WiFi network");
  client.setServer(mqttServer, mqttPort);
  while (!client.connected()){
    Serial.println("Connecting to MQTT...");

//    if (client.connect("ESP32Client", mqttUser, mqttPassword )) {
    if (client.connect("ESP32Client")) {
      Serial.println("connected");
    }else {
      Serial.print("fail with state");
      Serial.print(client.state());
      delay(2000);
    }
  }
  client.setCallback(callback);
  client.subscribe("lora");
}

void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  String payload_data;
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    payload_data += (char)message[i];
  }
}

void loop(void){
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  Serial.print("humidity: ");
  Serial.print(h);
  Serial.print(" temperature: ");
  Serial.println(t);
  client.loop();
  String Data = String(h)+ "," + String(t);
  client.publish("home",Data.c_str());
}
