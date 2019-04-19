# Crypto I

## Assignment details

This assignment has three parts. It is due by 4/26/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 ( Pts)

Hash crackers are cool, but can you write your own?

Your task is to write a small script to crack some [hashes.](hashes.txt). You
know that the hashes are formed by prepending a lowercase letter in the English
alphabet to a word in [this list](passwords.txt), then fed through the SHA256
algorithm. Write a script that reads in the hashes file and the passwords file,
and prints out the inputs corresponding to each hash.

### Part 2 ( Pts)



#### Important notes

Make sure to submit **all** of the code you write!

### Scoring

Full points will be granted for Python3 scripts that read in the hash and
password files, cracks each hash, and prints the correct input-hash pairs.
Points will be deducted for not reading in the files, or not implementing a hash
cracker.



### Tips

In Part 1, a common source of error is not stripping off the newline characters
after reading in each line of the file. You will fail to find the correct input
corresponding to each hash if you keep the newline character on each password
before you prepend a character and hash it, or compare this hash to one in the
hash file that still has the newline character.
