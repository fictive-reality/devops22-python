# Git Commands

## To merge from terminal
- git pull origin master
- git checkout master
- git merge AlexRoman
- git push -u origin master


## Git Cheat Sheet
- Git [cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)

## The way i doit

- ls
- mkdir -p directory
- cd directory
- git init
- git clone git_link
- git status
#### From here it starts to be confusing because i'm not sure yet if i should branch directly after the initial commit or i can branch directly and get the initial commit from my branch
- git add -A
- git commit -m "Initial commit"
- git branch
- git branch AlexRoman
- git switch AlexRoman
- git status
#### Importing the folder in VSC and start working
- git status
- git add -A
- git commit -m "New changes"
- git push (but maybe i should do the merge locally and then push to github)


## New things learned from youtube
- git diff filename -- see the diferrences between files.
- git add -p filename -- you can see and aprove just parts of the changes.
- git commit -- and then add a message and then a empty line and then the body of the commit messsage.

## Some way
- git clone xxx
- cd the_folder_it_cloned/
- code -- for calling the editor
- git branch yourbranch -- add a new branch
- git checkout yourbranch -- go to your branch
- do your changes, add files and so on
- git add file or git add -A
- git push --set-upstream origin yourbranch
- and then on github i can pullrequest or see at the begining how to doit automatically from terminal
- the previous point needs some testing