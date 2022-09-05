.include "/home/sravani/m328Pdef.inc"
ldi r16,0b11100011
out DDRD,r16
ldi r17,0b11111111  ;  activating pull ups
out PORTD,r17
ldi r16,0b00000001
out DDRB,r16            ;declaring 8th pin as output
loop:                   ;loop for reading the input from pins 2,3,4 continously

        in r17,PIND             ;reading the data from pins 2,3,4
;Taking z
        ldi r24,0b00000100
        mov r18,r17
        and r18,r24
        ldi r25,0b00000010
        loopx:  lsr r18
        dec r25
        brne    loopx
        .DEF Z = r18
;Taking y
        mov r19,r17
        ldi r24,0b00001000
        and r19,r24
        ldi r25,0b00000011
        loopy:  lsr r19
        dec r25 brne    loopy

        .DEF Y = r19
;Taking x
        ldi r24,0b00010000
        mov r20,r17
        and r20,r24
         ldi r25,0b00000100
        loopz:  lsr r20
        dec r25
        brne    loopz
        .DEF X = r20
        ldi r21,0x00
        ldi r22,0x00
        ldi r23,0x00
        .DEF T1 = r21
        .DEF T2 = r22
        .DEF T3 = r23

        ;POS expression
        ;G = (X+Y)(X+Z')(X'+Y'+Z)

        mov T1,X
        or T1,Y       ;T1 = X+Y
        mov T2,Z
        com T2
	or T2,X       ;T2= X+Z'
        ldi r25,0b00000001
        and T2,r25
        com X
        or X,Z
        com Y
        or X,Y
        and X,r25
        mov T3,X
        and T1,T2
        and T1,T3
        out PORTB,T1
        rjmp loop
start:
        rjmp start
