import curses
from curses.textpad import rectangle

class MyCurses:
    def __init__(self, height, width):
        self.stdscr = curses.initscr()
        curses.cbreak()
        self.stdscr.keypad(True)
        curses.noecho()

        self.main_height = height
        self.main_width = width
        self.begin_y = 0
        self.begin_x = 0
        self.main_window = curses.newwin(height - 2, width - 2, 1, 1)

    def draw_rectangle(self, x, y, height, width):
        rectangle(self.stdscr, y, x, y + height, width)
        self.stdscr.refresh()

    def main_window_borders(self):
        self.draw_rectangle(0, 0, self.main_height, self.main_width)

    def send_message(self, message, x, y, style=curses.A_NORMAL):
        self.main_window.addstr(y, x, message, style)
        self.main_window.refresh()

    def get_stdscr(self):
        return self.stdscr

    def get_user_input(self, x, y, length: int = None):
        curses.echo()

        user_input = self.stdscr.getstr(y, x, length)

        curses.noecho()

        return user_input.decode("utf-8")

    def move_cursor(self, x, y):
        self.stdscr.addstr(y, x, "")
        self.stdscr.refresh()

    def end(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
