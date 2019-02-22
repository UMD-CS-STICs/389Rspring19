OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Thursday, February 12 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `v0idcache`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `v0idcache` and answer the following questions:

1. What is `v0idcache`'s real name? Elizabeth Moffet

2. Where does `v0idcache` work? What is the URL to their website? She works at Elite Banking. http://1337bank.money/

3. List all personal information (including social media accounts, contacts, etc) you can find about `v0idcache`. For each, briefly detail how you discovered them.
Elizabeth is the CEO of the company.She lives in the Netherlands, according to her twitter account. I used usersearch.org to search the user tag 'v0idcache', which led me to the twitter account of Elizabeth.

4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
142.93.136.81 Canada
DNs 216.87.155.33 United States
216.87.152.33  '''
162.255.118.61
162.255.118.62
162.255.118.62
162.255.118.62
162.255.118.61

I used DnsDumpster to get this information

5. List any hidden files or directories you found on this website. For full credit, list *two* distinct flags.
User-agent: *
Disallow: /secret_directory
 CMSC389R-{h1ding_fil3s_in_r0bots_L0L}
 CMSC389R-{h1dd3n_1n_plain_5ight}
6. What ports are open on the website? What services are running behind these ports? How did you discover this?
22/tcp  ssh       
80/tcp  http  
1337    waste
I discovered the ports and services using nmap
7. Which operating system is running on the website? How did you discover this?
Werkzeug/0.14.1 Python/3.7.2
I used wget on the url 

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
 CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b}
### Part 2
username: v0idcache
password: linkinpark

### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, push it up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
