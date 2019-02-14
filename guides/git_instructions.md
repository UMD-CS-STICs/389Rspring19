# Homework Submission and Clone Repository Instructions

## Overview
Homework assignment and submission for this class will be handled through GitHub. This is meant as a way to teach and familiarize you with git software, as well as build a portfolio of cybersecurity writeups on your personal GitHub accounts. We will be running scripts that automatically retrieve your homeworks, and grades will be assigned through [ELMS](https://myelms.umd.edu/courses/1261976).

This guide covers how to setup the GitHub **and** local repositories you will need for this class. Please pay careful attention to the mention of *class* repository versus *personal* repository in this guide.

We recommend you follow this guide and use git from within your Kali VM.

## Getting Started
If you don't already have a GitHub account, you will have to create one. You can do this [here](https://github.com/).
1. After creating a GitHub account, the first thing you need to do is set your local git configuration to match it.
    - Type the following commands in your terminal, replacing the fillers with your information (keep the quotes!)
    - **You should use the same name and email you used to create your GitHub account**
    ```
    git config --global user.name "YOUR NAME HERE"
    git config --global user.email "YOUR EMAIL HERE"
    ```

2. Now you need to copy our [class repository](https://github.com/UMD-CS-STICs/389Rspring19) into your own personal GitHub repository.
    - Click the above link and look for the button in the top right corner that says "fork."
    - Click the "fork" button and wait a few seconds, GitHub should create a new repository on your account that's identical to our class repository.

## Creating a local repository to push and pull assignments from
Now you have a personal copy of the class repository. You need to download it so you can make changes on your computer and then re-upload them. Downloading and re-uploading through git is called *pulling* and *pushing*.

You need to *pull* changes from our class repository every week as we upload new lecture slides and assignments. When you complete the assignments, you'll need to *push* them to your personal copy of the repository on GitHub.

1. In your terminal, navigate to a directory where you want to copy your personal repository.
    - Execute the following command, replacing \<GitHub Username> with your GitHub username.
    ```
    git clone https://github.com/<GitHub Username>/389Rspring19
    ```

2. Once the repository is cloned, cd into its directory. We need to add our class repository as a remote for pulling data.
    - Execute the following command:
    ```
    git remote add upstream https://github.com/UMD-CS-STICs/389Rspring19
    ```

3. Confirm that the previous command was successful by executing the following command.
    - This command should output 4 lines, a *fetch* and a *push* for "origin" and "upstream"
    ```
    git remote -v
    ```

***You only need to do everything above this line once, at the beginning of the semester. The remaining instructions need to be done every week to obtain the new slides and assignments.***
    
# Pulling data from the class repository before starting your homework
As mentioned, you will need to do this every week to grab the latest assignments from our class repository. You must have completed all of the above steps for this to work.

1. The first thing you need to do is grab the new things we've uploaded to the class repository.
    - Use the following command to pull our changes into your local personal repository:
    ```
    git fetch upstream
    ```

2. Once you see the output describing that you've pulled some files, you need to merge what you've just downloaded into your repository.
    - The following command will add everything new that you don't already have into your local repository:
    ```
    git merge upstream/master -m "pull new assignment"
    ```

You should now have the new assignments, or whatever it is we uploaded to the class repository, in your local personal repository. You can now edit the new files as you please and upload them to your personal repository on GitHub.

# Pushing your completed homework to your personal repository
Once you've pulled the assignment down from the class repository, you're free to edit it on your own system. You'll notice that our writeup templates are writen in MarkDown language. You should edit them directly; MarkDown is a useful language to learn. If you want to add in extra files or screenshots, you can simply copy them into the same folder as the assignment and reference them in your writeup file.

Once you've completed your assignment and copied any extra files you want us to see into the assignment directory, you're ready to push your changes to GitHub so we can see them.

1. First you need to stage your changes so that git knows what you want to push.
    - Enter the following command to add all new/edited files:
    ```
    git add .
    ```

2. Once your changes have been staged, you need to define a commit to describe the changes.
    - Enter the following command to create a commit; you can change the message in quotations as you please.
    ```
    git commit -m "completed assignment 1"
    ```

3. Finally, once your changes have been staged and committed, you can push them to your personal GitHub repository.
    - Enter the following command. It will prompt you for your GitHub username and password, which you should enter.
    ```
    git push
    ```

That's it! Remember to fetch from upstream every week to obtain our changes from the class repository, and remember to push your homework to your personal GitHub repository before any deadlines!
