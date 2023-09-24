### Challenge: Demeter
The **Law of Demeter**, also known as the Principle of Least Knowledge, is a software design guideline that suggests that an object should avoid direct interaction with other objects that are not directly related to its primary purpose.

In simpler words, this law states that an object should only communicate with its immediate friends and not with the friends/attributes of its friends. Violating this principle can result in tightly coupled and brittle code that is difficult to maintain and modify over time.

A typical violation of the law is that one object directly interacts with an instance variable of another object. The code belonging to this challenge has several violations of the Law of Demeter. Refactor the code to remove these violations.

Resources
[Law of Demeter (Wikipedia)](https://en.wikipedia.org/wiki/Law_of_Demeter)