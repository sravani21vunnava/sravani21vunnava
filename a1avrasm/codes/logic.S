
#define __SFR_OFFSET 0
#include <avr/io.h>
.global loop

.section .text
loop:

 in r17,PIND             ;reading the data from pins 2,3,4
;Taking z
        ldi r24,0b00000100
        mov r18,r17
        and r18,r24
        ldi r25,0b00000010
        loopx:  lsr r18
        dec r25
        brne    loopx
;Taking y
        mov r19,r17
        ldi r24,0b00001000
        and r19,r24
        ldi r25,0b00000011
        loopy:  lsr r19
        dec r25
	brne loopy
;Taking x
        ldi r24,0b00010000
        mov r20,r17
        and r20,r24
         ldi r25,0b00000100
        loopz:  lsr r20
        dec r25
        brne    loopz
        ldi r21,0x00
        ldi r22,0x00
        ldi r23,0x00

        ;POS expression
        ;G = (X+Y)(X+Z')(X'+Y'+Z)

        mov r21,r20
        or r21,r19       ;T1 = X+Y
        mov r22,r18
        com r22
        or r22,r20       ;T2= X+Z'
        ldi r25,0b00000001
        and r22,r25
	com r20
        or r20,r18
        com r19
        or r20,r19
        and r20,r25
        mov r23,r20
        and r21,r22
        and r21,r23
        out PORTB,r21
        rjmp loop
start:
        rjmp start
