/*
 * Name: Alex Bloch
 * Section: 0101
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Alex Bloch
 */

/* your code goes here */
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