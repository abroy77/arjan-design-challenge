## Challenge: Payment Strategy
The Strategy pattern is a design pattern that allows you to define a family of algorithms (strategies) and make them interchangeable within an object at runtime. In other words, it lets you define a set of related algorithms and encapsulate each one in a separate class.

An object can then use one of these algorithms (strategies) without knowing the details of how the algorithm works or how it's implemented. This pattern promotes the principle of "composition over inheritance", which means that behavior should be composed dynamically at runtime rather than being hard-coded into classes through inheritance. This makes the code more flexible, extensible, and easy to maintain.

The example code allows you to pay by credit card, PayPal or Apple Pay. This is handled by the process_payment method in the ShoppingCart class. In this version of the code though, the shopping cart and in particular the process_payment method needs to know all the implementation details of each payment processing option. 

For this challenge you need to refactor this code and use the Strategy pattern to remove the coupling between the shopping cart and the different payment methods. You don't have to follow the pattern exactly by the book, you can also use a variety of the pattern, as long as it accurately removes the coupling.

#### Resources
[Strategy design pattern (Wikipedia)](https://en.wikipedia.org/wiki/Strategy_pattern)
My [video](https://youtu.be/WQ8bNdxREHU) about the Strategy design pattern, and a [follow-up](https://youtu.be/n2b_Cxh20Fw).