from typing import List, Optional, Union, Dict
from dataclasses import dataclass
from enum import Enum


class PokerCardBase:
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = None
    QUEEN = 12
    KING = 13
    ACE = 14


class PokerCardRuleStandart(PokerCardBase):
    JACK = 11


class PokerCardRuleJoker(PokerCardBase):
    JACK = 1


POKER_CARD_VALUES_BASE = {
    "2": PokerCardBase.TWO,
    "3": PokerCardBase.THREE,
    "4": PokerCardBase.FOUR,
    "5": PokerCardBase.FIVE,
    "6": PokerCardBase.SIX,
    "7": PokerCardBase.SEVEN,
    "8": PokerCardBase.EIGHT,
    "9": PokerCardBase.NINE,
    "T": PokerCardBase.TEN,
    "Q": PokerCardBase.QUEEN,
    "K": PokerCardBase.KING,
    "A": PokerCardBase.ACE,
}

POKER_CARD_VALUES_STANDARD = {"J": PokerCardRuleStandart.JACK, **POKER_CARD_VALUES_BASE}

POKER_CARD_VALUES_JOKER = {"J": PokerCardRuleJoker.JACK, **POKER_CARD_VALUES_BASE}


class PokerCombinations(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


@dataclass
class PokerHand:
    cards: List[Union[PokerCardRuleStandart, PokerCardRuleJoker]]
    bid: int
    combination: Optional[PokerCombinations] = None

    def apply_combination(self, rule: Dict = POKER_CARD_VALUES_STANDARD):
        """
        Gives a combination to a hand from PokerCombinations
        """
        card_count_dict = {}
        for card in self.cards:
            if card in card_count_dict:
                card_count_dict[card] += 1
            else:
                card_count_dict[card] = 1

        if (
            rule == POKER_CARD_VALUES_JOKER
            and PokerCardRuleJoker.JACK in card_count_dict
        ):
            number_of_jokers = card_count_dict.pop(PokerCardRuleJoker.JACK)
            highest_card_count = sorted(
                {card: number for card, number in card_count_dict.items() if number > 1}
            )
            if highest_card_count:
                highest_card = highest_card_count[-1]
                card_count_dict[highest_card] += number_of_jokers

        if 5 in card_count_dict.values():
            self.combination = PokerCombinations.FIVE_OF_A_KIND
        elif 4 in card_count_dict.values():
            self.combination = PokerCombinations.FOUR_OF_A_KIND
        elif 3 in card_count_dict.values():
            if 2 in card_count_dict.values():
                self.combination = PokerCombinations.FULL_HOUSE
            else:
                self.combination = PokerCombinations.THREE_OF_A_KIND
        elif 2 in card_count_dict.values():
            if len(card_count_dict.values()) == 3:
                self.combination = PokerCombinations.TWO_PAIR
            else:
                self.combination = PokerCombinations.ONE_PAIR
        else:
            self.combination = PokerCombinations.HIGH_CARD

    def compare_high_card(self, other):
        for i in range(5):
            if self.cards[i] > other.cards[i]:
                return self
            elif self.cards[i] < other.cards[i]:
                return other
            else:
                continue

    def compare_combinations(self, other):
        if self.combination.value > other.combination.value:
            return self
        elif self.combination.value < other.combination.value:
            return other
        else:
            return self.compare_high_card(other)

    def __gt__(self, other):
        if self.compare_combinations(other) == self:
            return True

    def __lt__(self, other):
        if self.compare_combinations(other) == other:
            return True


def parse_file(file_path: str, rule: Dict) -> List[PokerHand]:
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    hands = []
    for line in lines:
        cards_str, bid_str = line.split(" ")
        hand = PokerHand(
            cards=[rule[card] for card in cards_str],
            bid=int(bid_str),
        )
        hand.apply_combination(rule)
        hands.append(hand)

    return hands


def run_common_part(file_path, rule: Dict):
    hands: List[PokerHand] = parse_file(file_path, rule=rule)
    sorted_hands = []
    for _ in range(len(hands)):
        min_hand = hands[0]
        for hand in hands:
            if hand < min_hand:
                min_hand = hand
        hands.pop(hands.index(min_hand))
        sorted_hands.append(min_hand)

    result = 0
    for i, hand in enumerate(sorted_hands, 1):
        result += hand.bid * (i)

    return result


def run_part_1(file_path):
    return run_common_part(file_path, rule=POKER_CARD_VALUES_STANDARD)


def run_part_2(file_path):
    return run_common_part(file_path, rule=POKER_CARD_VALUES_JOKER)
