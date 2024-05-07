const int greenLED=13;
const int yellowLED=8;
const int redLED=5;

int counter=0;

void setup()
{
  // put your setup code here, to run once:
  pinMode(greenLED,OUTPUT);
  pinMode(yellowLED,OUTPUT);
  pinMode(redLED,OUTPUT);
  Serial.begin(9600);

}


void loop()
{
  // put your main code here, to run repeatedly:
  if (Serial.available())
{
  counter=Serial.parseInt();
}
if (counter<100)

{
  digitalWrite(greenLED,HIGH);
  digitalWrite(yellowLED,LOW);
  digitalWrite (redLED,LOW);
}
else if (counter>=100 && counter<=200)
{
  digitalWrite(greenLED,LOW);
  digitalWrite(yellowLED,HIGH);
  digitalWrite (redLED,LOW);
}
else
{
  digitalWrite(greenLED,LOW);
  digitalWrite(yellowLED,LOW);
  digitalWrite (redLED,HIGH);
}
}