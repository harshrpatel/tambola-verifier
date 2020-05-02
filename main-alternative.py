import ast
from os import system
from os import path
from termcolor import colored


class Checker:
    my_ticket = set()
    sorted_ticket = list()
    patterns_dict = dict()
    input_stream_from_host = set()
    patterns_dict_flags = dict()
    show_board_in_order = list()

    @classmethod
    def get_input_ticket_numbers(cls):
        first_time_flag = True
        done_with_input = False
        remove_numbers_flag = False
        while not done_with_input:
            if first_time_flag:
                response = input("Please enter the comma separated numbers here: ")
                first_time_flag = False
            else:
                response = input("Please enter the remaining numbers or numbers to remove(if chosen this option): ")
            response_list = filter(None, [int(x.strip()) for x in response.split(",")])
            if remove_numbers_flag:
                cls.my_ticket = cls.my_ticket - set(response_list)
            else:
                cls.my_ticket = cls.my_ticket.union(set(response_list))
            cls.sorted_ticket = sorted(list(cls.my_ticket))
            print("my ticket: ", cls.sorted_ticket)
            is_done = input("Does you ticket look fine?\n1. Type yes for done\n2. no for adding more numbers\n3. "
                            "remove for removing numbers from you ticket: ")
            if is_done == "yes":
                done_with_input = True
            elif is_done == "remove":
                remove_numbers_flag = True
            else:
                remove_numbers_flag = False

    @classmethod
    def get_input_winning_patterns(cls):
        system("clear")
        print("Now we enter the winning patterns")
        done_with_all_patterns = False
        done_with_individual_pattern = False
        while not done_with_all_patterns:
            have_more_pattens = input("Do you have patterns to add? Type yes/no: ")
            if have_more_pattens == "yes":
                done_with_individual_pattern = False
            else:
                done_with_all_patterns = True
                done_with_individual_pattern = True
            while not done_with_individual_pattern:
                pattern_name = input("Enter the pattern name: ")
                print("Ok, setting the pattern name as ", pattern_name)
                input_for_pattern_done = False
                while not input_for_pattern_done:
                    input_for_pattern = input("Enter the numbers for this pattern: ")
                    pattern_set = set(filter(None, [int(x.strip()) for x in input_for_pattern.split(",")]))
                    print("does this pattern for " + pattern_name + " look fine? ", pattern_set)
                    patten_done = input("Type yes for done, if not, sorry you would have retype all the "
                                        "numbers again for this pattern: ")
                    if patten_done == "yes":
                        done_with_individual_pattern = True
                        input_for_pattern_done = True
                        cls.patterns_dict[pattern_name] = pattern_set
            system("clear")
            print(cls.patterns_dict)

        for k in cls.patterns_dict:
            cls.patterns_dict_flags[k] = False

    @classmethod
    def generate_ticket_txt(cls):
        with open("my_ticket2.txt", "w") as wfile:
            wfile.write(str(cls.my_ticket) + "\n")
            wfile.write(str(cls.sorted_ticket) + "\n")
            wfile.write(str(cls.patterns_dict))

    @classmethod
    def pass_the_variables_from_file(cls, ticket_from_file=None, sorted_from_file=None, patterns_from_file=None):
        if ticket_from_file is None:
            ticket_from_file = set()
        if sorted_from_file is None:
            sorted_from_file = list()
        if patterns_from_file is None:
            patterns_from_file = dict()
        cls.my_ticket = ticket_from_file
        cls.sorted_ticket = sorted_from_file
        cls.patterns_dict = patterns_from_file

        for k in cls.patterns_dict:
            cls.patterns_dict_flags[k] = False

    @classmethod
    def print_status(cls, ticket=None, patterns=None):
        if ticket is None:
            ticket = cls.sorted_ticket
        if patterns is None:
            patterns = cls.patterns_dict
        print(colored("My Ticket: ", "cyan"))
        for i, num in enumerate(ticket):

            num_str = str(num).zfill(2)

            if i in [4, 9, 14, 19, 24]:
                if num in cls.input_stream_from_host:
                    print(colored(cls.strike_through(num_str), "red"))
                else:
                    print(num_str)
            else:
                if num in cls.input_stream_from_host:
                    print(colored(cls.strike_through(num_str), "red"), end=" " * 8)
                else:
                    print(num_str, end=" " * 8)

        print(colored("\nPatterns and your numbers:", "cyan"))
        for k, v in patterns.items():
            print(k.ljust(20), end=" ")
            for pnum in v:
                if pnum in cls.input_stream_from_host:
                    print(colored(cls.strike_through(pnum), "red"), end=" ")
                else:
                    print(pnum, end=" ")
            print()

    @classmethod
    def strike_through(cls, num):
        result = ''
        for c in str(num):
            result = result + c + '\u0336'
        return result

    @classmethod
    def print_board(cls):
        print(colored("BOARD:", "cyan"))
        for i in range(1, 91):
            if i in cls.input_stream_from_host:
                if i % 10 == 0:
                    print(colored(str(i).zfill(2), "green"))
                else:
                    print(colored(str(i).zfill(2), "green"), end=" " * 8)
            else:
                if i % 10 == 0:
                    print(str(i).zfill(2))
                else:
                    print(str(i).zfill(2), end=" " * 8)
        print("\nThe numbers came in this order: ", cls.show_board_in_order)

    @classmethod
    def verify_input(cls):
        game_over_flag = False
        while not game_over_flag:
            try:
                print("")
                input_during_game = input("Enter the number from host: ")
                if input_during_game == "gg":
                    print(colored("Good Game!!!", "blue"))
                    game_over_flag = True
                elif input_during_game == "show_order":
                    system("clear")
                    print("The numbers came in this order: ", cls.show_board_in_order)
                elif input_during_game in cls.patterns_dict_flags:
                    cls.patterns_dict_flags[input_during_game] = True
                    print(colored("marking this pattern as done,we wont be notifying you on completion of this pattern",
                                  "yellow"))
                else:
                    input_number = int(input_during_game)
                    cls.input_stream_from_host.add(input_number)
                    cls.show_board_in_order.append(input_number)
                    system("clear")
                    cls.print_board()
                    if input_number in cls.my_ticket:
                        print(colored("\n--------- Mark the ticket, {} is on your ticket --------".format(input_number),
                                      "yellow"))
                    else:
                        print(colored("\n--------- Never Mind, {} was not on your ticket --------".format(input_number),
                                      "magenta"))
                    print("")
                    cls.print_status()
                    cls.did_i_win_yet()
            except:
                print("Not a valid number, please enter a valid number")
                continue

    @classmethod
    def did_i_win_yet(cls):
        won_full_house_yet = False
        if not won_full_house_yet:
            if len(cls.my_ticket - cls.input_stream_from_host) == 0:
                print("***************************************************")
                print("******congratulations on winning full house********")
                print("***************************************************")
                won_full_house_yet = True
            if len(cls.my_ticket - cls.input_stream_from_host) == 0:
                print(colored("*********You just have one left for winning FULL HOUSE ********", "blue"))

        for k, v in cls.patterns_dict_flags.items():
            if not v:
                if len(cls.patterns_dict[k] - cls.input_stream_from_host) == 0:
                    print("")
                    print("*****************************************************")
                    print("Congratulations on winning the Pattern {}".format(k))
                    print("*****************************************************")
                    cls.patterns_dict_flags[k] = True
                if len(cls.patterns_dict[k] - cls.input_stream_from_host) == 1:
                    print("")
                    print(colored("******Just 1 left for winning the Pattern {} ******".format(k), "blue"))
        return


