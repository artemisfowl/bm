## Battery Monitor for Linux and Windows

### Problem Statement
One issue which people close to me were complaining about was the ability to have a notifier program which
would be able to notify the user based on the desired battery percentage. Meaning, that when the battery
percentage of the laptop goes below a certain point, the program would notify the user whether to charge
or keep using the same.

### The solution
In order to write the Proof Of Concept program, the choice of language was Python. Initial attempts were made
with C and C++, however the requirement of extensive libraries and the amount of time at hand forced me to
use Python.

In short, the aim was to create a program which would perform the following operations properly:
- Check the status of the battery in both Windows and Linux
- Send out a notification in both Windows and Linux
- Keep monitoring the status of the battery based on the user's specification

### Problems faced and the respective solutions
1. *Show notifications in Windows 10+ OS(s)* : Showing the notifications in Windows operating system was
posing problems. The first amonf these problems was that there is no library easily available which can be
made to work with MinGW. Process for checking the status of the battery is already available which
works for both Windows and Linux, however sending out notification in Windows was an issue.
While trying to find a library which would be able to handle both and not be as bulky as Qt, Python
presented an easier solution to the same.
2. *Single library to show the notifications* : Despite using Python, there is not single library with which
a notification can be shown in Windows as well as in Linux. Hence the platform specific code has to be put
in for importing the right module and setting up the toast master with the right notification handler
