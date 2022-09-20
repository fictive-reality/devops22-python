# Team Git Practice 

**25 min**

Let's practice using Git in a team environment to help us better prepare for development in a professional setting.

This shows a scenario where each developer creates their own features in separate branches and use Pull Request to get the changes approved by a release manager. This is realistic in a work setting but may be complicated or unnecessary when working closely in a course group project, so decide for yourself which process you will use to work together.

## Preparation

Split up into teams of 3-4. If You're in a group of 3, then the Release Manager will also play the role of Developer 3.

 * Release Manager - Responsible for managing the remote repository, merging branches
 * Developer 1
 * Developer 2 
 * Developer 3

The person who should be following a series of steps will be marked like ``` DEVELOPER 1 ```. It's suggested you all sit together with your computers while doing this excersise.

## Exercise 

#### RELEASE MANAGER

1. Create a private repository in your GitHub account
2. Add the 2-3 additional developers in your team as Collaborators (use their Github usernames or emails)

#### EVERYONE

1. Clone the newly created repository to your computer. Before you clone, make sure you are in good folder - you should NOT be inside another Git repository such as devops22-python, and you should PROBABLY be in the folder you created for all your code.
2. In the terminal, navigate to the working directory you just cloned.

#### DEVELOPER 1

1. Create a new branch called ``` readme ``` and switch to it
2. Create a file named ``` README.md ```
3. Write some basic information on what your group project will do
4. Stage the file for your next commit 
5. Commit the file 
6. **Stop and Think**: Do the other developers have access to the file you created yet? 
7. Push the branch to the remote repository
8. Create a pull request, either by clicking the link that is shown in terminal after pushing, or by going to GitHub, and it will show a yellow banner at the top that offers you to create a PR from `readme` to `main`

#### RELEASE MANAGER

1. Go to GitHub and view the repository you created for your team
2. On the right hand side click on "Pull requests"
3. Review the changes being proposed by Developer 1
4. If they look good, approve the changes by merging the new ``` readme ``` branch into ``` main ```

#### DEVELOPER 2

1. Pull down the latest changes from the remote repository
2. Create a new branch named ``` teamname ``` and switch to it
3. We need to make sure we add a team name to the readme. Add some text into ```README.md``` that shows the team name.
4. Stage your changes for the next commit
5. Commit your changes
6. Push the branch to the remote repository and create a pull request into `main`

#### RELEASE MANAGER

1. Go to GitHub and view the repository you created for your team
2. On the right hand side click on "Pull requests"
3. Review the changes being proposed by Developer 2
4. If they look good, approve the changes by merging the new ``` teamname ``` branch into ``` main ```

#### DEVELOPER 3

1. Pull down the latest changes from the remote repository
2. Create a new branch named ``` teamimage ``` and switch to it
3. Your job is to add an image that represents your team, put it next to the `README.md`.
4. Change the README.md to include a reference to the image (Google how to show image in Markdown)
5. Stage your changes for the next commit
6. Commit your changes
7. You think you have a much better team name. Without asking the others, change the team name in `README.md` to "Justin Bieber's Fan Club".
8. Stage your changes for the next commit
9. Commit your changes
10. Push the branch to the remote repository and create a pull request

#### RELEASE MANAGER

1. Go to GitHub and view the repository you created for your team
2. On the right hand side click on "Pull requests"
3. Review the changes being proposed by Developer 3
4. You don't notice the error with the team name, so just approve the changes by merging the new ``` teamimage ``` branch into ``` main ```

#### DEVELOPER 1

1. Your notice that the team name has changed to something that's not correct. Developer 3 is on vacation and cannot explain the choice, so you're tasked to fix this
2. Pull down the latest changes from the remote repository
3. Create a new branch named ``` hotfix1 ``` and switch to it
4. Correct the team name 
5. Stage your changes for the next commit
6. Commit your changes
7. **DO NOT** push your changes to the remote repository yet

#### DEVELOPER 2

1. Let's pretend Developer 2 is working in parallell with Developer 1.
2. Pull down the latest changes from the remote repository
3. Create a new branch named ``` teamname_update ``` and switch to it
4. Your manager asked you to make the team name all uppercase, so go ahead and do that.
5. Stage your changes for the next commit
6. **DO NOT** commit your changes or push them to the remote repository yet

#### DEVELOPER 1

1. You are back from lunch. Push the ``` hotfix1 ``` branch to the remote repository and create a pull request

#### RELEASE MANAGER

1. Go to GitHub and view the repository you created for your team
2. On the right hand side click on "Pull requests"
3. Review the changes being proposed by Developer 1
4. Approve the changes by merging the new ``` hotfix1 ``` branch into ``` main ```

#### DEVELOPER 2

1. Switch to the ``` main ``` branch
2. Pull down the latest changes from the remote repository
3. You noticed some files have changed, and you want the new branch you're working on to also have these changes
4. Switch to the existing ``` teamname_update ``` branch that you're still working on
5. Run ``` git merge main ``` to get those updates from main into `teamname_update`
6. You should have a conflict now with the new changes clashing with yours. Resolve these conflicts so that the team name is uppercase and also correct.
7. Stage your changes for the next commit
8. Commit your changes
9. Push the branch to the remote repository and create a pull request

#### RELEASE MANAGER

1. Go to GitHub and view the repository you created for your team
2. On the right hand side click on "Pull requests"
3. Review the changes being proposed by Developer 2
4. Approve the changes by merging the new ``` teamname_update ``` branch into ``` main ```

#### DEVELOPER 3

1. Pull down the latest changes from the remote repository
2. Create a new branch named ``` hotfix2 ``` and switch to it
3. You really want the team name to change again. Change it back to that again
4. Stage your changes for the next commit
5. Commit your changes
6. Push the branch to the remote repository and create a pull request

#### RELEASE MANAGER

1. Go to GitHub and view the repository you created for your team
2. On the right hand side click on "Pull requests"
3. Review the changes being proposed by Developer 3
4. This time, you learned your lesson and instead of merging you leave a comment about how this is incorrect and just close the request without merging.
5. Ask Developer 3 to stop doing this, or at least to discuss them before pushing, and tell them there's more to life than Justin Bieber 😊

