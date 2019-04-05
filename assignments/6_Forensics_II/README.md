# Forensics II

## Assignment details

This assignment has two parts. It is due by 4/4/19 at 11:59PM.

**There will be a late penalty of 5% per day late!**

### Part 1 (45 Pts)

One of 1337bank.money's network engineers recently discovered that a hacker has been attempting to steal (and potentially has already stolen) sensitive documents on their server. They have reached out the infamous CMSC389R hackers for help!

The network engineer has saved all network traffic from the intrusion. Can you analyze it for us and answer the following questions?

[netlog.pcap](netlog.pcap)

1. Warmup: what IP address has been attacked?

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

3. What are the hackers' IP addresses, and where are they connecting from?

4. What port are they using to steal files on the server?

5. Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,

    a) What kind of file is it?

    b) Where was this photo taken? Provide a country and city in your answer.

    c) When was this photo taken? Provide a timestamp in your answer.

    d) What kind of camera took this photo?

    e) How high up was this photo taken? Provide an answer in meters.

6. Which file did the attackers leave on the server?

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.

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
    2. Who authored `greetz.fpff`?
    4. List each section, giving us the data in it *and* its type.
    5. Report *at least* one flag hidden in `greetz.fpff`. Any other flag found will count as bonus points towards the *competition* portion of the syllabus.

#### Important notes

Make sure to submit **all** of the code you write, even if based on `stub.py`!

### Scoring

This assignment is worth 100 points, broken down between the pcap findings (25 points), and fpff parser (50 points) and question answering/analysis (25 points).

### Tips

Remember to document your steps for maximum credit. We want to know how you approached and solved this challenge!

Look at the Forensics I and II slides for guidance.

If you're using Python, Ruby, or another scripting language, check out the `pack` and `unpack`
methods:

* Python 2 - [`struct`](https://docs.python.org/2/library/struct.html)
* Python 3 - [`struct`](https://docs.python.org/3.5/library/struct.html)
* Ruby - [`Array#pack`](https://ruby-doc.org/core-2.5.0/Array.html#method-i-pack) and
[`String#unpack`](https://ruby-doc.org/core-2.5.0/String.html#method-i-unpack)
