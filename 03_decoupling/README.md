## Challenge: Decoupling
In this challenge, you're going to work on a banking service.

The problem with the current code is that the `BankService` class (in `bank.py`) is highly coupled with the payment service and the different account types. Also, the code has quite a bit of duplication. Your job is to refactor this code so that it's less coupled and has less duplicate code.

You have quite a bit of freedom in this challenge: it's okay to introduce new classes or replace existing classes by functions, feel free to experiment! However, the goal remains that banking operations should be decoupled from payment operations as much as possible.

### Resources
[Video](https://youtu.be/qR4-PBLUZNw) by me about reducing coupling