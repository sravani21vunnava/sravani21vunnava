#include <avr/io.h>
#include <stdbool.h>
#include <util/delay.h>
int main (void)
{

 bool X=0,Y=0,Z=0,G=0;
 DDRB =  0b00000001;
 DDRD =  0b11100011;
 PORTD = 0b00011100;
while(1){
Z = (PIND & (1 << PIND4)) == (1 << PIND4);
Y = (PIND & (1 << PIND3)) == (1 << PIND3);
X = (PIND & (1 << PIND2)) == (1 << PIND2);
G = (X|Y)&(X|(!Z))&((!X)|(!Y)|(Z));
PORTB |= (G << 0);
}
return 0;
}
