# task 8


class FileManager:

    def __init__(self, file_name):
        self.file_name = file_name
        print('FileManager initiated.')

    def update_file(self, text_data):
        with open(self.file_name, 'a+') as file:
            file.write(text_data)

    def read_file(self):
        with open(self.file_name, 'r') as file:
            return file.read()