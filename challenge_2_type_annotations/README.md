## Challenge: Type Annotations
Type annotations in Python allow you to explicitly specify the data types of constants, variables, function parameters and return values. This helps to improve code clarity, readability, and maintainability, especially in large-scale projects where multiple developers may be working on the same codebase.

By using type annotations, you can catch potential bugs early on in the development process, and on top of that they help your IDE provide better code suggestions and error detection.

For this challenge, you will need to add type annotations to the code given in the `before.py` file (click the Downloads button at the top to get the code). Before you start working on the code, make sure your VS Code editor has the Python language extension installed and also make sure that you've set type checking mode to "strict". You can do this by adding the following line to your settings.json file:

``` "python.analysis.typeCheckingMode": "strict" ```

Once you've done that and you open the `before.py` file, you should see a bunch of errors related to the types missing (even though you can still run the code).

The challenge is to write the type annotations so that:

All type errors identified by the IDE are gone
The type annotations are a generic as possible - in other words, the type annotations shouldn't impose any extra limitations on how you can use the functions
You're not allowed to use the Any type in this challenge. You can make minor modifications to the code if needed. However, the functionality should stay the same and you're not allowed to change things like function arguments and return types.

### Resources
[PEP 484 (type hints)](https://peps.python.org/pep-0484/)