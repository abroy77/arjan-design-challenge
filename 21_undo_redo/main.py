from dataclasses import dataclass, field


@dataclass
class InsertCommand:
    text: str
    num_chars: int


@dataclass
class DeleteCommand:
    num_chars: int
    text: str


Command = InsertCommand | DeleteCommand


@dataclass
class TextEditor:
    text: str = ""
    undo_stack: list[Command] = field(default_factory=list)
    redo_stack: list[Command] = field(default_factory=list)

    def insert(self, text: str) -> None:
        insert_command = InsertCommand(text, len(text))
        self.text += insert_command.text
        self.undo_stack.append(insert_command)
        self.redo_stack.clear()

    def delete(self, num_chars: int) -> None:
        delete_command = DeleteCommand(num_chars, text=self.text[-num_chars:])
        self.text = self.text[:-delete_command.num_chars]
        self.undo_stack.append(delete_command)
        self.redo_stack.clear()

    def undo(self) -> None:
        if not self.undo_stack:
            return
        command = self.undo_stack.pop()
        if isinstance(command, InsertCommand):
            self.text = self.text[:-command.num_chars]
        else:
            self.text += command.text

        self.redo_stack.append(command)

    def redo(self) -> None:

        if not self.redo_stack:
            return
        command = self.redo_stack.pop()
        if isinstance(command, InsertCommand):
            self.text += command.text
        else:
            self.text = self.text[:-command.num_chars]

        self.undo_stack.append(command)

    def print_text(self) -> None:
        print(self.text)


def main() -> None:
    # Test the text editor
    editor = TextEditor()

    # Since there is no text, these commands should do nothing
    editor.undo()
    editor.redo()

    editor.insert("Hello")
    editor.insert(" World!")
    editor.print_text()  # Output: Hello World!

    editor.delete(6)
    editor.print_text()  # Output: Hello

    editor.undo()
    editor.print_text()  # Output: Hello World!

    editor.redo()
    editor.print_text()  # Output: Hello

    editor.insert("!!!")
    editor.print_text()  # Output: Hello!!!

    editor.undo()
    editor.undo()
    editor.print_text()  # Output: Hello World!


if __name__ == "__main__":
    main()
