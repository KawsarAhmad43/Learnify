# Task: Card Deck

## Objective
Enums.

## Setup
*   Standard 52-card deck.

## Task
1.  Create an Enum `Suit` (HEARTS, DIAMONDS, CLUBS, SPADES).
2.  Create an Enum `Rank` (ACE, TWO... KING). Assign values (e.g., JACK=11).
3.  Create a dataclass `Card` with `rank: Rank` and `suit: Suit`.
4.  Adding `order=True` to the dataclass decorator allows you to compare cards (`card1 > card2`).
5.  **Task**: Create a full deck (loop over Enums), shuffle it (using `random.shuffle`), and deal 5 cards.

## Question
What is `__post_init__`?
*   Answer: A method in dataclasses that runs *after* `__init__`. Useful for validation or calculating derived fields (e.g., `self.fullname = f"{first} {last}"`).
