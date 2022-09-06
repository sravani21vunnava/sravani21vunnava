#include <avr/io.h>

//Function declared in initasm.S
extern void init(void);
extern void loop(void);


 int main (void)
{
  while (1)
   {
	  init();
	  loop();
		  	  
  }
  return 0;

}
