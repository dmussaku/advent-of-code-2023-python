import pytest

from .main import run_part_1, run_part_2, parse_file, PokerHand, PokerCard, PokerCombinations, POKER_CARD_VALUES


class PokerHandTestGroup:
    @pytest.mark.parametrize('cards,expected_combination', (
        ([PokerCard.TWO, PokerCard.THREE, PokerCard.FOUR, PokerCard.FIVE, PokerCard.SIX],PokerCombinations.HIGH_CARD),
        ([PokerCard.TWO, PokerCard.TWO, PokerCard.FOUR, PokerCard.FIVE, PokerCard.SIX],PokerCombinations.ONE_PAIR),
        ([PokerCard.TWO, PokerCard.TWO, PokerCard.FOUR, PokerCard.FOUR, PokerCard.SIX],PokerCombinations.TWO_PAIR),
        ([PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.FIVE, PokerCard.SIX],PokerCombinations.THREE_OF_A_KIND),
        ([PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.FIVE, PokerCard.FIVE],PokerCombinations.FULL_HOUSE),
        ([PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.SIX],PokerCombinations.FOUR_OF_A_KIND),
        ([PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.TWO],PokerCombinations.FIVE_OF_A_KIND),
    ))
    def test_apply_combination(self, cards, expected_combination):
        hand = PokerHand(cards=cards, bid=0)
        hand.apply_combination()
        assert hand.combination == expected_combination
    
    @pytest.mark.parametrize('other_hand', (
        PokerHand(cards=[PokerCard.ACE, PokerCard.THREE, PokerCard.FOUR, PokerCard.FIVE, PokerCard.SIX], bid=0),
        PokerHand(cards=[PokerCard.TWO, PokerCard.KING, PokerCard.FOUR, PokerCard.FIVE, PokerCard.SIX], bid=0),
        PokerHand(cards=[PokerCard.TWO, PokerCard.THREE, PokerCard.QUEEN, PokerCard.FIVE, PokerCard.SIX], bid=0),
        PokerHand(cards=[PokerCard.TWO, PokerCard.THREE, PokerCard.FOUR, PokerCard.JACK, PokerCard.SIX], bid=0),
        PokerHand(cards=[PokerCard.TWO, PokerCard.THREE, PokerCard.FOUR, PokerCard.FIVE, PokerCard.TEN], bid=0),
    ))
    def test_compare_high_card(self, other_hand):
        hand = PokerHand(cards=[PokerCard.TWO, PokerCard.THREE, PokerCard.FOUR, PokerCard.FIVE, PokerCard.SIX], bid=0)
        assert hand.compare_high_card(other_hand) == other_hand
    
    @pytest.mark.parametrize('cards,expected_result', (
        (PokerHand(cards=[PokerCard.TWO, PokerCard.THREE, PokerCard.FOUR, PokerCard.FIVE, PokerCard.SIX], bid=0), False),
        (PokerHand(cards=[PokerCard.TWO, PokerCard.TWO, PokerCard.FOUR, PokerCard.FIVE, PokerCard.SIX], bid=0), False),
        (PokerHand(cards=[PokerCard.TWO, PokerCard.TWO, PokerCard.FOUR, PokerCard.FOUR, PokerCard.SIX], bid=0), False),
        (PokerHand(cards=[PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.FIVE, PokerCard.SIX], bid=0), False),
        (PokerHand(cards=[PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.SIX], bid=0), True),
        (PokerHand(cards=[PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.TWO], bid=0), True),
    ))
    def test_compare_hands(self, other_hand, expected_result):
        hand = PokerHand(cards=[PokerCard.TWO, PokerCard.TWO, PokerCard.TWO, PokerCard.FIVE, PokerCard.FIVE], bid=0)
        assert hand > other_hand == expected_result

def test_parse_file():
    hands = parse_file('day7/input/test_file.txt')
    assert len(hands) == 5
    assert hands[0].cards == [PokerCard.THREE, PokerCard.TWO, PokerCard.TEN, PokerCard.THREE, PokerCard.KING]
    assert hands[0].bid == 765


def test_run_part_1():
    assert run_part_1('day7/input/test_file.txt') == 6440


def test_run_part_2():
    pass