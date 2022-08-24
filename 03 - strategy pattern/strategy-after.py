import random
import string
from abc import ABC, abstractmethod


def generate_id(length: int = 8) -> str:
    # helper function for generating an id
    return "".join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    def __init__(self, customer: str, issue: str) -> None:
        self.id: str = generate_id()
        self.customer: str = customer
        self.issue: str = issue


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(
            self, to_process_list: list[SupportTicket]
    ) -> list[SupportTicket]:
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(
            self, to_process_list: list[SupportTicket]
    ) -> list[SupportTicket]:
        return to_process_list.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(
            self, to_process_list: list[SupportTicket]
    ) -> list[SupportTicket]:
        return list(reversed(to_process_list.copy()))


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(
            self, to_process_list: list[SupportTicket]
    ) -> list[SupportTicket]:
        return sorted(to_process_list.copy(), key=lambda x: random.random())


class BlackHoleStrategy(TicketOrderingStrategy):
    def create_ordering(
            self, to_process_list: list[SupportTicket]
    ) -> list[SupportTicket]:
        return []


class CustomerSupport:
    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.tickets: list[SupportTicket] = []
        self.processing_strategy: TicketOrderingStrategy = processing_strategy

    def create_ticket(self, customer: str, issue: str) -> None:
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self) -> None:
        # create the ordered list
        ticket_list: list[SupportTicket] = self.processing_strategy.create_ordering(
            self.tickets
        )

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    @staticmethod
    def process_ticket(ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport(RandomOrderingStrategy())

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()
