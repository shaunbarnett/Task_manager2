

# At this stage i am opening the file that i would like the program to read from to validate username and

# The following lines of code checks the user input and coverts to lowercase. if user inputs their correct username and
# password, they are though to the menu stage else they will be asked repeatedly for username and password until it is correc

task_generator = 6
def user_pwd():

    file = open("user.txt", "r")
    lines = file.readlines()
    user = input("\nPlease enter username: ").lower()
    pwd = input("\nPlease enter your password: ").lower()
    for line in lines:
        words = line.strip()
        words = words.split(", ")

        if words[0] == user:
            print("\nWelcome,", user)
            break

    else:
        print("\nYou have entered an incorrect username!")
        user_pwd()

    if words[1] == pwd:
        print("\nThank you, you are now authorised")
        main_menu(user)

    else:
        print("Incorrect password!")
        user_pwd()


# presenting the menu to the user and making sure that the user input is converted to lower case

def main_menu(user):

    menu = input('''\nSelect one of the following Options below:     
r - Registering a user (Admins only)                                            
a - Adding a task                                                  
va - View all tasks                                                
vm - view my task
gr - generate reports 
d - Display statistics (Admins only)                                                 
e - Exit                                                           
: \n''').lower()

# for option r, only admin can register a new user otherwise this service will be denied. username is entered then
# password is entered twice for confirmation and the two password entries must match! If so, a file will be opened to
# write to entries are username, comma. then a space followed by password. all inputs are converted to lowercase.

    if menu == 'r':
        if user == "admin":
            register_user()
        else:
            print("Sorry, you are not authorised")
            main_menu(user)
    elif menu == "a":
        add_task(task_generator, user)
    elif menu == "va":
        view_all_tasks(user)
    elif menu == "vm":
        view_my_tasks(user)
    elif menu == "gr":
        generate_reports(task_generator, user)
    elif menu == "d":
        if user == "admin":
            display_statistics()
        else:
            print("Sorry, you are not authorised")
            main_menu(user)
    elif menu == "e":
        end()
    else:
        print("Please enter valid option")
        main_menu(user)


def register_user():

    user = input("Please enter  username: ").lower()
    pwd = input("Please enter password: ").lower()
    confirm = input("Please re-enter password: ").lower()
    if pwd == confirm:
        file = open("user.txt", "a")
        file.write(f"\n{user}, {pwd}")
        file.close()
        print()
        print(user, "has been registered")
    else:
        print("Passwords do not match!")
        register_user()



# option a is where users can assign tasks for other users. The tasks are in the following order that it is written in
# task.txt file: username, title, description, due date and current date. User must be a current user in the user.txt
# file. User input is converted to lowercase

def add_task(task_generator, user):

        user_file = open("user.txt", "r")
        user_file2 = user_file.readlines()
        user_file.close()

        user = input("\nPlease enter the username of the person whom the task is assigned to: ").lower()
        title = input("Please enter a title for this task: ").lower()
        description = input("Please give a short description: ").lower()
        date = input("Please give the due date for this task: ").lower()
        current_date = input("Please enter thr current date: ").lower()

        x = []
        for u in user_file2:
            u = u.strip()
            u = u.split(", ")
            if user in u:
                file = open("tasks.txt", "a")
                file.write(f"\n{user}, {title}, {description}, {date}, {current_date}, No\n")
                file.close()
                print(f"\nYou have added the {title} task to {user}")

        else:
            print(f"\nSorry, user {user} is not recognised!")


def view_all_tasks(user):


    print(f"\nHello, {user} the tasks are in the following format:")
    print("Username,  Task,  description,  Date the task commences,  Today's date,  Task completed Y/N\n")

    read = open("tasks.txt", "r")
    file = read.readlines()
    for lines in file:
        lines = lines.strip(", ")
        lines = lines.replace(", ", ",  ")
        print(lines)


# Option vm displays to user all tasks assigned to them, only.


def view_my_tasks(user):

# i open the tasks.txt file, turn it into a list with a for loop and i used the enumerate function tonumber the lines so
#that i can display all tasks belonging to the user in a user friendly manner

    with open("tasks.txt", "r") as file:
        read = file.readlines()
        for line_num, lines in enumerate(read):
            lines = lines.split(", ")
            if user in lines:
                print(f"___________________[{line_num + 1}]________________")
                print(f"USER:\t\t\t\t{lines[0]}")
                print(f"TASK:\t\t\t\t{lines[1]}")
                print(f"DESCRIPTION:\t\t{lines[2]}")
                print(f"DUE DATE:\t\t\t{lines[3]}")
                print(f"CURRENT DATE:\t \t{lines[4]}")
                print(f"COMPLETED Y/N:\t\t{lines[5]}")

