# Crypto II

## Assignment details

This assignment has two parts. It is due by 5/3/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (70 Pts)

You stumbled upon a [GPG key](key.asc), and an encrypted file called
[`message.txt.gpg`](message.txt.gpg)

Your task is to use this key to decrypt the file, and then follow the directions
written inside the file. You *must* use the command line tools `gpg` and
`openssl` for this task, or you will not receive *any* credit.

### Part 2 (30 Pts)

You are given an [image](original.bmp).

Encrypt this file with AES-128 encryption in ECB mode with this command:
`openssl enc -aes-128-ecb -e -in original.bmp -out ecb.bmp -K 00112233445566778899aabbccddeeff`

Next, encrypt this file with AES-128 encryption in CBC mode with this command:
`openssl enc -aes-128-cbc -e -in original.bmp -out cbc.bmp -K 00112233445566778899aabbccddeeff -iv 00000000000000000000000000000000`

Encrypt the image with the AES128 algorithm in ECB mode with the `openssl`
command line tool, and name it `ecb.bmp`. Next, encrypt the image with the
AES128 algorithm in the same way but in CBC mode, and call it `cbc.bmp`. Run
[this script](fix.sh) in order to patch the headers of both files so
they may be viewed as images, then embed both pictures in your writeup.

Answer these questions:

1. What do you notice about both pictures?
2. Which block cipher mode is less secure? Why? Explain using information about
   how the different block cipher modes of operation work.

#### Important notes

Make sure to submit **all** of the code you write, if any!

### Scoring

Your writeup **folder** should include

* original.bmp
* ecb.bmp
* cbc.bmp

as well as any other particular files mentioned in message.txt.gpg after
encrypting and following its instructions. Copy over existing files if
necessary.

For Part 1, half credit will be granted for importing the key and showing proof
that it is imported to the keychain. Full credit will be granted for
additionally following the steps mentioned in the encrypted message.

For Part 2, 10 points will be granted for encrypting the original picture twice
and including each file in your writeup, with the correct filenames. 10 points
will be granted for answering each question.

### Tips

Use any available documentation on how to use the commands mentioned in class.
This includes the lecture slides as well as the `man` pages.
