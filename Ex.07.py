int redLED =11;

int greenLED=10;
int blueLED=9;

const int sensorPin1=A0;
const int sensorPin2=A1;
const int sensorPin3=A2;

void setup () {
// put your setup code here, to run once:
Serial.begin(9600);
pinMode (redLED, OUTPUT) ;
pinMode (greenLED, OUTPUT) ;
pinMode (blueLED, OUTPUT) ;

void loop () {
// put your main code here, to run repeatedly:
int sensorValue1=analogRead (sensorPin1);
Serial.print ("Sensor Value 1:");
Serial.print (sensorValue1);

Serial.print (", volts :

float sensorVoltagel=(sensorValue1/1024.0) *5.0;
") ;
Serial.println(sensorVoltagel);
digitalWrite (redLED, sensorVoltage1);

int sensorValue2=analogRead (sensorPin2);
Serial.print ("Sensor Value 2:");
Serial.print (sensorValue2);
delay(1000) ;
float sensorVoltage2=(sensorValue2/1024.0) *5.0;
Serial.print (", volts : ");
Serial.println (sensorVoltage2);
digitalWrite (greenLED, sensorVoltage2);
delay (1000) ;

int sensorValue3=analogRead (sensorPin3);
Serial.print ("Sensor Value 3:");
Serial.print(sensorValue3);
delay(1000);
float sensorVoltage3=(sensorValue3/1024.0) *5.0;
Serial.print (", volts : ");
Serial.println (sensorVoltage3);
digitalWrite (greenLED, sensorVoltage3);
delay(1000);