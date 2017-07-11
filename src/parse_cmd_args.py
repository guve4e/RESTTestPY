
class CmdArgumentsParser(object):
    """
    This class parses the command line arguments
    supplied form user.
    It has 3 attributes:
        1.  project_name: String, the name of the project.
        2.  filter_keyword: String, if the user wants to filter test cases by word.
        3.  verbose: Boolean, if the user wants verbose info or not.
    """

    def __init__(self, args) -> None:
        super().__init__()

        # attributes
        self.__project_name = self.__filter_keyword = None
        self.__verbose = False

        # methods
        self.__validate_args(args)
        self.__retrieve_project_name(args)
        verbose_and_keyword_list = self.__sanitize_arg_list(args)
        self.__retrieve_verbose_and_keyword(verbose_and_keyword_list)

    @property
    def project_name(self):
        return self.__project_name

    @project_name.setter
    def project_name(self, value):
        self.__project_name = value

    @property
    def filter_keyword(self):
        return self.__filter_keyword

    @filter_keyword.setter
    def filter_keyword(self, value):
        self.__filter_keyword = value

    @property
    def verbose(self):
        return self.__verbose

    @verbose.setter
    def verbose(self, value):
        self.__verbose = value

    @classmethod
    def __validate_args(cls, args):
        """
        Validates args array
        :raise Exception if the array length is less than 2
        """
        len_args = len(args)

        if len_args < 2:
            raise Exception("Project Name Must Be Specified")

        if len_args > 4:
            raise Exception("Too many arguments")

    def __retrieve_project_name(self, args):
        """
        It extracts the second element
        from the parameter args array
        :param args: args array
        """

        self.project_name = args[1]

    def __retrieve_verbose_and_keyword(self, verbose_and_keyword_list):
        """
        Extracts the verbose and keyword from args list.
        It changes the state of the object.
        :param verbose_and_keyword_list:
        :return: void
        """

        # if we do not have verbose and keyword
        # exit early
        if not verbose_and_keyword_list:
            return

        # copy the parameter list into a different one,
        # to avoid touching the reference
        new_verbose_and_keyword_list = verbose_and_keyword_list[:]

        # loop trough the list
        # at this point the list is with max len of 2
        for list_elem in new_verbose_and_keyword_list:

            # if verbose element found
            # assign it to attribute verbose
            # and remove that element, so
            # the one left element is assigned to
            # the filter_keyword attribute
            if list_elem == "-v" or list == "-verbose":
                self.verbose = True
                index = new_verbose_and_keyword_list.index(list_elem)
                del new_verbose_and_keyword_list[index]
                if len(new_verbose_and_keyword_list) >= 1:
                    self.filter_keyword = new_verbose_and_keyword_list[0]

        if self.verbose is False:
            # At this point verbose element was not found
            # If there are more than one element in the list, something is wrong
            if len(new_verbose_and_keyword_list) > 1:
                raise Exception("Wrong Cmd Arguments")
            # if only one element left, it must be the keyword
            self.filter_keyword = new_verbose_and_keyword_list[0]

    @classmethod
    def __sanitize_arg_list(self, args):
        """
        Deletes the first and second element
        from the args array if the args list len
        is more than 2
        :param args: args array
        :return: list containing strings representing
        verbose and filter keyword parameters
        """

        # if args len is not more than 2
        # than we do not need to sanitize
        if len(args) > 2:
            # since args is reference to some list
            # somewhere else, make a new list verbose_and_keyword
            verbose_and_keyword = list(args)

            # then delete the first two elements
            del verbose_and_keyword[0]
            del verbose_and_keyword[0]

            return verbose_and_keyword