class FileStorage:
    stored_my_ticket = set()
    stored_sorted_ticket = list()
    stored_patterns_dict = dict()

    @classmethod
    def get_from_file(cls, file_path):
        with open(file_path, "r") as rfile:
            lines = rfile.readlines()
            for line in lines:
                obj = ast.literal_eval(line)
                if isinstance(obj, set):
                    cls.stored_my_ticket = obj
                elif isinstance(obj, list):
                    cls.stored_sorted_ticket = obj
                elif isinstance(obj, dict):
                    cls.stored_patterns_dict = obj


def main():
    checker = Checker()
    file_stored = FileStorage()
    continue_with_existing_ticket = False

    if path.exists("my_ticket2.txt"):
        print("There seems to be a ticket already generated :) ")
        file_stored.get_from_file("my_ticket2.txt")
        checker.print_status(file_stored.stored_sorted_ticket, file_stored.stored_patterns_dict)
        check_for_valid_ticket = input("is this your ticket? type yes to confirm and no to generate a new ticket: ")
        if check_for_valid_ticket == "yes":
            system("clear")
            continue_with_existing_ticket = True

    if continue_with_existing_ticket:
        checker.pass_the_variables_from_file(
            file_stored.stored_my_ticket,
            file_stored.stored_sorted_ticket,
            file_stored.stored_patterns_dict)
    else:
        system("clear")
        print("Lets generate a new ticket for you")
        checker.get_input_ticket_numbers()
        checker.get_input_winning_patterns()
        checker.generate_ticket_txt()
    checker.print_board()
    print(colored("\n-------------Ticket Updates will be shown here ------------------", "green"))
    checker.print_status()
    print(colored("\nStarting the game now....", "yellow"))
    checker.verify_input()


if __name__ == '__main__':
    main()
