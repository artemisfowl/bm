## Battery Monitor for Linux and Windows

### Problem Statement
Implement a program which can be run by a user in order to monitor the battery percentage and when the
battery charge goes below a specified limit, inform/notify the user in order to connect the charger.

### The solution
In order to write the Proof Of Concept program, the choice of language was Python. Initial attempts were made
with C and C++, however the requirement of extensive libraries and the amount of time at hand forced me to
use Python.

In short, the aim was to create a program which would perform the following operations properly:
- Check the status of the battery in both Windows and Linux
- Send out a notification in both Windows and Linux
- Keep monitoring the status of the battery based on the user's specification

Advanced Requirements:
- Should be able to show icons in the notification
- Should support both Windows and Linux platforms
- When charger is connected, the notifications should cease after showing charging once
- When charger is disconnected and battery percentage is above the specified limit, the notification should
be shown only once and then no more until the battery percentage drops below desired level

### Problems faced and the respective solutions
1. *Show notifications in Windows 10+ OS(s)* : Showing the notifications in Windows operating system was
posing problems. The first amonf these problems was that there is no library easily available which can be
made to work with MinGW. Process for checking the status of the battery is already available which
works for both Windows and Linux, however sending out notification in Windows was an issue.
While trying to find a library which would be able to handle both and not be as bulky as Qt, Python
presented an easier solution to the same.
2. *Single library to show the notifications* : Despite using Python, there is no single library with which
a notification can be shown in Windows as well as in Linux. Hence the platform specific code had to be put
in for importing the right module and setting up the toast master with the right notification handler.

### Not tested
I don't own a Mac system(though I have always wanted to own a Macbook air), hence I have not been able to
test the program on a Mac. So, in case you have a Mac and want to use this program(this should not be required
for a Mac though - the battery in those systems are good), please note that this might not work and the user
will have to hack around a bit in order to get it to work out
