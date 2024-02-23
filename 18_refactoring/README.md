## Challenge: Refactoring
While running code directly from its script is quite common, especially when developing, sometimes it's (necessary or) useful to run the application through the command line. This simplifies the interface for the user and allows for extra functionality such as documentation for all the available commands and examples of how to use the interface.

I have (again) extended the weather service application to now include a command-line interface. Refactor the command-line interface code in the main.py file to solve these design problems:

* There's a lot of duplication in the CLI code.
* Everything is in a single main function.
* Translating the CLI to display another language (for example, Dutch instead of English) would be a nightmare.