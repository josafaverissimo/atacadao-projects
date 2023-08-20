from ..utils import helpers
from time import sleep


class Sjbaibm:
    def __init__(self):
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

    def show_commands(self):
        line = 9
        for command in self.commands:
            helpers.move_cursor(line, 5)

            row = f'{command["sequence"]} {command["function"]} {command["description"]}'
            blanks = 40 - len(command["description"])
            row += " " * blanks + command["printer"]
            print(row)

            line += 1

    def show_parameters(self):
        parameters = [
            {
                "name": "Fil1",
                "value": "273"
            },
            {
                "name": "Fil2",
                "value": "0"
            },
            {
                "name": "Num1",
                "value": "0,0000"
            },
            {
                "name": "Num2",
                "value": "0,0000"
            },
            {
                "name": "Int1",
                "value": "0"
            },
            {
                "name": "Int2",
                "value": "0"
            }
        ]
        line = 16

        for parameter in parameters:
            helpers.move_cursor(line, 60)
            blanks = 12 - len(parameter['value'])
            row = f"| {parameter['name']}:"
            row += " " * blanks + parameter['value']
            print(row)
            line += 1

    def detail_command(self, command):
        helpers.move_cursor(16, 3)
        print(f"FUNCAO: <{command['function']}> {command['description']}")

        helpers.move_cursor(17, 3)
        print(f"SEQ...: {command['sequence']}")

        helpers.move_cursor(20, 3)
        print("-" * 57)

    def confirm_execution(self):
        helpers.move_cursor(21, 3)
        print("DESEJA EXECUTAR O COMANDO ACIMA (?): [ ] (S=Sim / N=Nao)")

        helpers.move_cursor(21, 41)
        self.opt = str(input())

    def clear_detail(self):
        helpers.move_cursor(16, 3)
        print(" " * 57)
        helpers.move_cursor(17, 3)
        print(" " * 10)

    def execute(self):
        line = 9
        for command in self.commands:
            self.clear_detail()
            self.detail_command(command)
            self.show_parameters()
            self.confirm_execution()

            if self.option == "S":
                self.clear_detail()

                helpers.move_cursor(16, 28)
                print("***  A G U A R D E  ***")

                helpers.move_cursor(line, 58)
                print("EM PROCESSO")

                helpers.move_cursor(22, 80)
                sleep(6)

                line += 1
            else:
                return
        return