"""Abstract classes and class/enum"""

from __future__ import annotations
from typing import Tuple, Optional, List
from abc import ABC, abstractmethod
from threading import Thread, Event
from dataclasses import dataclass
from time import time, sleep
from enum import Enum

from elsa_menu.color import TextColor, TextType


class InputValue(Enum):
    """
    Generic Input value, there are only the minimal action to navigate on menu
    """
    ND = (0, "ND")          # ND, but not arrow
    ND_X1 = (1, "ND_X1")    # ND arrow
    UP = (2, "UP")          # Go up on menu
    DOWN = (3, "DOWN")      # Go down on menu
    ENTER = (4, "ENTER")    # Enter on current selected line
    BACK = (5, "BACK")      # Go previous menu or close


class Input(ABC):
    """
    Generic input class.

    Main function to override are: getch
    """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def getch(self) -> Tuple[InputValue, str]:
        """
        Read the input and return a tuple where the first element
        are the InputValue, see the Enum, the second value on tuple
        are the string value of input read.

        Returns:
            Tuple[InputValue, str]: input read
        """


@dataclass
class MenuOption(object):
    """
    Data class to manage the option of menu.
    The option are:
    - cursor, default: "->"
    - prefix on line, default: None
    - don't add cursor space on not selectable line on menu, default: True
    """
    cursor: Optional[str] = "->"
    prefix: Optional[str] = None
    no_cursor_space_not_selectable: Optional[bool] = True


class Element(ABC):
    """
    Generic element on menu
    """

    def __init__(self, selectable: bool, refresh_min: int = 0, unique_id: str = None) -> None:
        """
        Init of generic element on menu, are needed all minimal info to add
        entry on menu, the value are:
        - The entry are selectable?
        - The entry require a refresh? passa value > 0 to set it

        Args:
            selectable (bool): _description_
            refresh_min (int, optional): _description_. Defaults to 0.
        """
        self.selectable: bool = selectable
        self.refresh_min: int = refresh_min
        self.unique_id: str = unique_id

    def generate_line(self, on_it: bool, option: MenuOption) -> print:
        """
        Generate the line to print on menu

        Args:
            on_it (bool): _description_
            option (MenuOption): _description_

        Returns:
            print: _description_
        """
        line = TextType.RESET.value + TextColor.WHITE.value
        if option.prefix:
            line = option.prefix.copy()

        if on_it:
            line += option.cursor
        elif self.selectable:
            if option.no_cursor_space_not_selectable:
                line += " " * len(option.cursor)
        return line + self.generate_text() + TextType.RESET.value

    @abstractmethod
    def generate_text(self) -> str:
        """
        Function to override, this will be called when are requested the
        rendering of entry on menu.

        Returns:
            str: line to print on menu
        """

    def callback_enter(self, instance: AbstractInstance) -> None:
        """
        This function are called when the user do a InputValue.ENTER

        Args:
            instance (AbstractInstance): current instance
        """

    def callback_go_in(self, instance: AbstractInstance) -> None:
        """
        This function are called when the cursor select this line

        Args:
            instance (AbstractInstance): current instance
        """

    def callback_go_out(self, instance: AbstractInstance) -> None:
        """
        This function are called when the cursor exit from this entry

        Args:
            instance (AbstractInstance): current instance
        """

    def callback_move_on_menu(self,
                              instance: AbstractInstance,
                              on_it: bool) -> None:
        """
        This function are called when we execute a move on menu where
        are present this entry

        Args:
            instance (AbstractInstance): current instance
            on_it (bool): True if the line are selected, otherwise False
        """


