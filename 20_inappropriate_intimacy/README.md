## Challenge: Inappropriate Intimacy
In programming, inappropriate intimacy refers to a situation where different parts of code become too dependent on each other, making changes or fixes difficult and causing potential issues. For example, imagine a Python class that directly accesses and modifies variables of another class, instead of using methods to interact with it, or a function that requests a lot of information without actually needing it. This tight coupling creates a brittle system that is hard to maintain and test. Inappropriate intimacy is an example of a code smell: if you see it in a piece of code, it's an indication that you need to fix something in the design.

An example of inappropriate intimacy is in the code for this challenge. Can you detect what it is? Refactor the code to fix the problem.

### Resources
* [Code smells (Wikipedia)](https://en.wikipedia.org/wiki/Code_smell)