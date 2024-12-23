# Mini-Blackjack Game

This project is a simple console-based blackjack game written in Python. It simulates a blackjack game where the player can place bets, draw cards, and compete against the dealer.

## Features

- Supports splitting pairs and doubling down.
- Includes an insurance option when the dealer shows an Ace.
- Automatically reshuffles when the deck runs out of cards.
- Simulates the dealer's play logic (dealer must draw until reaching 17 or more).

## How to Play

1. Run the script using Python.
2. Start with a wallet of 30 units.
3. Place a bet for each round.
4. Draw cards and aim to get as close as possible to 21 without exceeding it.
5. Decide whether to stay, hit, double down, or split (if applicable).
6. The game ends when your wallet reaches 0.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NathanRouille/BlackJack.git
   cd BlackJack
   ```
2. Run the script:
   ```bash
   python blackjack.py
   ```

## Rules

- Aces can count as 1 or 11 points, depending on the hand value.
- Face cards (Jack, Queen, King) are worth 10 points.
- The dealer must draw until their hand value reaches 17 or more.
- Players can:
  - `Hit`: Draw another card.
  - `Stay`: End their turn.
  - `Double Down`: Double the bet and draw one final card.
  - `Split`: Split the hand into two separate hands (if the initial cards are a pair).


## Contributions

Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests.