class AbstractMenu(ABC):
    """
    Abstract menu.
    Each menu has:
    - name
    - option -> MenuOption
    - list of entry
    """
    def __init__(self, name: str, option: MenuOption = MenuOption()) -> None:
        self.name = name
        self.option = option
        self.entry: List[Element] = []

    def add_element(self, element: Element, index: int = None) -> None:
        """
        Add entry on menu
        """
        if element is None:
            return

        if element.unique_id is None:
            if index is not None and index > 0:
                element.unique_id = f"{index}"
            else:
                element.unique_id = f"{len(self.entry) - 1}"

        if index is not None and index > 0:
            # valid index value
            if (len(self.entry) - 1) < index:
                self.entry.insert(index, element)
                return
        self.entry.append(element)

    def remove_element_with_unique_id(self, unique_id: str) -> bool:
        """
        Remove element from unique id

        Args:
            unique_id (str): unique id of element to remove

        Returns:
            bool: True if something are removed, otherwise False
        """
        if unique_id is None:
            return False

        for index, _element in enumerate(self.entry):
            if _element.unique_id is None:
                continue
            if _element.unique_id == unique_id:
                self.remove_element_index(index)
                return True
        return False

    def remove_element_index(self, index: int) -> bool:
        """
        Remove element on index passed

        Args:
            index (int): Index of element to remove

        Returns:
            bool: True if something are removed, otherwise False
        """
        if index is None or index < 0 or index > (len(self.entry) - 1):
            return False
        self.entry.pop(index)
        return True

    def generate_text(self, sel_line: int) -> List[str]:
        """
        Generate the text to print

        Args:
            sel_line (int): current line selected

        Returns:
            List[str]: list of line to print
        """
        text: List[str] = []
        for index, entry in enumerate(self.entry):
            text.append(entry.generate_line(index == sel_line, self.option))
        return text

    def callback_enter(self, instance: AbstractInstance) -> None:
        """
        This function are called when this menu are opened
        The instance has this menu on reference, but this
        method are called before to generate_text

        Args:
            instance (AbstractInstance): current instance
        """

    def callback_quit(self, instance: AbstractInstance) -> None:
        """
        This function are called when this menu are closed
        The instance has the new menu reference, called
        before the generate_text on new menu

        Args:
            instance (AbstractInstance): current instance
        """

    def callback_move(self,
                      instance: AbstractInstance,
                      in_: Tuple[InputValue, str]) -> None:
        """
        This function are called when there are some interaction whit the
        menu

        Args:
            instance (AbstractInstance): current instance
            in_ (Tuple[InputValue, str]): input read
        """


