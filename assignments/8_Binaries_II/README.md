# Binaries II

## Assignment details

This is an extra credit assignment with one part. It is due by 5/14/19 at
11:59PM.

**There will be no late submissions accepted!**

### Part 1 (100 Pts)

The binary [`locker`](locker) requires a flag to be entered. Find the flag, and
prove that it works. Run `./locker <flag>` and type `echo $?`, and take a
screenshot as proof. `echo $?` prints the exit code of the last running program,
and a working flag should print 0. Any other flag will cause `locker` to return
-1 (or 255). The flag follows the standard format of `CMSC389R-{...}`.

Along with the flag, document the steps you took to analyze the binary. What did
you do first? What second? Which tools did you use, and which ones were the most
or least helpful? Anything you found straight forward? Anything catch you
off-guard? These are just examples of some questions that may help you guide
your documentation, but it is not an exhaustive list. A fellow classmate
familiar with x86-64 assembly should be able to read this reflection and know
exactly what to do to solve the binary. Any notes, typed or handwritten, can be
pushed to your git repo and embedded in your writeup to help supplement your
analysis and explanation.

### Scoring

Full points will be granted with the correct flag, screenshot, and reflection.

If submitted, the grade for this assignment can used to replace the lowest
grade for any previous assignment.

### Tips

Look at the Binaries I and Binaries II slides for guidance. 

IDA Pro's [Quick Reference
Sheet](https://www.hex-rays.com/products/ida/support/freefiles/IDA_Pro_Shortcuts.pdf)
may come in handy. The hotkeys `N` to rename, `;` to write line comments, and
`Insert` to write block comments may be the most useful. Right clicking on
immediate values and selecting "Manual..." may help with representing numerical
data in more useful ways.

If there's an assembly instruction that wasn't covered in the lecture slides,
don't worry! There's *way* too many instructions that can be run on Intel CPUs
to fit in a lecture, many of which aren't used that often. You can look up what
an instruction does [here](https://www.felixcloutier.com/x86/). Posting on
Piazza for help is fine too!

### Hint

A specific tool reviewed in class probably won't work when analyzing this binary.
