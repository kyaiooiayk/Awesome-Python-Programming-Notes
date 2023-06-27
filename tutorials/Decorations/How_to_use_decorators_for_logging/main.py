from log_decorator import logger
import log


class Calculator:
    def __init__(self, first=0, second=0, log_file_name="", log_file_dir=""):
        self.first = first
        self.second = second
        self.log_file_name = log_file_name
        self.log_file_dir = log_file_dir

        # Initializing logger object to write custom logs
        self.logger_obj = log.get_logger(
            log_file_name=self.log_file_name, log_dir=self.log_file_dir
        )

    @logger
    def sum(self, first=0, second=0):
        """Sum

        Sum two numbers.
        """

        result = self.first + self.second
        # This message is set as info and is specific to this method
        self.logger_obj.info("Results is: " + str(result))
        return result


if __name__ == "__main__":

    import os

    if os.path.exists("./log.log"):
        os.remove("./log.log")

    calculator = Calculator(5, 0, "log")
    calculator.sum(first=2, second=3)
