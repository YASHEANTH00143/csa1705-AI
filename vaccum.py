class VacuumCleaner:

    def __init__(self, environment):

        self.environment = environment

        self.location = 0

    def move_left(self):

        if self.location > 0:

            self.location -= 1

    def move_right(self):

        if self.location < len(self.environment) - 1:

            self.location += 1

    def clean(self):

        if self.environment[self.location] == 'dirty':

            self.environment[self.location] = 'clean'

    def run(self):

        for i in range(len(self.environment)):

            print(f"Location: {self.location}, Current state: {self.environment}")

            self.clean()

            self.move_right() if i % 2 == 0 else self.move_left()

environment = ['dirty', 'clean', 'dirty', 'clean', 'dirty']

vacuum_cleaner = VacuumCleaner(environment)

vacuum_cleaner.run()
