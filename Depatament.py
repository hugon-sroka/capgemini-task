from datetime import datetime
from Employer import Employer


class Departament(Employer):
    def __init__(self, departament):
        self.username = f'{self.last_name}_{self.first_name}_{str(datetime.now())[-6:]}'
        self.departament = departament


