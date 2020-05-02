from util.ticket_stored import TicketStored
from util.ticket_status import TicketStatus
from os import system
from os import path
from termcolor import colored


class Main:
    ticket_path = "asset/cricket.txt"

    def __init__(self):
        pass

    ticket_from_file = TicketStored()
    if path.exists(ticket_path):
        print(colored("There seems to be a ticket already generated"))
        ticket_from_file.get_from_file(ticket_path)
        t1 = TicketStatus()
        t1.initialize(
            None,
            ticket_from_file.my_stored_ticket,
            ticket_from_file.my_stored_pattens)
        t1.print_ticket_status()

if __name__ == '__main__':
    Main
