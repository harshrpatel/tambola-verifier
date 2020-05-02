import ast


class BoardStored:
    my_stored_board = list()

    @classmethod
    def get_from_file(cls, file_path):
        with open(file_path, "r") as r_file:
            lines = r_file.readlines()
            for line in lines:
                obj = ast.literal_eval(line)
                if isinstance(obj, list):
                    cls.my_stored_board = obj
