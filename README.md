# The hangman

> My take on replit's 100 days of code [day 45 challenge](https://replit.com/learn/100-days-of-python/hub?utm_source=widget). It involves CRUD operations on a two-dimensional list.

### Requirements

1.- Have a menu that asks if you want to add, view, move or edit a 'to do'.

2.- If you choose 'add' then the system should:

  2.1 - Prompt you to input what the to do is, when it is due by and the priority (high, medium or low).

  2.2- Add the 'to do' to the list.

3.- 'View' should give two options:

  3.1 - View all - shows all 'to dos' with a pretty print.

  3.2 - View priority - allows you to search for high, medium or low priority and only see matching tasks.

4.- 'Edit' allows you to change any of the information within one of the 'to dos'.

5- 'Remove' lets you completely remove a 'to do' when it is 'to done'.

Hints
- Use a separate subroutine for add, view, edit, and remove.
- Clear the console before viewing a new entry.
- Use a while True loop to call the subroutines and display the menu.