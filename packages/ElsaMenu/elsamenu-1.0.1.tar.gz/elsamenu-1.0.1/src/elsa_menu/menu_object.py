"""Basic Element of menu"""

from elsa_menu.abstract_class import MenuOption, AbstractMenu


class MenuObject(AbstractMenu):
    """
    Basic menu
    """
    def __init__(self, name: str, option: MenuOption = MenuOption()) -> None:
        super().__init__(name, option)
