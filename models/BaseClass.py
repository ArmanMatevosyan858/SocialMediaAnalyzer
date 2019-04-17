from configurations import config


class BaseClass:
    """
    Base Class of the project
    """

    @staticmethod
    def display(message):
        """
        Displaying message in the terminal
        :param message:
        :return:
        """

        print("INFO:\t\t" + str(message))

    @staticmethod
    def debug(message):
        """
        The method is displaying message in the terminal when debug mode is turned ON
        :param message:
        :return:
        """

        if config.DEBUG_MODE:
            print("DEBUG:\t\t" + str(message))

    @staticmethod
    def error(message):
        """
        Displaying message in the terminal
        :param message:
        :return:
        """

        print("ERROR:\t\t" + str(message))

    @staticmethod
    def warning(message):
        """
        Displaying message in the terminal
        :param message:
        :return:
        """

        print("WARNING:\t\t" + str(message))

    @staticmethod
    def generate_url(list_of_values):
        """
        Method generates final url
        :param list_of_values:
        :return:
        """

        final_url = ""
        for value in list_of_values:
            final_url += "/" + value

        return final_url[1:]
