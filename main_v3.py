import os

from util.ticket_stored import TicketStored
from util.board_stored import BoardStored
from util.ticket_status import TicketStatus
from util.board_status import BoardStatus
from util.register_input import RegisterInput
import util.excel_data as excelAccess
from os import system
from os import path
from termcolor import colored


def main():
    ticket_path = "asset/parks_ticket.txt"
    board_path = "asset/parks_board.txt"
    excel_path = "asset/parks.xlsx"


    continue_with_existing_ticket = False
    continue_with_existing_board = False
    game_over_flag = False

    ticket_from_file = TicketStored()
    board_from_file = BoardStored()

    ticket_status = TicketStatus()
    board_status = BoardStatus()
    register_input = RegisterInput()

    if path.exists(ticket_path):
        print(colored("There seems to be a ticket already generated", "yellow"))
        ticket_from_file.get_from_file(ticket_path)
        ticket_status.initialize(
            None,
            ticket_from_file.my_stored_ticket,
            ticket_from_file.my_stored_pattens)
        ticket_status.print_ticket_status()
        check_for_valid_ticket = input("Is this your ticket? "
                                       "type yes to confirm and no to generate a new ticket: ")
        if check_for_valid_ticket == "yes":
            print(colored("Cool, we will be using this ticket", "yellow"))
            continue_with_existing_ticket = True

    if continue_with_existing_ticket:
        pass
    else:
        system("clear")
        ask_excel_path = input("Should we be using util/movie.xlsx, type yes to confirm or file path for others: ")
        if ask_excel_path != "yes":
            excel_path = ask_excel_path
        excel_data = excelAccess.get_data_from_excel(excel_path)
        ticket_status.initialize(None,
                                 excel_data["ticket"],
                                 excel_data["patterns"])
        ticket_status.print_ticket_status()
        check_for_valid_ticket = input("Is this your ticket? "
                                       "type yes to confirm and no to generate a new ticket: ")
        if check_for_valid_ticket == "yes":
            print(colored("Cool, we will be using this ticket", "yellow"))

    if path.exists(board_path):
        print(colored("There seems to be a ready board", "yellow"))
        board_from_file.get_from_file(board_path)
        board_status.initialize(None, board_from_file.my_stored_board)
        board_status.print_board_status()
        check_for_valid_board = input("Is this your board? "
                                      "type yes to confirm and no to generate a new board: ")
        if check_for_valid_board == "yes":
            print(colored("Cool, we will be using this board", "yellow"))
            continue_with_existing_board = True

    if continue_with_existing_board:
        pass
    else:
        pass

    system("clear")
    board_status.print_board_status()
    print(colored("\n--------------- Ticket Updates will be shown here --------------------", "green"))
    print(colored("------------ Sit Back and Relax, We have eyes on it ------------------", "green"))
    print(colored("------------------------ (-(-_(-_-)_-)-) -----------------------------", "yellow"))
    ticket_status.print_ticket_status()
    print(colored("\nStarting the game now....", "yellow"))
    register_input.initialize(ticket_status.registered_numbers,
                              board_status.current_board,
                              ticket_status.pattern_dict_completion_flags,
                              ticket_status.ticket)

    while not game_over_flag:
        if register_input.game_over_flag:
            game_over_flag = True
            continue
        if not register_input.command_from_input_flag:
            system("clear")
            board_status.print_board_status(register_input.registered_numbers)
            print(register_input.text_to_display_from_input)
            ticket_status.print_ticket_status(register_input.registered_numbers)
        register_input.get_input_and_commands()


if __name__ == '__main__':
    main()
