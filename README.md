# Task_manager2

In the previous Capstone project, Task_manager, I created a simple task management system that stored data in text files. In this project, I used lists or dictionaries and functions to extend the functionality of your previous Capstone Project.

I created a copy of your previous Capstone project (task_manager.py). Also I created a copy of files (user.txt and tasks.txt) that accompanied the previous Capstone project to this folder. In this task modified this program.

in this task I allowed the user to select either a specific task (by entering a number)or input ‘-1’ to return to the main menu. If the user selects a specific task, they should be able to choose to either mark the task as complete or edit the task. If the user chooses to mark a task as complete, the ‘Yes’/’No’ value that describes whether the task has been completed or not should be changed to ‘Yes’. When the user chooses to edit a task, the
username of the person to whom the task is assigned or the due date of the task can be edited. The task can only be edited if it has not yet been completed.

I also added an option to generate reports to the main menu of the application. The menu for the admin user should now look something like this:

Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit

When the user chooses to generate reports, two text files, called
task_overview.txt and user_overview.txt, should be generated. Both
these text files should output data in a user-friendly, easy to read manner.

task_overview.txt should contain:
 
 ▪ The total number of tasks that have been generated and
  tracked using the task_manager.py.
  ▪ The total number of completed tasks.
  ▪ The total number of uncompleted tasks.
  ▪ The total number of tasks that haven’t been completed and
  that are overdue.
  ▪ The percentage of tasks that are incomplete.
  ▪ The percentage of tasks that are overdue.

user_overview.txt should contain:
  
  ▪ The total number of users registered with task_manager.py.
  ▪ The total number of tasks that have been generated and
  tracked using task_manager.py.
  ▪ For each user also describe:
  ▪ The total number of tasks assigned to that user.
  ▪ The percentage of the total number of tasks that have
  been assigned to that user
  ▪ The percentage of the tasks assigned to that user that
  have been completed
  ▪ The percentage of the tasks assigned to that user that
  must still be completed
  ▪ The percentage of the tasks assigned to that user that
  have not yet been completed and are overdue
 
I modified the menu option that allows the admin to display statistics so that the reports generated are read from task_overview.txt and user_overview.txt and displayed on the screen in a user-friendly manner. If these text files don’t exist (because the user hasn’t selected to generate
them yet), first call the code to generate the text files
