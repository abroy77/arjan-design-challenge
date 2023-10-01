## Challenge: MVP
When you create a GUI application, it's a good thing to consider separating the GUI-specific code such as creating frames, buttons, text fields, and so on, from the logic of your application (what should happen when you press a button), as well as from the data that your application relies on or modifies.

There are different architectural patterns that address this. The most well-known one is Model-View-Controller, but there are several varieties including Model-View-Presenter or Model-View-Viewmodel.

The code that you'll use as a starting point in this challenge has a single main() function containing everything, although it does rely on the functions you created in the previous challenge that process data.

Refactor this code by using a GUI architectural pattern such as Model-View-Controller or Model-View-Presenter. Consider:

* What code should be part of each element of the pattern?
* Where should we create and connect the Model, View, and Controller/Presenter objects?
* Which object needs to have a reference to which other object?

### Resources
* [Model-view-controller (Wikipedia)](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)

* [Model-view-presenter (Wikipedia)](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter)

* [Video](https://youtu.be/eHhXoCNCI1c) about GUI architectures