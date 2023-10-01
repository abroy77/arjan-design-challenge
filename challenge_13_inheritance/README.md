## Challenge: Inheritance
I've learned that you should use inheritance sparingly in your code. It can be a really helpful tool to decouple your code, especially if you use inheritance with Abstract Base Classes or Protocols in Python.

Unfortunately, many developers abuse inheritance to do other things than decoupling your code. The code belonging to this challenge is a good example of that.

The code retrieves the weather information from a free-to-use weather API and prints it to the console. To run the code, you'll need to obtain a free API key from the OpenWeather service. That requires creating an account and you automatically receive one after you confirm your e-mail address. To create an account, follow [these](https://openweathermap.org/appid#signup) instructions. Note that it might take some few minutes before the API key is activated on their servers.

* After you've created the free account and you have an API key, download the code and replace the key in the code with your API key. Run the code to see what it does.
* Analyze the code, and take a look at how it's organized. In particular, think about how inheritance is being used in the code.
* Refactor the code so that inheritance is no longer used.
* Compare your second version with the original code and consider in what ways the new version is better. How did you remove the inheritance relationship? Did it lead you to change other things as well in the code?
### Resources
* [Video](https://youtu.be/0mcP8ZpUR38) about composition vs. inheritance