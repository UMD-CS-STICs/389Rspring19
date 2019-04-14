# Writeup 7 - Binaries I

Name: Ashan Panduwawala
Section: 0101
I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Ashan Panduwawala
## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
#include <stdio.h>
int main()
{
int x = 0xfeedface;
int y = 0x1ceb00da;
int temp;
printf("%d\n" , x);
printf("%d\n", y);
x = x^y;
y = y^x;
x = x^y;
printf("%d\n", x);
printf("%d\n",y);
return 0;
}
```

### Part 2 (10 Pts)
 The first part of the code is initializing the stack to hold two local variables. The values of the two local variables are printed, then the values are swapped using bitwise operations, and finally the new swapped variables are printed again.