class AbstractInstance(ABC):
    """
    Abstraction layer of instance
    """

    def __init__(self,
                 input_: Input,
                 refresh_time: float,
                 dont_close_on_back: bool) -> None:
        """
        Init, specify some option to manage the current open menu:
        - Input source
        - Auto refresh and the time on seconds
        - Don't close the instance if are request the BACK on root menu

        Args:
            input_ (Input): input source
            refresh_time (float): enable/disable auto refresh
            dont_close_on_back (bool): don't close on BACK on last menu
        """

        # data value
        self.refresh_time = refresh_time
        self.dont_close_on_back = dont_close_on_back
        self._input = input_

        # interna value
        self._current_menu: AbstractMenu = None
        self._current_line: int = 0
        self._history: List[AbstractMenu] = []

        # state value
        self._stop = False  # need to close all thread

        # internal event
        self._auto_refresh: Event = Event()     # auto refresh request
        self._update_menu: Event = Event()      # trigger the menu refresh
        self._action_event = Event()            # refresh required from action

        # auto refresh internal value
        self._time = time()
        self._current_refresh_time: int = 0

    def wait_action(self):
        """
        Wait action
        """
        _res = self._input.getch()
        if _res:
            return _res
        return None

    def go_up(self, step: int = 1) -> None:
        """
        Move cursor up of step passed

        Args:
            step (int, optional): step to move. Defaults to 1.
        """
        if len(self._current_menu.entry) <= 1:
            return
        self._current_line -= step
        if self._current_line < 0:
            self._current_line = len(self._current_menu.entry) - 1
        if not self._current_menu.entry[self._current_line].selectable:
            self.go_up(1)

    def go_down(self, step: int = 1) -> None:
        """
        Move cursor down of step passed

        Args:
            step (int, optional): step to move. Defaults to 1.
        """
        if len(self._current_menu.entry) <= 1:
            return
        self._current_line += step
        if self._current_line > len(self._current_menu.entry) - 1:
            self._current_line = 0
        if not self._current_menu.entry[self._current_line].selectable:
            self.go_down(1)

    def manage_action(self, in_: Tuple[InputValue, str]) -> bool:
        """
        Manage the input action

        Args:
            action (InputValue): Input read

        Returns:
            bool: True if menu change, otherwise False
        """
        _action = None
        if in_:
            _action = in_[0]
        _res = False
        _previous_slot = self._current_line
        _old_menu = self._current_menu
        if _action == InputValue.ND or _action == InputValue.ND_X1:
            _res = self.not_default_input(in_)
        elif _action == InputValue.UP:
            self.go_up()
            _res = False
        elif _action == InputValue.DOWN:
            self.go_down()
            _res = False
        elif _action == InputValue.ENTER:
            _entry = self._current_menu.entry[self._current_line]
            _entry.callback_enter(self)
            _res = _old_menu != self._current_menu
        elif _action == InputValue.BACK:
            _res = self.set_previous_menu(self.dont_close_on_back)
        else:
            _res = False

        self.manage_entry_callbacks(_res, _previous_slot, in_)
        return _res

    def not_default_input(self, _action: Tuple[InputValue, str]) -> bool:
        """
        Manage not default action

        Args:
            _action (Tuple[InputValue, str]): action read

        Returns:
            bool: True if menu change, otherwise False
        """
        return False

    def manage_entry_callbacks(self, change_menu: bool, previous_slot, in_):
        """
        Manage all callback after move

        Args:
            change_menu (bool): _description_
            previous_slot (_type_): _description_
        """
        _on_it = False
        if self._current_menu is None:
            return

        self._current_menu.callback_move(self, in_)

        for index, entry in enumerate(self._current_menu.entry):
            _on_it = False
            if index == self._current_line:
                _on_it = True
                entry.callback_go_in(self)

            if index == previous_slot:
                entry.callback_go_out(self)

            if not change_menu:
                entry.callback_move_on_menu(self, _on_it)

    def open_sub_menu(self, menu: AbstractMenu) -> None:
        """
        Open new menu

        Args:
            menu (AbstractMenu): new menu to open
        """
        self._history.append((self._current_menu, self._current_line))
        self.set_current_menu((menu, 0))

    def manage_menu_callbacks(self, old: AbstractMenu, new: AbstractMenu):
        """
        Manage callback of menu

        Args:
            old (AbstractMenu): previous menu
            new (AbstractMenu): new menu
        """
        if old:
            old.callback_quit(self)
        if new:
            new.callback_enter(self)

    def set_previous_menu(self, stay_on_root: bool) -> bool:
        """
        Set previous menu on history

        Args:
            stay_on_root (bool): don't close if there are the last

        Returns:
            bool: True if are setted a new menu, otherwise False
        """
        if len(self._history) > 0:
            previous = self._history.pop()
            self.set_current_menu(previous)
            return True
        else:
            if not stay_on_root:
                self._current_menu = None
                return True
            return False

    def set_current_menu(self, menu: Tuple[AbstractMenu, int]) -> None:
        """
        Set current menu

        Args:
            menu (Tuple[AbstractMenu, int]): new menu set with line
        """
        _old_menu = self._current_menu

        if menu:
            self._current_menu = menu[0]
            self._current_line = menu[1]
            self._find_min_refresh()
        else:
            self._current_menu = None
            self._current_line = 0

        self.manage_menu_callbacks(_old_menu, menu[0] if menu else None)

    def _find_min_refresh(self) -> None:
        """
        Find lowest time on entry of menu
        """
        min_val = None
        for entry in self._current_menu.entry:
            if entry.refresh_min <= 0:
                continue
            if min_val is None or entry.refresh_min < min_val:
                min_val = entry.refresh_min
        if min_val:
            self._current_refresh_time = min_val
        else:
            self._current_refresh_time = self.refresh_time

    def _ping_update_menu(self):
        self._update_menu.set()

        self._end_ping_menu()

    def _end_ping_menu(self):
        # reset auto refresh
        self._reset_auto_refresh()

    def _start_show_menu(self) -> InputValue:
        Thread(target=self._show_menu_loop).start()

    def _start_input_managing(self) -> InputValue:
        Thread(target=self._wait_input_loop).start()

    def _start_auto_refresh(self) -> None:
        Thread(target=self._auto_refresh_loop).start()

    def _show_menu_loop(self) -> None:
        while self._current_menu is not None:
            _current_menu = self._current_menu
            _line = self._current_line
            self.print_text(_current_menu.generate_text(_line))

            # wait event to update menu
            self._update_menu.wait()
            self._update_menu.clear()
        self._quit()

    def _quit(self):
        """
        Close the thread and instance
        """
        self._stop = True

    def stop(self):
        """
        Stop instance
        """
        self.set_current_menu(None)
        self._ping_update_menu()

    def _wait_input_loop(self) -> None:
        while not self._stop:
            if self._stop:
                break
            in_ = self.wait_action()
            if in_:
                self.manage_action(in_)
                self._ping_update_menu()

    def _auto_refresh_loop(self) -> None:
        self._reset_auto_refresh()
        while not self._stop:
            if self._current_refresh_time <= 0:
                sleep(1)
                continue
            if time() - self._time > self._current_refresh_time:
                self._ping_update_menu()
            else:
                sleep(self._current_refresh_time/10)

    def _reset_auto_refresh(self):
        self._time = time()

    @abstractmethod
    def print_text(self, lines: List[str]) -> None:
        """
        Show the menu

        Args:
            lines (List[str]): list of string to show
        """

    def start_show(self):
        """
        Start instance thread
        """
        self._start_input_managing()
        self._start_show_menu()
        self._start_auto_refresh()
