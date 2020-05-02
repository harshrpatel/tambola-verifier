import ast


class TicketStored:
    my_stored_ticket = list()
    my_stored_pattens = dict()

    @classmethod
    def get_from_file(cls, file_path):
        with open(file_path, "r") as r_file:
            lines = r_file.readlines()
            for line in lines:
                obj = ast.literal_eval(line)
                if isinstance(obj, list):
                    cls.my_stored_ticket = obj
                elif isinstance(obj, dict):
                    cls.my_stored_pattens = obj
