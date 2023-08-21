from .jobs.sjbou02 import Sjbou02


def init():
    job_trigger = Sjbou02()

    job_trigger.get_screen()
