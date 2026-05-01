#!/usr/bin/env python3
"""NPC Word Cards — neutral narrative tone for game NPCs."""

import random

CARDS = [
    # 状态/处境
    "Waiting for something that may not come.",
    "Carrying more than it looks.",
    "Been here longer than intended.",
    "Not the first to ask.",
    "Something was taken.",
    "Something was left behind.",
    "Knows more than they say.",
    "Says more than they know.",
    "Stuck between two things.",
    "Almost ready to leave.",
    "Just arrived.",
    "Has been watching.",
    "Lost the thread.",
    "Found the wrong thing.",
    "Owes someone.",
    "Is owed.",
    "Made a trade once.",
    "Regrets one thing.",
    "Regrets nothing.",
    "Forgot the reason.",

    # 对玩家的态度/反应
    "Recognizes something.",
    "Doesn't trust easily.",
    "Trusts too easily.",
    "Wants to help but can't.",
    "Could help but won't.",
    "Needs something first.",
    "Has already decided.",
    "Still deciding.",
    "Pretending not to notice.",
    "Noticed everything.",
    "Will remember this.",
    "Has forgotten worse.",
    "Wants to be asked.",
    "Doesn't want to be asked.",
    "Will lie once.",
    "Won't lie.",
    "Tells half.",

    # 线索/环境
    "The door was open before.",
    "Someone else came through here.",
    "The light changed recently.",
    "Something moved in the night.",
    "The water level is wrong.",
    "It used to make a sound.",
    "There's a mark on the floor.",
    "The smell is wrong.",
    "It was heavier before.",
    "The name has changed.",
]

def draw(n=3):
    return random.sample(CARDS, min(n, len(CARDS)))

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    results = draw(n)
    print("=== NPC WORD CARDS ===")
    for i, card in enumerate(results, 1):
        print(f"{i}. {card}")
