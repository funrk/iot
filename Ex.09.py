const int greenLED=13;
const int yellowLED=8;
const int redLED=5;

void setup () {
// put your setup code here, to run once:
pinMode (greenLED, OUTPUT) ;
pinMode (yellowLED, OUTPUT) ;
pinMode (redLED, OUTPUT) ;
Serial.begin(9600);

void loop () {
// put your main code here, to run repeatedly:
if (Serial.available () )
{

char command=Serial.read ();
if (command == 'b')

for (int i=0; i<5; i++)

digitalWrite(greenLED, HIGH) ;
delay(500);
digitalWrite (greenLED, LOW) ;
delay (500);

}

}

else if (command == 'g')
{

digitalWrite(greenLED, HIGH) ;
digitalWrite (yellowLED, LOW) ;
digitalWrite (redLED, LOW) ;

}

else if (command == 'y')

digitalWrite (greenLED, LOW) ;
digitalWrite(yellowLED, HIGH) ;
digitalWrite (redLED, LOW) ;

else if (command == 'r')

{

digitalWrite (greenLED, LOW) ;
digitalWrite (yellowLED, LOW) ;
digitalWrite(redLED, HIGH) ;

}