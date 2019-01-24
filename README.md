# CMSC389R: Introduction to Ethical Hacking (HackTheClass)
![HackTheClass](HackTheClass.png)

## Course Description
This practical, hands-on [1-credit course](http://sticsumd.com/) provides students with an introduction to ethical hacking. The course begins with a discussion on the ethics behind security research and progresses to topics that surround penetration testing, forensics, cryptology, and binary reverse engineering and exploitation. This course is also meant to introduce students to Capture-the-Flag (CTF) style cybersecurity challenges, encourages participation in UMD's Cybersecurity Club ([UMDCSEC](https://csec.umd.edu)), and prepares for CMSC414.


## Course Details
- **Course**: [CMSC389R](https://app.testudo.umd.edu/soc/search?courseId=cmsc389r&sectionId=&termId=201901&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on)
- **Prerequisites**: C- or better in CMSC216 and CMSC250
- **Credits**: 1
- **Seats**: 60, (30/section)
- **Lecture Time**: Fridays, 1-1:50 PM (0101) and 2-2:50 PM (0201)
- **Location**: CSI 2118
- **Semester**: Spring 2019
- **Textbook**: None
- **Course Facilitators**: [Michael Reininger](https://www.github.com/1umpus), [Wesley Weidenhamer](https://github.com/wesley27), [Joshua Fleming](https://github.com/jsfleming), and [Michael Bailey](https://github.com/Miskerest)
- **Faculty Advisor**: [Dave Levin](http://www.cs.umd.edu/~dml/)
- **Syllabus Last Updated**: January 23, 2019
- **Previous Offering**: [Spring 2018](https://github.com/UMD-CS-STICs/389Rspring18), [Fall 2018](https://github.com/UMD-CS-STICs/389Rfall18)

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
    - Network packet captures
    - Steganography
- Binaries
    - Reverse engineering
    - Stack-based buffer overflow
- Web
    - Javascript deobfuscation
    - SQL injection
    - XSS
- Cryptography
    - Classic ciphers
    - Symmetric and asymmetric key
    - Hash-length extension attacks
    - Password cracking
- Capture the Flag (CTF)
    - Jeopardy vs Attack-Defense
    - Write-ups and Proof-of-Concept (PoC)

## Grading
Assignments should be submitted through your personal fork of our class repository. Instructions on how to set this up and do it can be found [here](HW_Submit_Instructions.md).

Grades will be released through ELMS.

You are responsible for all material discussed in lecture and posted on the class repository, including announcements, deadlines, policies, etc.

Your final course grade will be determined according to the following percentages:

| Percentage | Title | Description |
| ------------- | -----|-------- |
| 50% | Write-ups  | Weekly individual write-ups (250-500 words) that summarize and explain your solutions to the assigned CTF challenges or concepts covered in lecture. |
| 20% | Midterm | Examination on topics covered until Forensics II. |
| 30% | Final Hack | Demonstrate mastery of all topics learned and apply knowledge to change your grade on the class's private grade server. The grade earned will be determined by levels unlocked in the grade server and will be applied to your official final grade. 

Any request for reconsideration of any grading on coursework must be submitted within 36 hours  of when it is returned. No requests will be considered afterwards.

Assignments may be submitted up to 3 days late for a 10%/day penalty.

## Schedule

| Week | Topic | Assignment |
| ----|----|----- |
| 1 (8/31) | [Introduction + Ethics 1](week/1/Introduction.pdf) | [Writeup 1](week/1), Download [VMWare](https://terpware.umd.edu), [Kali](https://www.kali.org/). [OSINT Handbook](https://www.i-intelligence.eu/wp-content/uploads/2016/11/2016_November_Open-Source-Intelligence-Tools-and-Resources-Handbook.pdf)
| 2 (9/7) |[Ethics 2 + OSINT 1](week/2/OSINT.pdf) | [Writeup 2](week/2), [Kali VM installation instructions](https://github.com/UMD-CS-STICs/389Rspring18/blob/master/week/2/kali_instructions.pdf)|
| 3 (9/14) | [OSINT II + Vulnerability scanning](https://github.com/UMD-CS-STICs/389Rfall18/blob/master/week/3/VulnerabilityScanning_OpSec_SE.pdf) | [Writeup 3](week/3) |
| 4 (9/21) | [Penetration testing I](week/4/Pentesting-1.pdf) | [Writeup 4](week/4) |
| 5 (9/28) | [Binaries I](week/5/Binaries%20I.pdf) | [Writeup 5](week/5) |
| 6 (10/5) | [Binaries II](week/6/Binaries-2.pdf) | [Writeup 6](week/6) |
| 7 (10/12) | [Forensics I](week/7/ForensicsI.pdf) | [Writeup 7](week/7) |
| 9 (10/19) | Midterm | |
| 10 (10/26) | [Forensics II](week/8/Forensics-II.pdf) | [Writeup 8](week/8) |
| 10 (11/2) | [Cryptography I](week/9/Crypto-1.pdf) | [Writeup 9](week/9) |
| 11 (11/9) | [Cryptography II](week/10/Crypto-2.pdf) | [Writeup 10](week/10) |
| 12 (11/16) | [Web I](week/11/Web.pdf) | [Writeup 11](week/11) |
| 13 (11/23) | Thanksgiving Break | |
| 14 (11/23) | [Web II](week/14/Web-2.pdf) | [Writeup 12](week/14) |
| 15 (11/30) | (Potential Guest Speaker or Demo Day) | |
| 16 (12/7) | [Wrap-up]() | Final hack. |

The timeline is not final and can be subject to change.

## Communicating with course staff

All official announcements will be sent through the course Piazza. Interaction between students and course staff will also occur via Piazza. Email should only be used for emergencies.

Office hours will be provided after class on Friday's from 3-4 PM. Course staff will remain in the classroom to answer questions and provide assistance as needed. Meetings can also be scheduled via Piazza.

Faculty Admin:

Dr. Dave Levin - dml@cs.umd.edu

Instructors:

Michael Reininger - michael@csec.umiacs.umd.edu

Wesley Weidenhamer - wesley@csec.umiacs.umd.edu

Joshua Fleming - president@csec.umiacs.umd.edu


## Excused Absence and Academic Accommodations
See the section titled <a href="http://www.ugst.umd.edu/courserelatedpolicies.html">Course Related Policies</a>.

## Disability Support Accommodations
See the section titled "Accessibility" available at <a href="http://www.ugst.umd.edu/courserelatedpolicies.html">Course Related Policies</a>.


## Academic Integrity
Note that academic dishonesty includes not only cheating, fabrication, and plagiarism, but also includes helping other students commit acts of academic dishonesty by allowing them to obtain copies of your work. In short, all submitted work must be your own. Cases of academic dishonesty will be pursued to the fullest extent possible as stipulated by the <a href="http://osc.umd.edu/OSC/Default.aspx">Office of Student Conduct</a>.

It is very important for you to be aware of the consequences of cheating, fabrication, facilitation, and plagiarism. For more information on the Code of Academic Integrity or the Student Honor Council, please visit http://www.shc.umd.edu.


# Course Evaluations
If you have a suggestion for improving this class, don't hesitate to tell the instructor or TAs during the semester. At the end of the semester, please don't forget to provide your feedback using the campus-wide CourseEvalUM system. Your comments will help make this class better.
