#define __SFR_OFFSET 0
#include <avr/io.h>

.global init

.section .text
init:
	ldi r16,0b11100011
	out DDRD,r16
	ldi r16,0b00000001
	out DDRB,r16
	ret