# user is asked to enter a task number or press -1 to exit. if they press a task number, they will be taken to another
# menu where they will have a choice to edit username, edit due date or mark task as complete

    others = []
    pick = int(input("please enter a task number or '-1' to quit: ")) - 1
    if pick == -1:
        print("See you next time")
        #exit()


    print("_______________________________________________________________")
    print(f"\nYou have picked task {pick + 1}.")
    print("---------------------------------------------------------------")
    with open("tasks.txt", "r") as file:
        read = file.readlines()

# bellow i have appended a list called others where i can store a list of the other tasks

    for line_num, lines in enumerate(read):
        lines = lines.split(", ")
        if pick != line_num:
            others.append(lines)

    for line_num, lines in enumerate(read):
        lines = lines.split(", ")
        if pick == line_num and lines[0] == user:
            print("\n1. Mark As Complete")
            print("2. Edit Username")
            print("3. Edit Due Date")
            choice = int(input("PLEASE MAKE A SELECTION: "))

# if choice is == to 1, i made a code to mark the chosen line as compete and .join the other list and the chosen list
# and re write the task file

            if choice == 1:
                lines[-1] = "Yes"
                lines = ", ".join(lines)
                with open("tasks.txt", "w") as file:
                    file.write(lines + "\n")
                with open("tasks.txt", "a") as file:
                    for x in others:
                        x = ", ".join(x)
                        file.write(x)
                    print("Your task is marked as complete")

# this is the same code as the "mark as complete" code but i have changed index 1 instead of index -1

            elif choice == 2:
                name = input(f"\nWhat name do you want to replace {lines[0]} with? ")
                lines[0] = name
                lines = ", ".join(lines)
                with open("tasks.txt", "w") as file:
                    file.write(lines)
                    for x in others:
                        x = ", ".join(x)
                        file.write(x)
                    print(f"Username has been replaced with {name}")

# again same code but i have modified index 3 instead of index 0

            elif choice == 3:
                date = input(f"\nDue date {lines[3]}: Please enter new due date in the same format.")
                lines[3] = date
                lines = ", ".join(lines)
                with open("tasks.txt", "w") as file:
                    file.write(lines)
            else:
                print("\nIncorrect option: try again ")
                view_my_tasks(user)


def generate_reports(task_generator, user):

# number of tasks and writing to tasks_overview

    num_of_tasks = 0
    with open("tasks.txt", "r") as file:
        read = file.readlines()
    for line_num, lines in enumerate(read):
        lines = lines.strip()
        lines = lines.split(", ")
        num_of_tasks = line_num + 1

    with open("tasks_overview.txt", "w") as task_report:
        task_report.write("________________________[ TASKS REPORT ]_________________________\n")
        task_report.write("______________________________\n")
        task_report.write(f"Total number of tasks: {num_of_tasks}.\n")

# writing completed tasks to tasks_overview

    completed_tasks = 0
    for line_num, lines in enumerate(read):
        lines = lines.strip()
        lines = lines.split(", ")
        if lines[-1] == "Yes":
            completed_tasks += 1

    task_report = open("tasks_overview.txt", "a")
    task_report.write("______________________________\n")
    task_report.write(f"Completed tasks: {completed_tasks}.\n")

# writing uncompleted tasks to tasks_overview

    percent_incomplete = 0
    uncompleted_tasks = 0

    for line_num, lines in enumerate(read):
        lines = lines.strip()
        lines = lines.split(", ")
        if lines[-1] == "No":
            uncompleted_tasks += 1
    percent_incomplete = uncompleted_tasks / num_of_tasks * 100
    task_report.write("______________________________\n")
    task_report.write(f"Uncompleted tasks: {uncompleted_tasks}.\n")

# writing the percentage of tasks to tasks_overview

    task_report.write("______________________________\n")
    task_report.write(f"percentage of incomplete tasks: {percent_incomplete}.\n")

