#!/usr/bin/python3
from time import sleep


class ProgressBar(object):
    """
    Class to represent Progress Bar
    """
    def __init__(self, prefix='', suffix='', decimals=1, length=100, fill='█') -> None:
        """
        Constructor
        :param prefix: 
        :param suffix: 
        :param decimals: 
        :param length: 
        :param fill: 
        """
        super().__init__()

        self.__iteration = 0
        self.__total = 57
        self.__sleep_time = 0.1
        self.__prefix = prefix
        self.__suffix = suffix
        self.__decimals = decimals
        self.__length = length
        self.__fill = fill

    def __print_bar(self):
        """
        Prints progress bar
        :return:
        """
        # get percentage
        percent = ("{0:." + str(self.__decimals) + "f}").format(100 * (self.__iteration / float(self.__total)))
        # get the length
        filled_length = int(self.__length * self.__iteration // self.__total)
        bar = self.__fill * filled_length + '-' * (self.__length - filled_length)
        print('\r%s |%s| %s%% %s' % (self.__prefix, bar, percent, self.__suffix), end='\r')
        # Print New Line on Complete
        if self.__iteration == self.__total:
            print()

    def show(self):
        """
        Loop around to simulate progress bar
        :return: void
        """
        self.__iteration = 0
        self.__total = 57

        for item in range(self.__total):
            sleep(0.01)
            self.__iteration += 1
            self.__print_bar()

        self.__iteration = 0
        self.__total = 0

