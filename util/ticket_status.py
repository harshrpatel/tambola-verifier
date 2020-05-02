from termcolor import colored


class TicketStatus:
    registered_numbers = list()
    ticket = list()
    pattern_dict = dict()

    @classmethod
    def initialize(cls, registered_numbers=None, ticket=None, patterns_dict=None):
        cls.registered_numbers = registered_numbers
        cls.ticket = ticket
        cls.pattern_dict = patterns_dict

    @classmethod
    def print_ticket_status(cls, registered_numbers=None, ticket=None, patterns_dict=None):
        if registered_numbers is None:
            registered_numbers = cls.registered_numbers
        if ticket is None:
            ticket = cls.ticket
        if patterns_dict is None:
            patterns_dict = cls.pattern_dict

        if registered_numbers is None:
            registered_numbers_set = set()
        else:
            registered_numbers_set = set(registered_numbers)

        print(colored("My Ticket: ", "cyan"))
        for i, cell in enumerate(ticket):
            if i in [4, 9, 14, 19, 24]:
                if cell in registered_numbers_set:
                    print(colored(cls.strike_through(cell.ljust(10)), "red"))
                else:
                    print(cell.ljust(10))
            else:
                if cell in registered_numbers_set:
                    print(colored(cls.strike_through(cell.ljust(10)), "red"), end=" "*8)
                else:
                    print(cell.ljust(10), end=" "*8)

        print(colored("\nPatterns and your numbers:", "cyan"))
        for key, value in patterns_dict.items():
            print(key.ljust(20), end=" ")
            for pattern_value in value:
                if pattern_value in registered_numbers_set:
                    print(colored(cls.strike_through(pattern_value), "red"), end=" ")
                else:
                    print(pattern_value, end=" ")
            print("")

    @classmethod
    def strike_through(cls, cell):
        result = ''
        for c in str(cell):
            result = result + c + '\u0336'
        return result

