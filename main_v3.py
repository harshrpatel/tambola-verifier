from util.ticket_stored import TicketStored
from util.board_stored import BoardStored
from util.ticket_status import TicketStatus
from util.board_status import BoardStatus
from os import system
from os import path
from termcolor import colored


def main():
    ticket_path = "asset/cricket.txt"
    board_path = "asset/cricket_board.txt"

    continue_with_existing_ticket = False
    continue_with_existing_board = False

    ticket_from_file = TicketStored()
    board_from_file = BoardStored()

    ticket_status = TicketStatus()
    board_status = BoardStatus()

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
        pass

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


if __name__ == '__main__':
    main()
