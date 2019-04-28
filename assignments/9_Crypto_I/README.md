# Crypto I

## Assignment details

This assignment has two parts. It is due by 4/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (70 Pts)

Hash crackers are cool, but can you write your own?

Your task is to write a small script to crack some [hashes.](hashes.txt). You
know that the hashes are formed by prepending a lowercase letter in the English
alphabet to a word in [this list](passwords.txt), then fed through the SHA256
algorithm. Write a script that reads in the hashes file and the passwords file,
and prints out the inputs corresponding to each hash. Write your code in
`writeup/crack.py`.

### Part 2 (30 Pts)

With your code from Part 1, now use it against a live server spitting out random
hashes that need to be cracked! The hashes will be the same format as in Part 1,
but will be randomized. You only need to correctly crack 3 hashes in succession
in order to get the flag. The program is available via `nc 134.209.128.58 1337`.
Write your code in `writeup/server_crack.py`.

#### Important notes

Make sure to submit **all** of the code you write!

### Scoring

For Part 1, full points will be granted for a Python3 script that reads in the hash and
password files, cracks each hash, and prints the correct input-hash pairs.
Points will be deducted for not reading in the files, or not implementing a hash
cracker.

For Part 2, full points will be granted for a working script that correctly
interacts with the server to retrieve the flag, while reading in the
passwords.txt file.

### Tips

In Part 1, a common source of error is not stripping off the newline characters
after reading in each line of the file. You will fail to find the correct input
corresponding to each hash if you keep the newline character on each password
before you prepend a character and hash it, or compare this hash to one in the
hash file that still has the newline character.

In Part 2, a common source of error is sending data too fast before the server
gets a chance to respond, causing the program to "hang." A simple fix would be
to `import time` and use `sleep.time()` to introduce a bit of controlled delay
to help alleviate this problem.
