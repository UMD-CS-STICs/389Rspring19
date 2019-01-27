# CMSC389R: Introduction to Ethical Hacking (HackTheClass)
![HackTheClass](HackTheClass.png)

## Course Description
This practical, hands-on [1-credit course](http://sticsumd.com/) provides students with an introduction to ethical hacking. The course begins with a discussion on the ethics behind security research and progresses to topics that surround penetration testing, forensics, cryptology, and binary reverse engineering and exploitation. This course is also meant to introduce students to Capture-the-Flag (CTF) style cybersecurity challenges, encourages participation in UMD's Cybersecurity Club ([UMDCSEC](https://csec.umd.edu)), and prepares for CMSC414.


## Course Details
- **Course**: [CMSC389R](https://testudo.umd.edu)
- **Prerequisites**: C- or better in CMSC216 and CMSC250
- **Credits**: 1
- **Seats**: 30, 2 sections
- **Lecture Time**: Fridays, 2-2:50 PM (0101) and 3-3:50 PM (0201)
- **Location**: CSI 2118
- **Semester**: Spring 2018
- **Textbook**: None
- **Course Facilitators**: [Michael Reininger](https://www.github.com/1umpus), [Joshua Fleming](https://github.com/jsfleming), [Wesley Weidenhamer](https://github.com/wesley27) and [Mike Bailey](https://github.com/Miskerest)
- **Faculty Advisor**: [Dave Levin](http://www.cs.umd.edu/~dml/)
- **Syllabus Last Updated**: January 26, 2019

## Topics Covered
- Security research ethics
    - Cyberlaw
    - Responsible disclosure
    - Expectation of privacy
- Linux
    - Command line
    - Configuring an environment
    - Virtual machines
- Target reconnaissance
    - OSINT
    - Social engineering
    - OPSEC
- Penetration testing
    - Vulnerability scanning
    - Using automated tools
    - Maintaining persistence
- Forensics
    - Imaging
    - File types and carving
    - Metadata
    - File system artifacts
    - Password cracking
    - Network captures
    - Steganography
- Binaries
    - Reverse engineering
    - Stack-based buffer overflow
    - Shellcode
- Web
    - Javascript deobfuscation
    - SQL injection
    - XSS & CSRF
- Crypto
    - Classic ciphers
    - Symmetric and asymmetric key
- CTF
    - Jeopardy vs Attack-Defense
    - Write-ups

## Grading
Grades will be maintained on the CS Department <a href="https://grades.cs.umd.edu/">grades server</a>.

You are responsible for all material discussed in lecture and posted on the class repository, including announcements, deadlines, policies, etc.

Your final course grade will be determined according to the following percentages:

| Percentage | Title | Description |
| ------------- | -----|-------- |
| 55% | Write-ups  | Weekly individual write-ups (250-500 words) that summarize the lecture and assigned CTF challenges. |
| 20% | Midterm | Examination on topics covered until Forensics II. |
| 25% | Final Hack | Demonstrate mastery of all topics learned and apply knowledge to change your grade on the class's private grade server. The grade earned will be determined by levels unlocked in the grade server and will be applied to your official final grade. |

Any request for reconsideration of any grading on coursework must be submitted within one week of when it is returned. No requests will be considered afterwards.

## Schedule

| Week | Topic | Assignment |
| ----|----|----- |
| 1 (2/1) | [Introduction + Ethics 1](week/1/Introduction.pdf) | Download [VirtualBox](https://www.virtualbox.org/), [Kali](https://www.kali.org/). [Gray Hat Hacking (Ch. 1)](https://archive.org/details/GrayHatHackingTheEthicalHackersHandbook3rdEdition). [OSINT Handbook](http://www.i-intelligence.eu/wp-content/uploads/2016/11/2016_November_Open-Source-Intelligence-Tools-and-Resources-Handbook.pdf). [OPSEC](http://opsec.readthedocs.io/en/latest/). |
| 2 (2/8) | [Ethics 2 + OSINT 1](week/2/OSINT.pdf) | [Challenges.](week/2/challenges/README.md) Write-up 1. [Kali VM installation instructions](week/2/kali_instructions.pdf)|
| 3 (2/15) | [OSINT 2 + Vulnerability scanning](week/3/OSINT2-Vulnerability-Scanning.pdf) | [Challenges.](week/3/challenges/README.md) Write-up 2. |
| 4 (2/22) | [Penetration testing I](week/4/Pentesting-1.pdf) | [Challenges.](week/4/challenges/README.md) Write-up 3. |
| 5 (3/1) | [Penetration testing II](week/5/Pentesting-2.pdf) | [Challenges.](week/5/challenges) Write-up 4. |
| 6 (3/8) | [Forensics I](week/6/Forensics-1.pdf) | [Challenges.](week/6/challenges) Write-up 5. |
| 7 (3/15) | Midterm | Start of spring break. |
| 8 (3/22) | [Forensics II](week/7/Forensics-2.pdf) | [Challenges.](week/7/challenges) Write-up 6. |
| 9 (3/29) | [Cryptography I](week/9/Crypto-1.pdf) | [Challenges.](week/9/challenges) Write-up 7.|
| 10 (4/5) | [Cryptography II](week/10/Crypto-2.pdf) | [Challenges.](week/10/) Write-up 8.|
| 11 (4/12) | [Web](week/11/Web.pdf) | [Challenges.](week/11/challenges) Write-up 9. |
| 12 (4/19) | [Binaries I](week/12/Binaries-1.pdf) | [Challenges.](week/12/challenges) Write-up 10. |
| 13 (4/26) | [Binaries II](week/13/Binaries-2.pdf) | [Challenges.](https://github.com/UMD-CS-STICs/389Rspring18/tree/master/week/13) Write-up 11. |
| 14 (5/3) | [Wrap-up](https://github.com/UMD-CS-STICs/389Rspring18/tree/master/week/14) | Final hack. |

The timeline is not final and can be subject to change.

## Communicating with course staff

Outside of class interaction between students and course staff will occur via piazza.
Email should only be used for emergencies and not class related questions.

Instructor:

Dr. Dave Levin - dml@cs.umd.edu

TAs:

Michael Reininger - michael@csec.umiacs.umd.edu

Joshua Fleming - secretary@csec.umiacs.umd.edu

Wesley Weidenhamer - wesley@csec.umiacs.umd.edu

Mike Bailey - misker@protonmail.com

## Excused Absence and Academic Accommodations
See the section titled <a href="http://www.ugst.umd.edu/courserelatedpolicies.html">Course Related Policies</a>.

## Disability Support Accommodations
See the section titled "Accessibility" available at <a href="http://www.ugst.umd.edu/courserelatedpolicies.html">Course Related Policies</a>.


## Academic Integrity
Note that academic dishonesty includes not only cheating, fabrication, and plagiarism, but also includes helping other students commit acts of academic dishonesty by allowing them to obtain copies of your work. In short, all submitted work must be your own. Cases of academic dishonesty will be pursued to the fullest extent possible as stipulated by the <a href="http://osc.umd.edu/OSC/Default.aspx">Office of Student Conduct</a>.

It is very important for you to be aware of the consequences of cheating, fabrication, facilitation, and plagiarism. For more information on the Code of Academic Integrity or the Student Honor Council, please visit http://www.shc.umd.edu.


# Course Evaluations
If you have a suggestion for improving this class, don't hesitate to tell the instructor or TAs during the semester. At the end of the semester, please don't forget to provide your feedback using the campus-wide CourseEvalUM system. Your comments will help make this class better.

###### Thanks to the writers of <a href = "https://github.com/UMD-CS-STICs/389Kfall17">this</a> syllabus for the wording of much of this document.
