'''A simple logger'''

import os
import datetime

class Logger:
    '''A simple logger class'''
    def __init__(
            self,
            file_path: str = os.path.join(os.getcwd(), "log.txt"),
            encoding: str = "utf-8-sig",
            time_format: str = "%Y.%m.%d %H:%M:%S",
            separator: str = "\t"
        ):
        self.file_path = file_path
        self.encoding = encoding
        self.time_format = time_format
        self.separator = separator

    def __str__(self) -> str:
        return f"Log file: {self.file_path}"

    def __str_time(self) -> str:
        current_time = datetime.datetime.now()
        try:
            return current_time.strftime(self.time_format)
        except Exception as e:
            print(f"Error: {e}")
            return current_time.strftime("%Y.%m.%d %H:%M:%S")

    def __log_to_file(self, content: str):
        with open(self.file_path, "a", encoding = self.encoding) as file:
            file.write(content)

    def log(self, content: str = "") -> None:
        '''Log content to file'''
        content = self.__str_time() + self.separator + str(content) + "\n"
        print(content)
        self.__log_to_file(content)

    def change_path(self, file_path: str) -> str:
        '''Change the log file path'''
        if file_path:
            self.file_path = file_path
            return f"Changed path from {self.file_path} to {file_path}"
        return "No path provided"

    def change_encoding(self, encoding: str) -> str:
        '''Change the log file encoding'''
        if encoding:
            self.encoding = encoding
            return f"Changed encoding to {encoding}"
        return "No encoding provided"

    def change_time_format(self, time_format: str) -> str:
        '''Change the time format'''
        if time_format:
            self.time_format = time_format
            return f"Changed time format to {time_format}"
        return "No time format provided"

    def change_separator(self, separator: str) -> str:
        '''Change the separator'''
        if separator:
            self.separator = separator
            return f"Changed separator to {separator}"
        return "No separator provided"
