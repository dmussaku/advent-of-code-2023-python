from dataclasses import dataclass


@dataclass
class Card:
    _id: int
    winning_numbers: list[int]
    numbers: list[int]
    num_of_copies: int = 1

    def __repr__(self):
        return f"Card({self._id}, {self.winning_numbers}, {self.numbers})"

    def __str__(self):
        return f"{self._id}, {self.winning_numbers}, {self.numbers}"

    @property
    def matched_numbers(self) -> set[int]:
        return set(self.numbers).intersection(set(self.winning_numbers))

    @property
    def points(self) -> int:
        matched_numbers = self.matched_numbers
        if len(matched_numbers) == 0:
            return 0
        elif len(matched_numbers) == 1:
            return 1 * self.num_of_copies
        elif len(matched_numbers) > 1:
            return 1 * (2 ** (len(matched_numbers) - 1)) * self.num_of_copies


def build_cards(input_lines):
    cards = []
    for line in input_lines:
        _id, rest = line.split(": ")
        winning_numbers, numbers = rest.split(" | ")
        card = Card(
            int(_id.split(" ")[-1]),
            [
                int(number)
                for number in filter(lambda x: x != "", winning_numbers.split(" "))
            ],
            [int(number) for number in filter(lambda x: x != "", numbers.split(" "))],
        )
        cards.append(card)

    return cards


def run_part_1(input_lines):
    cards = build_cards(input_lines)
    return sum([card.points for card in cards])


def run_part_2(input_lines) -> int:
    cards = build_cards(input_lines)
    # print([(card._id, card.matched_numbers) for card in cards])
    for i, card in enumerate(cards):
        num_of_winning_numbers = len(card.matched_numbers)
        # print(card._id, num_of_winning_numbers)
        if i + 1 == len(cards):
            continue

        positions = (
            list(range(i + 1, min(i + num_of_winning_numbers, len(cards)) + 1))
            * card.num_of_copies
        )
        # print(i, card._id, positions)
        for position in positions:
            cards[position].num_of_copies += 1
    return sum(card.num_of_copies for card in cards)
