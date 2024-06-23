from typing import Tuple
import termios
import select
import tty
import sys

from elsa_menu.abstract_class import Input, InputValue


class KeyboardInput(Input):
    """
    Manage the input from keyboard
    """

    def _getch_helper(self, timeout) -> str:
        """
        Helper function to read from keyboard
        """
        fd = sys.stdin.fileno()
        settings = termios.tcgetattr(fd)
        ch = None
        try:
            tty.setraw(fd)
            if timeout:
                ready, _, _ = select.select([sys.stdin], [], [], timeout)
                if ready:
                    ch = sys.stdin.read(1)
                else:
                    ch = None
            else:
                ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, settings)
        return ch

    def getch(self) -> Tuple[InputValue, str]:
        """
        Read keyborad input
        """
        key = self._getch_helper(0.1)

        if key == '\x1b':
            # special character, like up/down/...
            next_key = self._getch_helper(None)

            if next_key == '[':
                arrow = self._getch_helper(None)

                if arrow == 'A':
                    return (InputValue.UP, arrow)
                elif arrow == 'B':
                    return (InputValue.DOWN, arrow)
                else:
                    return (InputValue.ND_X1, arrow)
        elif key == '\r':
            return (InputValue.ENTER, key)
        elif key == '\x7f':
            return (InputValue.BACK, key)
        elif key is None:
            return None
        else:
            return (InputValue.ND, key)
