from termcolor import colored


class BoardStatus:
    registered_numbers = list()
    current_board = list()

    @classmethod
    def initialize(cls, registered_numbers=None, current_board=None):
        cls.registered_numbers = registered_numbers
        cls.current_board = current_board

    @classmethod
    def print_board_status(cls, registered_numbers=None, current_board=None):
        if registered_numbers is None:
            registered_numbers = cls.registered_numbers
        if current_board is None:
            current_board = cls.current_board
        if registered_numbers is None:
            registered_numbers_set = set()
        else:
            registered_numbers_set = set(registered_numbers)

        if len(current_board[0]) > 2:
            ljust_len = 25
        else:
            ljust_len = 10

        print(colored("BOARD:", "cyan"))

        for i, cell in enumerate(current_board):
            if cell in registered_numbers_set:
                if i % 10 == 9:
                    print(colored(cell.ljust(ljust_len), "green"))
                else:
                    print(colored(cell.ljust(ljust_len), "green"), end=" ")
            else:
                if i % 10 == 9:
                    print(cell.ljust(ljust_len))
                else:
                    print(cell.ljust(ljust_len), end=" ")

        print("\nThe numbers came in this order: ", registered_numbers)
