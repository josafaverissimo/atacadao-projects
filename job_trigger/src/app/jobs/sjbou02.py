import os
from datetime import datetime
from ..utils import helpers
from .sjbaibm import Sjbaibm



class Sjbou02:
    def __init__(self):
        self.job_id = None
        self.unit = None
        self.unit_name = "MACEIO PETROPOLIS"
        self.batch_date = datetime.today().strftime("%d/%m/%Y")

        self.jobs = {
            "SJBAIBM": Sjbaibm()
        }

    def get_screen(self) -> None:
        current_dir = os.path.dirname(__file__)
        sjbou02_screen = open(f'{current_dir}/sjbou02.txt')

        for line in sjbou02_screen.readlines():
            print(line, end="")

    def set_batch_date(self):
        helpers.move_cursor(4, 18)
        print(f'{self.batch_date} - {helpers.weekday()}')

        helpers.move_cursor(4, 68)
        print(f'{self.batch_date}')

    def set_unit(self):
        helpers.move_cursor(3, 25)
        blanks = 53 - len(self.unit_name)
        print(self.unit_name + " " * blanks)
            
    def get_input_unit(self) -> None:
        helpers.move_cursor(3, 19)
        self.unit = int(input())

    def get_input_job_id(self) -> None:
        helpers.move_cursor(5, 19)
        self.job_id = str(input())

    def load_job(self):
        helpers.move_cursor(5, 29)
        print(helpers.get_job_description_by_id(self.job_id))

        job = self.jobs[self.job_id]

        job.show_commands()
        job.execute()
