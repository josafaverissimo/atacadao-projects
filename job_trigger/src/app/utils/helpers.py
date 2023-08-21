from datetime import datetime


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
