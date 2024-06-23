"""Base menu object"""

from elsa_menu.abstract_class import AbstractMenu, Input, AbstractInstance
from elsa_menu.instance_object import ConsoleInstance
from elsa_menu.keyboard_input import KeyboardInput


class ElsaMenu(object):
    """
    Base class of menu
    """

    def __init__(self, refresh_time: int = 5, input_: Input = KeyboardInput()) -> None:
        self.instance: AbstractInstance = ConsoleInstance(input_, refresh_time, False)
        self.root = None

    def set_root(self, root: AbstractMenu):
        """
        Set menu root
        """
        self.root = root

    def start_show(self):
        """
        Start menu
        """
        self.instance.set_current_menu((self.root, 0))
        self.instance.start_show()
