#!/usr/bin/python3
from time import sleep



class ProgressBar(object):
    """
    Class to represent Progress Bar
    """
    def __init__(self, prefix='', suffix='', decimals=1, length=100, fill='█') -> None:
        super().__init__()

        self.iteration = 0
        self.total = 0
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.status = "FAIL"

    def print_bar(self):
        """
        Prints progress bar
        :return:
        """
        # get percentage
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (self.iteration / float(self.total)))
        # get the length
        filled_length = int(self.length * self.iteration // self.total)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        print('\r%s |%s| %s%% %s' % (self.prefix, bar, percent, self.suffix), end='\r')
        # Print New Line on Complete
        if self.iteration == self.total:
            print()

    def show(self):
        """
        Loop around to simpulate progress bar
        :return: void
        """
        items = list(range(0, 57))
        self.iteration = 0
        self.total = len(items)

        for item in items:
            sleep(0.01)
            self.iteration += 1
            self.print_bar()

        self.iteration = 0
        self.total = 0