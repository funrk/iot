int LM35Pin=A0;

void setup () {
// put your setup code here, to run once:
Serial.begin(9600);

void loop () {
// put your main code here, to run repeatedly:

// Get the ADC value from temperator sensor
int adcVal=analogRead (LM35Pin) ;

//
float miliVolt=adcVal*(5000/1024);

convert the ADC value to voltage in milivolts

//convert the voltage to the temperature in celsius
float tempC=miliVolt/10;

// convert the celsius to Fahrenheit
flat tempF=tempC*9/5 +32;


//Print the temp in serial monitor
Serial.print ("Temperature:");
Serial.print (tempC);
Serial.println ("degreeC");
Serial.print (" ~ ");


Serial.print ("Fahrenheit:");
Serial.print (tempF);
Serial.println("F");
delay(1000);

}