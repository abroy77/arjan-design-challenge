## Challenge: String Formatting
String formatting is a way of constructing a string that includes dynamic or variable values. It allows you to insert values into a string and control how those values are displayed. You can use string formatting to replace placeholders in a string with actual values, such as numbers or strings, and also specify how those values should be formatted.

This can help make your code more readable and easier to maintain, especially when you need to output complex or formatted strings. In Python, there are different ways to perform string formatting, including using the % operator, the format() method, or f-strings. I recommend you use f-strings wherever possible.

The starting point of this challenge is a code example that creates a shopping cart and prints an overview of the shopping cart contents to the console. Currently, this is what the program produces, which is unfortunately quite hard to read:

Shopping Cart:
Item, Price, Qty, Total
Apple, 1.50, 10, 15.00
Banana, 2.00, 2, 4.00
Pizza, 11.90, 5, 59.50
========================================
Total: $78.50
The goal is to use string formatting to make the output easier to read by better aligning the values. Ultimately, the table look something like this:

Shopping Cart:
Item           Price    Qty        Total
Apple       $   1.50     10     $  15.00
Banana      $   2.00      2     $   4.00
Pizza       $  11.90      5     $  59.50
========================================
Total: $ 78.50
The exact number of spaces between each column is not important. However, the dollar signs as well as the prices need to be correctly aligned.

### Resources
* [PEP 498 (f-strings)](https://peps.python.org/pep-0498/)
* My [video](https://youtu.be/Mfmr_Puhtew) about f-strings
