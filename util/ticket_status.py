from termcolor import colored


class TicketStatus:
    registered_numbers = list()
    ticket = list()
    pattern_dict = dict()
    pattern_dict_completion_flags = dict()

    @classmethod
    def initialize(cls, registered_numbers=None, ticket=None, patterns_dict=None):
        cls.registered_numbers = registered_numbers
        cls.ticket = ticket
        cls.pattern_dict = patterns_dict
        for key in patterns_dict:
            cls.pattern_dict_completion_flags[key] = False

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

        if len(ticket[0]) > 2:
            ljust_len = 25
        else:
            ljust_len = 5

        print(colored("My Ticket: ", "cyan"))
        for i, cell in enumerate(ticket):
            if i in [4, 9, 14, 19, 24]:
                if cell in registered_numbers_set:
                    print(colored(cell.ljust(ljust_len), "red"))
                else:
                    print(cell.ljust(ljust_len))
            else:
                if cell in registered_numbers_set:
                    print(colored(cell.ljust(ljust_len), "red"), end=" "*8)
                else:
                    print(cell.ljust(ljust_len), end=" "*8)

        print(colored("\nPatterns and your numbers:", "cyan"))
        for key, value in patterns_dict.items():
            print(key.ljust(20), end=" ")
            for pattern_value in value:
                if pattern_value in registered_numbers_set:
                    print(colored(pattern_value, "red"), end=" --- ")
                else:
                    print(pattern_value, end=" --- ")
            print("")

    @classmethod
    def strike_through(cls, cell):
        result = ''
        for c in str(cell):
            result = result + c + '\u0336'
        return result

