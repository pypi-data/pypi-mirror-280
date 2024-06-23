"""Base Instance"""

import os

from elsa_menu.abstract_class import AbstractInstance


class ConsoleInstance(AbstractInstance):
    """
    Instance of menu on console
    """

    def print_text(self, lines) -> None:
        os.system('clear')
        for line in lines:
            print(line, flush=True, end='\r\n')
