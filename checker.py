import ast
from os import path
import copy


class Checker:
    my_ticket = set()
    sorted_ticket = list()
    patterns_dict = dict()

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
                        cls.patterns_dict[pattern_name] = list(pattern_set)
            print(cls.patterns_dict)

    @classmethod
    def generate_ticket_txt(cls):
        with open("my_ticket.txt", "w") as wfile:
            wfile.write(str(cls.my_ticket)+"\n")
            wfile.write(str(cls.sorted_ticket)+"\n")
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

    @classmethod
    def print_status(cls, ticket=None, patterns=None):
        if ticket is None:
            ticket = cls.sorted_ticket
        if patterns is None:
            patterns = cls.patterns_dict

        print("My Ticket: ")
        for i, num in enumerate(ticket):
            if i in [4, 9, 13, 18, 23]:
                print(str(num).zfill(2))
            elif i == 12:
                print("X " + " " * 8 + str(num).zfill(2), end=" " * 8)
            else:
                print(str(num).zfill(2), end=" " * 8)

        print("\nPatterns and your numbers")
        for k, v in patterns.items():
            print(k, end=" ")
            print(v)


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


class Verify:

    def __init__(self, sorted_ticket, my_ticket, input_num, pattern_dict=None, file_name=None):
        self.ticket = my_ticket
        self.variations = pattern_dict
        self.input_num = input_num
        if file_name:
            self.file_name = file_name
        self.remaining_ticket = sorted_ticket

    def get_remaining_ticket(self):
        if int(self.input_num) in self.remaining_ticket:
            self.remaining_ticket.remove(int(input_num))
        print(self.remaining_ticket)

    def get_scratched_ticket(self):
        new_tkt = self.ticket
        self.ticket = [strike_through(x) if x in list(set(self.ticket) - set(self.remaining_ticket)) else x for x in new_tkt]
        print(self.ticket)

    def check_variations(self):
        remaining_variation = {}
        print(self.variations)
        try:
            for i in self.variations:
                print(i)
                print(self.variations[i])
                if int(self.input_num) in self.variations[i]:
                    self.variations[i].remove(int(self.input_num))
                remaining_variation[i] = self.variations[i]
                if len(remaining_variation[i]) < 1:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Congratulations, for your ticket variation {} is successfully done!".format(i))
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(remaining_variation)

        except Exception as err:
            print(err)



def strike_through(num: int) -> str:
    result = ''
    for c in str(num):
        result = result + c + '\u0336'
    return result


def main():
    checker = Checker()
    fileStored = FileStorage()
    continue_with_existing_ticket = False

    if path.exists("my_ticket.txt"):
        print("There seems to be a ticket already generated :) ")
        fileStored.get_from_file("my_ticket.txt")
        checker.print_status(fileStored.stored_sorted_ticket, fileStored.stored_patterns_dict)
        check_for_valid_ticket = input("is this your ticket? type yes to confirm and no to generate a new ticket: ")
        if check_for_valid_ticket == "yes":
            continue_with_existing_ticket = True

    if continue_with_existing_ticket:
        checker.pass_the_variables_from_file(
            fileStored.stored_my_ticket,
            fileStored.stored_sorted_ticket,
            fileStored.stored_patterns_dict)
    else:
        print("Lets generate a new ticket for you")
        checker.get_input_ticket_numbers()
        checker.get_input_winning_patterns()
        checker.generate_ticket_txt()

    checker.print_status()


if __name__ == '__main__':
    sort_ticket = [1, 2, 3, 4, 5]
    my_ticket = [1, 2, 3, 4, 5]
    patterns = {'a': [1, 2], 'b': [3, 4], 'c': [3,1]}
    while True:
        input_num = input("Enter any number:")
        verify = Verify(sort_ticket, my_ticket, input_num, pattern_dict=patterns)
        verify.get_remaining_ticket()
        verify.get_scratched_ticket()
        verify.check_variations()
