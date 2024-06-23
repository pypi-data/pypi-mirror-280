"""Basic Element of menu"""

from elsa_menu.abstract_class import Element, AbstractMenu, AbstractInstance


class TextBox(Element):
    """
    Simple textbox on menu
    """

    def __init__(self, selectable: bool, text: str) -> None:
        super().__init__(selectable)
        self.text = text

    def generate_text(self) -> str:
        return self.text


class NotSelectableTextBox(TextBox):
    def __init__(self, text: str) -> None:
        super().__init__(False, text)


class SelectableTextBox(TextBox):
    def __init__(self, text: str) -> None:
        super().__init__(True, text)


class OpenMenu(SelectableTextBox):
    """
    Base entry to change menu to on submenu
    """
    def __init__(self, text: str, menu: AbstractMenu) -> None:
        super().__init__(text)
        self.menu = menu

    def callback_enter(self, instance: AbstractInstance) -> str:
        instance.open_sub_menu(self.menu)


class CloseMenu(SelectableTextBox):
    def __init__(self, text: str) -> None:
        super().__init__(text)

    def callback_enter(self, instance: AbstractInstance) -> str:
        instance.stop()


class BackMenu(SelectableTextBox):
    def __init__(self, text: str, stay: bool = True) -> None:
        super().__init__(text)
        self.stay = stay

    def callback_enter(self, instance: AbstractInstance) -> str:
        instance.set_previous_menu(self.stay)
