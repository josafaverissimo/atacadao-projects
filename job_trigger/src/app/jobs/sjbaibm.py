from ..utils import helpers
from time import sleep


class Sjbaibm:
    def __init__(self, sjbou02):
        self.sjbou02 = sjbou02
        self.id = "SJBAIBM"
        self.description = "PROCESSA ALTERACAO DE PRECO SASBU07 PARCIAL"
        self.option = "S"
        self.commands = [
            {
                "sequence": "25",
                "function": "SASBU07",
                "description": "DADOS PROD. GERAIS PARA TRANSMI",
                "printer": "0"
            },
            {
                "sequence": "50",
                "function": "SASBI51",
                "description": "GERA ARQ.TXTITENS PARA BALANCA TOLED",
                "printer": "0"
            },
            {
                "sequence": "75",
                "function": "SASBI81",
                "description": "GERA ARQUIVO XML DE PRODUTOS - RUB",
                "printer": "0"
            }
        ]

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def show_commands(self):
        line = 0
        for command in self.commands:
            self.sjbou02.insert_job_execution_row(
                line,
                command["sequence"],
                command["function"],
                command["description"],
                command["printer"]
            )

            line += 1

    def execute(self):
        self.show_commands()
        line = 0

        for command in self.commands:
            self.sjbou02.clear_command_execution_description()
            self.sjbou02.set_command_execution_description_function(
                command["function"],
                command["description"],
                command["sequence"]
            )

            self.sjbou02.set_parameters("273", "0", "0,0000", "0,0000", "0", "0")

            confirmation = self.sjbou02.get_confirmation_execution()

            if confirmation == "S":
                self.sjbou02.set_job_execution_status(line)
                self.sjbou02.wait_command_execution()
                sleep(6)
                self.sjbou02.set_job_execution_time(line, "00:00:12")

                line += 1
            elif confirmation == "N":
                break
