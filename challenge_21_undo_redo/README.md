## Challenge: Undo/Redo
Download the code for this challenge and inspect what it does.

In short, this is a simple text editor. It's not a complete text editor, but it does provide a basic system underlying a text editor that allows for text operations like inserting and deleting text. Obviously, a real text editor will have a way more complex system underlying it, but that's out of the scope of this challenge (though feel free to extend this code if you like).

The goal of this challenge is to extend the text editor to have **undo and redo operations**. However, when you write the code, make sure to think about how to add undo and redo behavior in such a way that it's independent of the text editing operations. For example, if you want to add a new text editing feature "boldface" in the future, you should be able to do it without having to change the undo/redo system.

### Resources
* [Watch my video](https://youtu.be/FM71_a3txTo) about the Command design pattern for inspiration