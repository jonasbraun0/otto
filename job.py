import datetime
import os

class Job:
    def __init__(self, name):
        this.job_id = generate_job_id()
        generate_results_folder()
        this.job_name = name

    def generate_job_id():
        return now.isoformat()

    def generate_results_folder():
        os.mkdir("%s/%s-%s"%(otto.results_dir, job_name, job_id))

