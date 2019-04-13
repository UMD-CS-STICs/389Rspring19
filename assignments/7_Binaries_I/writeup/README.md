# Writeup 7 - Binaries I

Name: Alex Bloch
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Alex Bloch

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
#include <stdio.h>

int main()
{

    unsigned char eight =0x1ceb00da;
    unsigned char four = 0xfeedface;
    printf("a = %d\n", four);
    printf("b = %d\n", eight);
    
    eight ^= four;
    four ^= eight;
    eight ^= four;
    
    printf("a = %d\n", four);
    printf("b = %d\n", eight);
    
    
    return 0;
}
```

### Part 2 (10 Pts)

Prints: 
a = 206                                                                                                               
b = 218                                                                                                               
a = 218                                                                                                               
a = 206     

Behind the scences, it swaps the a value and the b value 