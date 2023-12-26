from typing import List, Optional
from dataclasses import dataclass
from enum import Enum

class PokerCard(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5 
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

POKER_CARD_VALUES = {
    "2": PokerCard.TWO,
    "3": PokerCard.THREE,
    "4": PokerCard.FOUR,
    "5": PokerCard.FIVE,
    "6": PokerCard.SIX,
    "7": PokerCard.SEVEN,
    "8": PokerCard.EIGHT,
    "9": PokerCard.NINE,
    "T": PokerCard.TEN,
    "J": PokerCard.JACK,
    "Q": PokerCard.QUEEN,
    "K": PokerCard.KING,
    "A": PokerCard.ACE,
}

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
    cards: List[PokerCard]
    bid: int
    combination: Optional[PokerCombinations] = None

    def apply_combination(self):
        """
        Gives a combination to a hand from PokerCombinations
        """
        card_count_dict = {}
        for card in self.cards:
            if card in card_count_dict:
                card_count_dict[card] += 1
            else:
                card_count_dict[card] = 1
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
            if self.cards[i].value > other.cards[i].value:
                return self
            elif self.cards[i].value < other.cards[i].value:
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


def parse_file(file_path: str) -> List[PokerHand]:
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    hands = []
    for line in lines:
        cards_str, bid_str = line.split(" ")
        hand = PokerHand(
            cards=[POKER_CARD_VALUES[card] for card in cards_str],
            bid=int(bid_str),
        )
        hand.apply_combination()
        hands.append(hand)

    return hands


def run_part_1(file_path):
    hands: List[PokerHand] = parse_file(file_path)
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
    

def run_part_2(file_path):
    pass


