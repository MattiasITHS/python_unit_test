class Profile:
    def __init__(self, name, age, job):
        self._age = age
        self._name = name
        self._job = job

    def print_name(self):
        print(self._name)

    def print_job(self):
        print(self._job)

    def print_age(self):
        print(self._age)


profile = Profile("Mattias", 35, "Tester")
profile.print_name()
profile.print_age()
profile.print_job()