from .jobs.sjbou02 import Sjbou02


def init():
    job_trigger = Sjbou02()

    job_trigger.get_screen()
    job_trigger.get_input_unit()
    job_trigger.set_unit()
    job_trigger.set_batch_date()
    job_trigger.get_input_job_id()
    job_trigger.load_job()
