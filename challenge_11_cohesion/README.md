## Challenge: Cohesion
It is very common when coding and especially for beginners that people write very big functions with lots of different functionalities inside. Although this might look very appealing approach because you can write the code faster, it creates unnecessary coupling of functionalities, that becomes a headache later on when you try to test, debug, or further develop your application.

In the code belonging to this challenge, you'll see that there is a single main() function that contains everything. Refactor this function into several smaller ones without - of course - affecting the overall functionality. There are many ways in which you can split up the single large function, but try to come up with a solution that makes sure the separate functions are not too large, that they're easy to test, and that there's not too much duplication.

### Resources
* [Video](https://youtu.be/eiDyK_ofPPM) about cohesion and coupling
* [Cohesion (Wikipedia)](https://en.wikipedia.org/wiki/Cohesion_(computer_science))