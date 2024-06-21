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
        '''Returns the current time as a string'''
        current_time = datetime.datetime.now()
        try:
            return current_time.strftime(self.time_format)
        except Exception as e:
            print(f"Error: {e}")
            return current_time.strftime("%Y.%m.%d %H:%M:%S")

    def __log_to_file(self, content: str):
        '''Appends file'''
        with open(self.file_path, "a", encoding = self.encoding) as file:
            file.write(content)

    def log(self, content: str = "") -> None:
        '''Logs content to file'''
        content = self.__str_time() + self.separator + str(content) + "\n"
        print(content.strip())
        self.__log_to_file(content)

    def change_path(self, file_path: str) -> str:
        '''Changes the log file path'''
        if file_path:
            self.file_path = file_path
            return f"Changed path from {self.file_path} to {file_path}"
        return "No path provided"

    def change_encoding(self, encoding: str) -> str:
        '''Changes the log file encoding'''
        if encoding:
            self.encoding = encoding
            return f"Changed encoding to {encoding}"
        return "No encoding provided"

    def change_time_format(self, time_format: str) -> str:
        '''Changes the time format'''
        if time_format:
            self.time_format = time_format
            return f"Changed time format to {time_format}"
        return "No time format provided"

    def change_separator(self, separator: str) -> str:
        '''Changes the separator'''
        if separator:
            self.separator = separator
            return f"Changed separator to {separator}"
        return "No separator provided"

    def read(self) -> str:
        '''Reads the log file'''
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding=self.encoding) as file:
                lines = file.readlines()
                return "".join(lines)
        return "Log file does not exist"
    
    def read_list(self) -> list:
        '''Reads the log file as a list'''
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding=self.encoding) as file:
                lines = file.readlines()
                return lines
        return ["Log file does not exist"]

    def clear(self) -> str:
        '''Clears the log file'''
        if os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding=self.encoding) as file:
                return "Log file cleared"
        return "Log file does not exist"

    def remove(self) -> str:
        '''Removes the log file'''
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            return "Log file removed"
        return "Log file does not exist"
