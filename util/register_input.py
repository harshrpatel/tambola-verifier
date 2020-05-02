from termcolor import colored
from fuzzywuzzy import process


class RegisterInput:
    registered_numbers = list()
    current_board = list()
    pattern_dict_completion_flags = dict()
    game_over_flag = False
    command_from_input_flag = False
    text_to_display_from_input = colored("", "white")
    ticket = list()

    @classmethod
    def initialize(cls, registered_numbers=None, current_board=None, pattern_dict_completion_flags=None,
                   ticket=None):
        cls.registered_numbers = registered_numbers
        cls.current_board = current_board
        cls.pattern_dict_completion_flags = pattern_dict_completion_flags
        cls.ticket = ticket

    @classmethod
    def get_input_and_commands(cls, registered_numbers=None):
        if registered_numbers is None:
            registered_numbers = cls.registered_numbers

        valid_input_provided = False
        cls.command_from_input_flag = False

        while not valid_input_provided:
            try:
                input_during_game = input(colored("\nEnter the number from host: ", "blue"))
                f_list = process.extractBests(input_during_game, cls.current_board, limit=3, score_cutoff=80)
                f_dict = {}

                if len(f_list) > 0:
                    for i, t in enumerate(f_list):
                        f_dict[i + 1] = t[0]

                if cls.registered_numbers is None:
                    cls.registered_numbers = []

                if input_during_game == "gg":
                    print("༼ つ ◕_◕ ༽つ" + " Good Game " + "༼ つ ◕_◕ ༽つ")
                    cls.game_over_flag = True

                elif input_during_game in cls.registered_numbers:
                    cls.text_to_display_from_input = colored("\nThis value was already added and account "
                                                             "for: {}".format(input_during_game), "magenta")

                elif input_during_game in cls.pattern_dict_completion_flags:
                    cls.command_from_input_flag = True
                    cls.pattern_dict_completion_flags[input_during_game] = True
                    print(colored("Marking this pattern as done,we wont be notifying you on completion of this "
                                  "pattern, type unmark if done by mistake", "yellow"))

                elif input_during_game == "remove":
                    what_to_remove = input("What do wish to remove, need right spelling and case: ")
                    cls.registered_numbers.remove(what_to_remove)
                    cls.text_to_display_from_input = colored("\nThis is input is removed for "
                                                             "register inputs: {}".format(what_to_remove), "magenta")
                elif input_during_game == "unmark":
                    what_to_unmark = input("What do wish to unmark: ")
                    cls.pattern_dict_completion_flags[what_to_unmark] = True
                    cls.text_to_display_from_input = colored("\nThis is pattern is now unmarked"
                                                             ": {}".format(what_to_unmark), "magenta")

                elif input_during_game in cls.current_board:
                    cls.registered_numbers.append(input_during_game)
                    if input_during_game in cls.ticket:
                        cls.text_to_display_from_input = colored("\n--------- Mark the ticket, {} is on your ticket "
                                                                 "--------".format(input_during_game), "yellow")
                    else:
                        cls.text_to_display_from_input = colored("\n--------- Never Mind, {} was not on your ticket "
                                                                 "--------".format(input_during_game), "magenta")
                elif len(f_list) > 0:
                    print(colored("\nDid you any of the following?: ", "blue"))
                    for k, v in f_dict.items():
                        print("type {} for {}".format(k, v))
                    input_from_fuzzy = int(input(colored("\ntype your choice here: ", "blue")))
                    input_during_game = f_dict[input_from_fuzzy]
                    cls.registered_numbers.append(input_during_game)
                    if input_during_game in cls.ticket:
                        cls.text_to_display_from_input = colored("\n--------- Mark the ticket, {} is on your ticket "
                                                                 "--------".format(input_during_game), "yellow")
                    else:
                        cls.text_to_display_from_input = colored("\n--------- Never Mind, {} was not on your ticket "
                                                                 "--------".format(input_during_game), "magenta")
                else:
                    raise

                valid_input_provided = True
            except:
                print("Not a valid value, Please enter a valid input")
                continue
