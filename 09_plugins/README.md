## Challenge: Plugins
In this challenge, we're going to take the Strategy pattern you implemented in the previous challenge to the next level. First, download the code by clicking the Downloads button at the top.

When you take a look at the code, you see that at the moment, adding a new payment processor means we have to change the application code. For example, if you wanted to add a Google Pay option, you'll need to add a function to the `main.py` file. This is not ideal, because that file will get larger and larger as you add more payment methods. Additionally, it would be ideal if adding a new payment method requires only minimal changes in the rest of the code so that things are nicely decoupled and it's really easy to extend the code in the future.

The aim of this challenge is to modify the code so that we can add additional payment methods **without having to change anything at all in the main file**. This is what's also called a **plugin mechanism**.

Modify the code so that you can add more payment methods by going through these simple steps:

* Create a new Python script containing the code for the payment method that you'd like to add.
* Put the script in a dedicated plugins folder.
* Now run `main.py` - it should recognize the new payment method in the plugins folder and make it available automatically to the user.
That's it!

Once you've refactored the code so that it supports a plugin interface, test it by creating a new payment method and verify that you can use it without having to change anything in the rest of the code.

Hints
* You can use `importlib` to dynamically load Python scripts and you can use `os.walk` to retrieve the files in a particular folder.
* Feel free to split things up into separate files. For example, you could create a separate file that manages loading and getting access to the plugins, so your `main.py` file remains relatively small.

### Resources
Check out this [video](https://youtu.be/iCE1bDoit9Q) for an idea of how to approach this problem.