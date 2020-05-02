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

        print(colored("BOARD:", "cyan"))

        for i, cell in enumerate(current_board):
            if cell in registered_numbers_set:
                if i % 10 == 9:
                    print(colored(cell.ljust(10), "green"))
                else:
                    print(colored(cell.ljust(10), "green"), end=" " * 8)
            else:
                if i % 10 == 9:
                    print(cell.ljust(10))
                else:
                    print(cell.ljust(10), end=" "*8)

        print("\nThe numbers came in this order: ", registered_numbers)
