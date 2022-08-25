
#include <Arduino.h>

int Z,Y,X;
int D;

//Code released under GNU GPL.  Free to use for anything.
void Kmap(int D)
{
  digitalWrite(5, D); //MSB
}
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(5, OUTPUT);
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
X = digitalRead(2);
Y = digitalRead(3);
Z = digitalRead(4);

D = (X||Y)&&(X||!Z)&&(!X||!Y||Z);
Kmap(D);
}
