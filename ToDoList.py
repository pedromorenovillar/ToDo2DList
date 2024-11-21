# 👉 Day 45 Challenge
# Made it? Good! Let's get cracking.

# Your system should:

# 1- Have a menu that asks if you want to add, view, move or edit a 'to do'.
# 2- If you choose 'add' then the system should:
#   2.1 - Prompt you to input what the to do is, when it is due by and the priority (high, medium or low).
#   2.2- Add the 'to do' to the list.
# 3- 'View' should give two options:
#   3.1 - View all - shows all 'to dos' with a pretty print.
#   3.2 - View priority - allows you to search for high, medium or low priority and only see matching tasks.
# 4- 'Edit' allows you to change any of the information within one of the 'to dos'.
# 5- 'Remove' lets you completely remove a 'to do' when it is 'to done'.

# Hints
# - Use a separate subroutine for add, view, edit, and remove.
# - Clear the console before viewing a new entry.
# - Use a while True loop to call the subroutines and display the menu.

import os, time


def printToDoList(list, longestItem):
  os.system("clear")
  print()
  paddedLength = longestItem + 4
  rowLength = paddedLength * len(list[0]) + (len(list[0]) - 1) * 3
  print(f"\033[33m{"My To Do List":^{rowLength}}\033[0m")
  print("-" * rowLength)
  for row in list:
    formatted_row = [f"{cell:^{paddedLength}}" for cell in row]
    print("|".join(formatted_row))
    print("-" * rowLength)
  

myTasks = [
  ["TASK", "DUE", "PRIORITY"],
  ["Clean the kitchen", "Today", "High"],
  ["Cook", "Tomorrow", "Medium"],
  ["Feed the hamster", "Friday", "Low"]
]

def findLongestItem(two_d_list):
    flat_list = [item for row in two_d_list for item in row]
    return len(max(flat_list, key=len))

def backOrQuit():
  backOrQuit = input("""What do you want to do now?
  1. See the menu again
  2. Quit
  > """).strip().lower()
  if backOrQuit[0] == "q" or backOrQuit[0] == "2":
    quit("Closing the to do list...")

def addTask():
  os.system("clear")
  print("Adding task")
  task = input("What is the task? > ").strip().capitalize()
  due = input("When is it due by? > ").strip().capitalize()
  priority = input("What is the priority? (high/medium/low) > ").strip().capitalize()
  myTasks.append([task, due, priority])
  print(f"The following task has been added: {task} | {due} | {priority}")
  backOrQuit()

def viewTasks():
  os.system("clear")
  print("Viewing tasks")
  allOrPriority = input("""Do you want to see all tasks or filter by priority?
    1. All
    2. Filter by priority
    > """).strip().lower()
  if allOrPriority[0] == "a" or allOrPriority[0] == "1":
    viewAll()
    time.sleep(5)
  elif allOrPriority[0] == "f" or allOrPriority[0] == "2":
    priorityView = input("""Which tasks do you want to see?
    1. High priority
    2. Medium priority
    3. Low priority
    > """).strip().lower()

    if priorityView[0] == "h" or priorityView[0] == "1":
      filterByPriority("High")
    elif priorityView[0] == "m" or priorityView[0] == "2":
      filterByPriority("Medium")
    elif priorityView[0] == "l" or priorityView[0] == "3":
      filterByPriority("Low")
    else:
        print("Invalid option! Returning to menu.")
        time.sleep(2)
  else:
      print("Invalid option! Returning to menu.")
      time.sleep(2)
      backOrQuit()

def filterByPriority(priority):
    os.system("clear")
    print(f"Displaying tasks with \033[33m{priority}\033[0m priority...")
    time.sleep(1)
    filteredTasks = [myTasks[0]] + [row for row in myTasks[1:] if row[2] == priority.capitalize()]
    
    if len(filteredTasks) > 1: 
        printToDoList(filteredTasks, findLongestItem(filteredTasks))
    else:
        print(f"No tasks with {priority} priority found.")
    
    time.sleep(5)


def viewAll():
  printToDoList(myTasks, findLongestItem(myTasks))

def removeTask():
    taskToRemove = input("Which task do you want to remove? ").strip().capitalize()
    found = False
    for row in myTasks[1:]:
        if taskToRemove == row[0]:
            myTasks.remove(row)
            print(f'\033[33m{taskToRemove}\033[0m removed from the list!')
            found = True
            time.sleep(1)
            break
    if not found:
        print(f'\033[33m{taskToRemove}\033[0m is not on the list!')
        time.sleep(1)
    viewAll()

def editTask():
  viewAll()
  taskToEdit = input("Which task do you want to edit? ").strip()
  found = False

  for i, row in enumerate(myTasks[1:], start=1): 
      if taskToEdit.lower() == row[0].lower(): 
          print(f"Current details: Task: {row[0]}, Due: {row[1]}, Priority: {row[2]}")
          
          task = input(f"New task name (leave blank to keep '{row[0]}'): ").strip() or row[0]
          due = input(f"New due date (leave blank to keep '{row[1]}'): ").strip() or row[1]
          priority = input(f"New priority (leave blank to keep '{row[2]}'): ").strip() or row[2]

          myTasks[i] = [task.capitalize(), due.capitalize(), priority.capitalize()]
          print(f"\033[33m{task.capitalize()}\033[0m has been updated!")
          found = True
          time.sleep(1)
          break

  if not found:
      print(f"\033[33m{taskToEdit.capitalize()}\033[0m is not on the list!")
      time.sleep(1)

  viewAll()

while True:
  os.system("clear")
  print("  🌟 Life Organizer 🌟")
  menu = input("""
  What do you want to do?
  1. View tasks
  2. Add task
  3. Edit task
  4. Remove task
  > """).strip().lower()

  if menu[0] == "v" or menu[0] == "1":
    viewTasks()
  elif menu[0] == "a" or menu[0] == "2":
    addTask() 
  elif menu[0] == "e" or menu[0] == "3":
    editTask()
  elif menu[0] == "r" or menu[0] == "4":
    removeTask()
  else:
    backOrQuit()