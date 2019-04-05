# Binaries I

## Assignment details

This assignment has two parts. It is due by 4/12/19 at 11:59PM.

**There will be a late penalty of 5% per day late!**

### Part 1 (90 Pts)

There is an assembly file called [main.s](main.s) in this folder, which is an
excerpt from a compiled C program. Using what you've learned about x86-64
assembly, translate the code into an equivalent C program. Remember to take note
for x86-64 calling conventions, specifically the order for a function's
arguments and which registers correspond to said arguments.

One caveat not mentioned in lecture is that functions that take in variadic
arguments (e.g. `printf`) require one to note how many vector registers are used
(e.g. xmm0, xmm1, etc) into `rax`. Typically these are only used for passing
floating point arguments to a function. In our case, if a call to `printf`
doesn't use any floating point numbers, we can just load `0` into `rax`.

The name of the game is **static analysis**, where you analyze a binary by
reading off of the assembly. We don't really want you to try and assemble and
run the binary to analyze it's behavior just yet, as we'll save **dynamic
analysis** for next week.

### Part 2 (10 Pts)

In a sentence or two, state what the program achieves. Don't say that the
program executes X or Y instructions and prints stuff, but rather say what these
instructions achieve.

#### Important notes

Make sure to submit **all** of the code you write!

### Scoring

For Part 1, full points will be granted for C programs that compile and run on a
Kali Linux environment. Partial credit will be granted if the program conveys
the gist of assembly.

For Part 2, full points will be granted for correctly stating what the program
achieves. No partial credit will be granted.

### Tips


Look at the Binaries I slides for guidance.

If there's an assembly instruction that wasn't covered in the lecture slides,
don't worry! There's *way* too many instructions that can be run on Intel CPUs
to fit in a lecture, many of which aren't used that often. You can look up what
an instruction does [here](https://www.felixcloutier.com/x86/). Posting on
Piazza for help is fine too!
