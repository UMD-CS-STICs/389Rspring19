# Writeup 6 - Forensics

Name: Alex Bloch
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Alex Bloch

## Assignment Writeup

1. Warmup: what IP address has been attacked?
142.93.136.81
2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.
Command line tools (question is kinda unclear but I think this is what it is asking), curl, 
3. What are the hackers' IP addresses, and where are they connecting from?
159.203.113.181 - Clifton NJ, 178.19.107.42 - Sidra Poland, 37.237.212.29 - Iraq
4. What port are they using to steal files on the server?
21
5. Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,
	find_me.jpeg
    a) What kind of file is it?
	jpeg
    b) Where was this photo taken? Provide a country and city in your answer.
		Punta Del Este / Maldonado, Uruguay
    c) When was this photo taken? Provide a timestamp in your answer.
	Sun 23rd of December 2018
    d) What kind of camera took this photo?
	Iphone8
    e) How high up was this photo taken? Provide an answer in meters.
	4.5
6. Which file did the attackers leave on the server?
	greetz.fpff
7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.
	Update the vsFTPd version
### Part 2 (55 Pts)

After looking at a file that you discovered in #6 above, we were unable to identify its file type or any program that can open it. Fortunately, our friends at UMDCSEC were able to dig up a file specification sheet for this file type! Can you write a parser for us and tell us what the file contains?

Here is file's spec sheet [here](fpff-spec.md). Once you write the parser, report back with what you've found!

Perform the following tasks:

1. Develop the parser, using both the
[specification](fpff-spec.md) and
`greetz.fpff` for reference. [stub.py](stub.py) contains the beginnings of a Python parser, if
you'd like to develop in Python.

2. Parse `greetz.fpff`, and report the following information:
    1. When was `greetz.fpff` generated?
	Wednesday, March 27, 2019 4:15:05 AM
    2. Who authored `greetz.fpff`?
1848732774 or n1lf. Not sure if i converted to ascii correctly
    4. List each section, giving us the data in it *and* its type.
	format for sections and data is not specified, so I will list them in hex:
section
0x1
data
0x18
section
0x20796548
data
0x2c756f79
section
0x65656b20
data
0x6f6c2070
section
0x6e696b6f
data
0x293a2067
section
0x6
data
0x10


    5. Report *at least* one flag hidden in `greetz.fpff`. Any other flag found will count as bonus points towards the *competition* portion of the syllabus.
	CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R
#### Important notes


