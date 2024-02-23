## Challenge: Configuration
A configuration file allows you to store settings or parameters separately from the code. This makes it easier to  modify or manage these settings without changing the code itself, and also allows you to use the same code with different configurations, easier than when you need to find that value in the code itself.

In the weather service example, specifically the API url and the API key are things that are good candidates to move to a config file.

Download the code for this challenge, and extend it so that this information is now read from a config file (in JSON format). Consider the following things while refactoring the code:

* What values should we store in the config file and how do we structure it?
* Where do we define the config file path?
* Where should be load the config file?
* How should we pass data that is read from the config file to the code that needs it?