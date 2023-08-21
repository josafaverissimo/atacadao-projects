import curses
from ..utils.my_curses import MyCurses
from datetime import datetime
from ..utils import helpers
from .sjbaibm import Sjbaibm


class Sjbou02:
    def __init__(self):
        self.screen_height = 24
        self.screen_width = 80
        self.curses = MyCurses(self.screen_height, self.screen_width)
        self.job_id = None
        self.unit = None
        self.unit_name = "MACEIO PETROPOLIS"
        self.batch_date = datetime.today().strftime("%d/%m/%Y")

        self.jobs = [
            Sjbaibm(self)
        ]

    def get_job_by_id(self, id):
        for job in self.jobs:
            if job.get_id() == id:
                return job

        return False

    def screen_header(self):
        logo = "[ATACADAO]"
        main_message = "SJBOU02 - DISPARADOR DE JOBS"

        borders_x = 2
        self.curses.send_message(main_message, 0, 0)
        self.curses.send_message(logo, self.screen_width - borders_x - len(logo), 0)

    def screen_input_data(self):
        begin_x = 1
        begin_y = 2
        height = 4
        width = self.screen_width - 1

        messages = [
            f"Filial.......: <{' ' * 3}> {' ' * 55}",
            f"Data Batch...: {' ' * 10} - {' ' * 5} {' ' * 18} Data Online: {' ' * 11}",
            f"Codigo do Job: <{' ' * 8}> {' ' * 50}"
        ]

        underlines = [
            {
                "x": 17,
                "y": 2,
                "blanks": 3
            },
            {
                "x": 22,
                "y": 2,
                "blanks": 55
            },
            {
                "x": 16,
                "y": 3,
                "blanks": 10
            },
            {
                "x": 29,
                "y": 3,
                "blanks": 10
            },
            {
                "x": 67,
                "y": 3,
                "blanks": 10
            },
            {
                "x": 17,
                "y": 4,
                "blanks": 8
            },
            {
                "x": 27,
                "y": 4,
                "blanks": 50
            },
        ]

        self.curses.draw_rectangle(begin_x, begin_y, height, width)

        for message in messages:
            self.curses.send_message(message, begin_x, begin_y)
            begin_y += 1

        for underline in underlines:
            self.curses.send_message(" " * underline["blanks"], underline["x"], underline["y"], curses.A_UNDERLINE)

    def screen_header_job_execution(self):
        begin_y = 6
        begin_x = 3

        columns = [
            "Seq",
            "Funcao ",
            "Descricao" + ' ' * 27,
            "Imp",
            "Ocorrencia ",
            "Descorrido"
        ]

        for column in columns:
            self.curses.send_message(column + " ", begin_x, begin_y)
            begin_x += len(column) + 1

    def screen_job_execution_rectangle(self):
        begin_x = 1
        begin_y = 8
        height = 7
        width = self.screen_width - 1
        self.curses.draw_rectangle(begin_x, begin_y, height, width)

    def screen_job_execution_parameters_rectangle(self):
        begin_x = 58
        begin_y = 15
        height = 7
        width = self.screen_width - 1
        self.curses.draw_rectangle(begin_x, begin_y, height, width)

    def set_job_execution_sequence(self, y, sequence):
        begin_x = 6 - len(sequence)
        self.curses.send_message(sequence, begin_x, y)

    def set_job_execution_function(self, y, function):
        begin_x = 7
        self.curses.send_message(function, begin_x, y)

    def set_job_execution_description(self, y, description):
        begin_x = 15
        self.curses.send_message(description, begin_x, y)

    def set_job_execution_printer(self, y, printer):
        begin_x = 55 - len(printer)
        self.curses.send_message(printer, begin_x, y)

    def set_job_execution_status(self, y):
        begin_y = 8 + y
        begin_x = 56
        message = "EM PROCESSO"
        self.curses.send_message(message, begin_x, begin_y)

    def set_job_execution_time(self, y, time):
        begin_y = 8 + y
        begin_x = 68
        time = f'[{time}]'
        self.curses.send_message(time, begin_x, begin_y)

    def insert_job_execution_row(self, y, sequence, function, description, printer):
        begin_y = 8 + y
        self.set_job_execution_sequence(begin_y, sequence)
        self.set_job_execution_function(begin_y, function)
        self.set_job_execution_description(begin_y, description)
        self.set_job_execution_printer(begin_y, printer)
        # self.set_job_execution_status(begin_y)
        # self.set_job_execution_time(begin_y, time)

    def clear_command_execution_description(self):
        begin_x = 1
        begin_y = 15
        self.curses.send_message(" " * 56, begin_x, begin_y)
        self.curses.send_message(" " * 56, begin_x, begin_y + 1)


    def set_command_execution_description_function(self, command_name, command_description, sequence):
        begin_y = 15
        begin_x = 1

        message_function = f"FUNCAO: <{command_name}> {command_description}"
        message_sequence = f"SEQ...: {sequence}"

        self.curses.send_message(message_function, begin_x, begin_y)
        self.curses.send_message(message_sequence, begin_x, begin_y + 1)

    def get_confirmation_execution(self):
        self.insert_confirm_execution()

        confirmation = ""

        while confirmation not in ["S", "N"]:
            confirmation = self.curses.get_user_input(40, 22, 1)

        return confirmation

    def wait_command_execution(self):
        self.clear_command_execution_description()
        begin_y = 16
        message = "*** A G U A R D E ***"
        begin_x = 18

        self.curses.send_message(message, begin_x, begin_y)
        self.curses.move_cursor(80, 22)

    def insert_confirm_execution(self):
        begin_x = 1
        begin_y = 21
        message = "DESEJA EXECUTAR O COMANDO ACIMA (?): [ ] (S=Sim / N=Nao)"

        self.curses.send_message(message, begin_x, begin_y)

        stdscr = self.curses.get_stdscr()
        stdscr.addstr(23, 2, "[MENSAGEM:]")
        stdscr.refresh()

    def screen_set_version(self):
        stdscr = self.curses.get_stdscr()
        stdscr.addstr(2, 71, "(v.3)")
        stdscr.refresh()

    def set_parameters(self, fil1, fil2, num1, num2, int1, int2):
        begin_x = 59
        begin_y = 15
        i = 1

        parameters = [
            {
                "name": "Fil1",
                "value": fil1
            },
            {
                "name": "Fil2",
                "value": fil2
            },
            {
                "name": "Num1",
                "value": num1
            },
            {
                "name": "Num2",
                "value": num2
            },
            {
                "name": "Int1",
                "value": int1
            },
            {
                "name": "Int2",
                "value": int2
            }
        ]

        for parameter in parameters:
            message = parameter["name"] + ":"
            blanks = 14 - len(parameter['value'])
            message += " " * blanks
            message += parameter['value']
            self.curses.send_message(message, begin_x, begin_y)
            begin_y += 1

    def get_user_input_unit(self):
        unit = ""
        while not unit.isdigit():
            unit = self.curses.get_user_input(18, 3, 3)

        return unit

    def get_user_input_job_id(self):
        job_id = self.curses.get_user_input(18, 5, 7)

        return job_id

    def load_job(self):
        begin_x = 27
        begin_y = 4
        job = self.get_job_by_id(self.job_id)

        while not job:
            message = "JOB INEXISTENTE"
            self.curses.send_message(message, begin_x, begin_y)
            job_id = self.get_user_input_job_id()
            job = self.get_job_by_id(job_id)

        message = job.get_description()
        self.curses.send_message(message, begin_x, begin_y)

        job.execute()

    def get_user_input(self):
        self.unit = self.get_user_input_unit()

        self.set_batch_date()
        self.set_unit()

        self.job_id = self.get_user_input_job_id()

        self.load_job()

    def get_screen(self) -> None:
        self.curses.main_window_borders()
        self.screen_header()
        self.screen_input_data()
        self.screen_header_job_execution()
        self.screen_job_execution_rectangle()
        self.screen_job_execution_parameters_rectangle()
        self.screen_confirm_execution_rectangle()
        self.screen_set_version()

        self.get_user_input()

        self.curses.end()

    def screen_confirm_execution_rectangle(self):
        begin_x = 1
        begin_y = 21
        height = 2
        width = 58
        self.curses.draw_rectangle(begin_x, begin_y, height, width)

    def set_batch_date(self):
        begin_x = 16
        begin_y = 3
        self.curses.send_message(f'{self.batch_date} - {helpers.weekday()}', begin_x, begin_y)

        self.curses.send_message(f'{self.batch_date}', 67, begin_y)

    def set_unit(self):
        begin_x = 22
        begin_y = 2
        self.curses.send_message(self.unit_name, begin_x, begin_y)
