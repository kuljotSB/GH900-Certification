## Lab – Git Basics: Clone, Commit, and Create Your First Pull Request

### Scenario
You are contributing to a shared GitHub repository for the first time.
Your task is to clone the repository, make a small change locally, and submit it back using a Pull Request (PR).

This lab introduces core Git commands and the standard GitHub collaboration workflow.

---

### Lab Objectives
By completing this lab, you will be able to:
- Clone a GitHub repository
- Use basic Git commands to track changes
- Create your first commit
- Submit a Pull Request to the main repository

### Step 1 - Cloning the Repository

1. Open your terminal or Git Bash.
2. Clone the repository using the command:
   ```
   git clone <repository-URL>
   ```

### Step 2 - Modify the contributors.txt File

1. Navigate into the cloned repository:
   ```
   cd <repository-name>
   ```
2. Open the `contributors.txt` file in a text editor.
3. Add your name to the list of contributors.
4. Save and close the file.

### Step 3 - Stage and Commit Your Changes

1. Change branch to a new feature branch:
   ```
   git branch -m add-contributor
   git checkout add-contributor
   ```
2. Stage the modified file:
   ```
    git add contributors.txt
    ```
3. Commit your changes with a descriptive message:
    ```
    git commit -m "Added my name to contributors.txt"
    ```

### Step 4 - Push Changes to the Main Repository

1. Push your changes to the remote repository:
   ```
   git push -f origin add-contributor
   ```  

### Step 5 - Create a Pull Request

1. Go to the GitHub repository in your web browser.
2. You should see a prompt to create a Pull Request for your recently pushed branch. Click on "Compare & pull request".
3. Add a title and description for your Pull Request.
4. Click on "Create pull request" to submit your changes for review.


### Some Helpful Git Commands
- `git status`: Check the status of your working directory and staging area.
- `git log`: View the commit history.
- `git diff`: See the changes made to files before committing.

### Conclusion
Congratulations! You have successfully cloned a repository, made changes, committed them, and created your first Pull Request on GitHub.