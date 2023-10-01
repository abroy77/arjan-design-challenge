## Challenge: Higher-Order Functions
A higher-order function is a function that takes one or more functions as arguments, and/or returns a function as  its result. In other words, a higher-order function is a function that operates on functions.

Higher-order functions are a key feature of functional programming, which is a programming paradigm that emphasizes the use of functions to perform computations. They enable a more declarative and expressive style of programming, where functions can be composed, combined, and manipulated like any other value.

Some common examples of higher-order functions in Python include map, filter, and reduce. These functions take one or more functions as arguments and apply them to some input data to produce a new output.

The goal of this challenge is to take the object-oriented weather service code from the previous challenge (see the Downloads section at the top) and change it to functional code that relies on a higher-order function, as follows:

* First, turn the `WeatherService` class into separate functions. Specifically, create a `get_forecast` function that takes an `HttpClient`, a city and an API key and then returns the forecast object.
* Turn the properties that retrieve temperature, humidity, etc, into separate functions that get the forecast object as an argument and then extract the relevant information.
* Now, change the `RequestsClient` class into a get function, and then pass that function to the `get_forecast` function (this turns it into a higher-order function!)
* As a bonus, can you define another function that allows you to get a weather forecast without having to provide the http getter function and the API key?

### Resources

* [Higher-order functions (Wikipedia)](https://en.wikipedia.org/wiki/Higher-order_function)

* [Video](https://youtu.be/ph2HjBQuI8Y) about functools in Python