# Writeup 3 - Operational Security and Social Engineering

Name: Alex Bloch
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Alex Bloch

## Assignment Writeup

### Part 1 (40 pts)
To get this information out of Elizabeth, I will track down her insurance information and pose as a customer support agent for her insurance company. 
I will call her and tell her that there’s a security issue with her account and she will need to confirm various pieces of information to confirm her identity. I will lead with asking what browser she last used, and then say the attacker used a different browser with a foreign IP address. 
Then I will ask her to confirm her mother's maiden name, city of birth and first pet’s name. 
Finally I will ask her to set up a pin to secure her account, which I will assume to be the same as her bank pin. I would then stay on the line for a bit to avoid suspicion. 

### Part 2 (60 pts)

Part 2:
Weak password:
The password used on the website is very insecure. It is short, and only uses lowercase letters, in addition to being on a list of commonly used passwords. 
To remedy this I would recommend using a password manager. Password managers auto generate and store secure passwords, so you can use secure passwords without needing to memorize them.

Open port:
Port 1337 is open on the website, which allows anyone to access the port. This could be solved by installing a firewall, that could, for example, limit access to only one IP address. 
This would add an extra layer of security while still allowing the user access to the port.

Easy to find username:
The username used for the login prompt on the website is used in various other places around the internet. 
This made the login prompt easier to brute force as there was only one plausible username. Using a unique username would go a long way in making the prompt harder to access.
