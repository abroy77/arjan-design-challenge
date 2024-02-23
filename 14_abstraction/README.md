## Challenge: Abstraction
Introducing (levels of) abstraction allows classes to need less knowledge of each other, thus reducing coupling. This makes code more readable, maintainable and understood better both in depth, but also from a

**higher (conceptual) level.** 

For this challenge you need to refactor the given code so that the `WeatherService` becomes agnostic to the `requests` module.

In the current setup, `WeatherService` fetches the current weather forecast of a given city using the OpenWeather API. However, the `WeatherService` class is coupled to the `requests` library. This makes it hard to change the request module in the future to something else, or to replace it by a mock http request when testing the code.

The challenge is to use abstraction to separate the `WeatherService` class from the `requests` module.

### Hint
You can create a separate `RequestsClient` class that defines a get method for fetching data from an API, and then let the `WeatherService` depend on an abstraction.

### Resources
[Video](https://youtu.be/2ejbLVkCndI) covering dependency injection and dependency inversion