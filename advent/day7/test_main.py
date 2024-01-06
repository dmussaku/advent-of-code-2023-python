import pytest

from .main import (
    run_part_1,
    run_part_2,
    parse_file,
    PokerHand,
    PokerCardRuleStandart,
    PokerCardRuleJoker,
    PokerCombinations,
    POKER_CARD_VALUES_STANDARD,
    POKER_CARD_VALUES_JOKER,
)


class PokerHandTestGroup:
    @pytest.mark.parametrize(
        "cards,expected_combination",
        (
            (
                [
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.THREE,
                    PokerCardRuleStandart.FOUR,
                    PokerCardRuleStandart.FIVE,
                    PokerCardRuleStandart.SIX,
                ],
                PokerCombinations.HIGH_CARD,
            ),
            (
                [
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.FOUR,
                    PokerCardRuleStandart.FIVE,
                    PokerCardRuleStandart.SIX,
                ],
                PokerCombinations.ONE_PAIR,
            ),
            (
                [
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.FOUR,
                    PokerCardRuleStandart.FOUR,
                    PokerCardRuleStandart.SIX,
                ],
                PokerCombinations.TWO_PAIR,
            ),
            (
                [
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.FIVE,
                    PokerCardRuleStandart.SIX,
                ],
                PokerCombinations.THREE_OF_A_KIND,
            ),
            (
                [
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.FIVE,
                    PokerCardRuleStandart.FIVE,
                ],
                PokerCombinations.FULL_HOUSE,
            ),
            (
                [
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.SIX,
                ],
                PokerCombinations.FOUR_OF_A_KIND,
            ),
            (
                [
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.TWO,
                ],
                PokerCombinations.FIVE_OF_A_KIND,
            ),
        ),
    )
    def test_apply_combination_standart(self, cards, expected_combination):
        hand = PokerHand(cards=cards, bid=0)
        hand.apply_combination(rule=POKER_CARD_VALUES_STANDARD)
        assert hand.combination == expected_combination

    @pytest.mark.parametrize(
        "cards,expected_combination",
        (
            (
                [
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.THREE,
                    PokerCardRuleJoker.FOUR,
                    PokerCardRuleJoker.FIVE,
                    PokerCardRuleJoker.JACK,
                ],
                PokerCombinations.HIGH_CARD,
            ),
            (
                [
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.JACK,
                    PokerCardRuleJoker.FIVE,
                    PokerCardRuleJoker.SIX,
                ],
                PokerCombinations.THREE_OF_A_KIND,
            ),
            (
                [
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.FOUR,
                    PokerCardRuleJoker.FOUR,
                    PokerCardRuleJoker.JACK,
                ],
                PokerCombinations.FULL_HOUSE,
            ),
            (
                [
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.FIVE,
                    PokerCardRuleJoker.FIVE,
                ],
                PokerCombinations.FULL_HOUSE,
            ),
            (
                [
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.JACK,
                    PokerCardRuleJoker.SIX,
                ],
                PokerCombinations.FOUR_OF_A_KIND,
            ),
            (
                [
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.JACK,
                    PokerCardRuleJoker.JACK,
                ],
                PokerCombinations.FIVE_OF_A_KIND,
            ),
            (
                [
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.TWO,
                    PokerCardRuleJoker.JACK,
                    PokerCardRuleJoker.JACK,
                    PokerCardRuleJoker.JACK,
                ],
                PokerCombinations.FIVE_OF_A_KIND,
            ),
        ),
    )
    def test_apply_combination_joker(self, cards, expected_combination):
        hand = PokerHand(cards=cards, bid=0)
        hand.apply_combination(rule=POKER_CARD_VALUES_JOKER)
        assert hand.combination == expected_combination

    @pytest.mark.parametrize(
        "other_hand",
        (
            PokerHand(
                cards=[
                    PokerCardRuleStandart.ACE,
                    PokerCardRuleStandart.THREE,
                    PokerCardRuleStandart.FOUR,
                    PokerCardRuleStandart.FIVE,
                    PokerCardRuleStandart.SIX,
                ],
                bid=0,
            ),
            PokerHand(
                cards=[
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.KING,
                    PokerCardRuleStandart.FOUR,
                    PokerCardRuleStandart.FIVE,
                    PokerCardRuleStandart.SIX,
                ],
                bid=0,
            ),
            PokerHand(
                cards=[
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.THREE,
                    PokerCardRuleStandart.QUEEN,
                    PokerCardRuleStandart.FIVE,
                    PokerCardRuleStandart.SIX,
                ],
                bid=0,
            ),
            PokerHand(
                cards=[
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.THREE,
                    PokerCardRuleStandart.FOUR,
                    PokerCardRuleStandart.JACK,
                    PokerCardRuleStandart.SIX,
                ],
                bid=0,
            ),
            PokerHand(
                cards=[
                    PokerCardRuleStandart.TWO,
                    PokerCardRuleStandart.THREE,
                    PokerCardRuleStandart.FOUR,
                    PokerCardRuleStandart.FIVE,
                    PokerCardRuleStandart.TEN,
                ],
                bid=0,
            ),
        ),
    )
    def test_compare_high_card(self, other_hand):
        hand = PokerHand(
            cards=[
                PokerCardRuleStandart.TWO,
                PokerCardRuleStandart.THREE,
                PokerCardRuleStandart.FOUR,
                PokerCardRuleStandart.FIVE,
                PokerCardRuleStandart.SIX,
            ],
            bid=0,
        )
        assert hand.compare_high_card(other_hand) == other_hand

    @pytest.mark.parametrize(
        "cards,expected_result",
        (
            (
                PokerHand(
                    cards=[
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.THREE,
                        PokerCardRuleStandart.FOUR,
                        PokerCardRuleStandart.FIVE,
                        PokerCardRuleStandart.SIX,
                    ],
                    bid=0,
                ),
                False,
            ),
            (
                PokerHand(
                    cards=[
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.FOUR,
                        PokerCardRuleStandart.FIVE,
                        PokerCardRuleStandart.SIX,
                    ],
                    bid=0,
                ),
                False,
            ),
            (
                PokerHand(
                    cards=[
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.FOUR,
                        PokerCardRuleStandart.FOUR,
                        PokerCardRuleStandart.SIX,
                    ],
                    bid=0,
                ),
                False,
            ),
            (
                PokerHand(
                    cards=[
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.FIVE,
                        PokerCardRuleStandart.SIX,
                    ],
                    bid=0,
                ),
                False,
            ),
            (
                PokerHand(
                    cards=[
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.SIX,
                    ],
                    bid=0,
                ),
                True,
            ),
            (
                PokerHand(
                    cards=[
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.TWO,
                        PokerCardRuleStandart.TWO,
                    ],
                    bid=0,
                ),
                True,
            ),
        ),
    )
    def test_compare_hands(self, other_hand, expected_result):
        hand = PokerHand(
            cards=[
                PokerCardRuleStandart.TWO,
                PokerCardRuleStandart.TWO,
                PokerCardRuleStandart.TWO,
                PokerCardRuleStandart.FIVE,
                PokerCardRuleStandart.FIVE,
            ],
            bid=0,
        )
        assert hand > other_hand == expected_result


def test_parse_file():
    hands = parse_file("day7/input/test_file.txt", POKER_CARD_VALUES_STANDARD)
    assert len(hands) == 5
    assert hands[0].cards == [
        PokerCardRuleStandart.THREE,
        PokerCardRuleStandart.TWO,
        PokerCardRuleStandart.TEN,
        PokerCardRuleStandart.THREE,
        PokerCardRuleStandart.KING,
    ]
    assert hands[0].bid == 765


def test_run_part_1():
    assert run_part_1("day7/input/test_file.txt") == 6440


def test_run_part_2():
    assert run_part_2("day7/input/test_file.txt") == 5905