# importing date from datetime in order to find if a task is overdue as in the code below

    from datetime import date
    today = date.today()
    now = today.strftime("%d %b %Y")
    incomplete_overdue = 0

    with open("tasks.txt", "r") as file:
        read = file.readlines()
        for lines in read:
            lines = lines.strip()
            lines = lines.split(", ")
            if lines[3] <= now and lines[-1] == "No":
                incomplete_overdue += 1

# writing the percentage of tasks that are overdue to tasks_overview
# also the tasks that haven't been completed and are overdue

    overdue = incomplete_overdue / num_of_tasks * 100
    task_report.write("______________________________\n")
    task_report.write(f"Tasks that haven't been completed and are overdue: {incomplete_overdue}.\n")
    task_report.write("______________________________\n")
    task_report.write(f"Percentage of tasks that are overdue: {overdue}.\n")
    task_report.close()

    with open("user_overview.txt", "w") as user_report:
        user_report.write("___________________[ USER REPORT ]_______________________\n")

# the total number of users registered in task manger and the total number of tasks that have been generated
# and tracked using task manager written to user_overview.txt after reading the info from task.txt

    num_of_users = 0
    holder = []
    with open("tasks.txt", "r") as file:
        read = file.readlines()
        for lines in read:
            lines = lines.strip()
            lines = lines.split(", ")
            if lines[0] not in holder:
                holder.append(lines[0])
                num_of_users += 1

    user_report = open("user_overview.txt", "a")
    user_report.write(f"\nTotal number of users registered in task manger: {num_of_users}\n")

    user_report.write("______________________________\n")
    user_report.write(f"The total number of tasks that have been generated\n")
    user_report.write(f"and tracked using task manager: {task_generator}\n")

# number of tasks assigned to user

    tasks_assigned = 0
    with open("tasks.txt", "r") as file:
        read = file.readlines()
        for lines in read:
            lines = lines.strip()
            lines = lines.split(", ")
            if lines[0] == user:
                tasks_assigned += 1

        user_report.write("______________________________\n")
        user_report.write(f"The total number of tasks assigned to you: {tasks_assigned}\n")

# percentage of tasks assigned to user

    percentage_of_tasks = tasks_assigned / num_of_tasks * 100

    user_report.write("______________________________\n")
    user_report.write(f"The percentage of tasks assigned to you: {percentage_of_tasks}\n")

    complete_assigned = 0
    with open("tasks.txt", "r") as file:
        read = file.readlines()
        for lines in read:
            lines = lines.strip()
            lines = lines.split(", ")
            if lines[0] == user and lines[-1] == "Yes":
                complete_assigned += 1
        percent_complete_assigned = complete_assigned / tasks_assigned * 100
        user_report.write("______________________________\n")
        user_report.write(f"The percentage of tasks assigned to you\n")
        user_report.write(f"that has been completed: {percent_complete_assigned}\n")

# The percentage of tasks assigned to user, that is yet to be completed and written to user_overview.txt

    incomplete_assigned = 0
    with open("tasks.txt", "r") as file:
        read = file.readlines()
        for lines in read:
            lines = lines.strip()
            lines = lines.split(", ")
            if lines[0] == user and lines[-1] == "No":
                incomplete_assigned += 1
        percent_incomplete_assigned = incomplete_assigned / tasks_assigned * 100
        user_report.write("______________________________\n")
        user_report.write(f"The percentage of tasks assigned to you\n")
        user_report.write(f"that is yet to be completed: {percent_incomplete_assigned}\n")

# The percentage of tasks assigned to user that is yet to be completed and is overdue
# the user_overview.txt has been generated

    count = 0
    with open("tasks.txt", "r") as file:
        read = file.readlines()
        for lines in read:
            lines = lines.strip()
            lines = lines.split(", ")
            if lines[0] == user and lines[3] < now and lines[-1] == "No":
                count += 1
    incomplete = count / tasks_assigned * 100

    user_report.write("______________________________\n")
    user_report.write(f"The percentage of tasks assigned to you\n")
    user_report.write(f"that is yet to be completed and is overdue: {percent_incomplete_assigned}\n")
    user_report.close()
    print("Your report has been generated")

def display_statistics():

    with open("tasks_overview.txt", "r") as file:
        task = file.readlines()
        for line in task:
            print(line)

    with open("user_overview.txt", "r") as file:
        task = file.readlines()
        for line in task:
            print(line)

def end():

    print('Goodbye!!!')
    exit()

user_pwd()