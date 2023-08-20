from os import system
from datetime import datetime

def move_cursor(y, x):
    y -= 1
    x -= 1
    system(f"tput cup {y} {x}")


def weekday() -> str:
    weekday_number = datetime.today().weekday()
    weekday_by_number = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    }

    return weekday_by_number[weekday_number]


def get_job_description_by_id(job_id: str) -> str:
    job_description_by_id = {
        "SJBAIBM": "PROCESSA ALTERACAO DE PRECO SASBU07 PARCIAL"
    }
    job_description = job_description_by_id[job_id]

    blanks = 49 - len(job_description)

    return job_description + " " * blanks
