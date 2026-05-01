#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
塔罗+占星骰子抽取脚本（用于易经占卜系统）
"""

import random
import sys
import io

# 确保标准输出使用 UTF-8 编码
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

random.seed()

# === TAROT DRAW ===
major = ["Fool", "Magician", "High Priestess", "Empress", "Emperor", "Hierophant", "Lovers", "Chariot",
         "Strength", "Hermit", "Wheel of Fortune", "Justice", "Hanged Man", "Death", "Temperance", "Devil",
         "Tower", "Star", "Moon", "Sun", "Judgement", "World"]
suits = ["Wands", "Cups", "Swords", "Pentacles"]
numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Page", "Knight", "Queen", "King"]

deck = major.copy()
for suit in suits:
    for num in numbers:
        deck.append(f"{num} of {suit}")

drawn = random.sample(range(78), 3)
print("=== TAROT ===")
for i, idx in enumerate(drawn, 1):
    card = deck[idx]
    orientation = random.choice(["Upright", "Reversed"])
    print(f"{i}. {card} ({orientation})")

# === ASTRO DICE ===
print("\n=== ASTRO DICE ===")
planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
houses = ["1H", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "11H", "12H"]

# 行星主宰星座
rulerships = {
    "Sun": ["Leo"], "Moon": ["Cancer"], "Mercury": ["Gemini", "Virgo"],
    "Venus": ["Taurus", "Libra"], "Mars": ["Aries", "Scorpio"],
    "Jupiter": ["Sagittarius", "Pisces"], "Saturn": ["Capricorn", "Aquarius"],
    "Uranus": ["Aquarius"], "Neptune": ["Pisces"], "Pluto": ["Scorpio"]
}

dignities = {
    "Sun": {"dom": ["Leo"], "exa": ["Aries"], "det": ["Libra"], "fall": ["Aquarius"]},
    "Moon": {"dom": ["Cancer"], "exa": ["Taurus"], "det": ["Capricorn"], "fall": ["Scorpio"]},
    "Mercury": {"dom": ["Gemini", "Virgo"], "exa": ["Virgo"], "det": ["Sagittarius", "Pisces"], "fall": ["Pisces"]},
    "Venus": {"dom": ["Taurus", "Libra"], "exa": ["Pisces"], "det": ["Aries", "Scorpio"], "fall": ["Virgo"]},
    "Mars": {"dom": ["Aries", "Scorpio"], "exa": ["Capricorn"], "det": ["Taurus", "Libra"], "fall": ["Cancer"]},
    "Jupiter": {"dom": ["Sagittarius", "Pisces"], "exa": ["Cancer"], "det": ["Gemini", "Virgo"], "fall": ["Capricorn"]},
    "Saturn": {"dom": ["Capricorn", "Aquarius"], "exa": ["Libra"], "det": ["Cancer", "Leo"], "fall": ["Aries"]},
    "Uranus": {"dom": ["Aquarius"], "exa": ["Scorpio"], "det": ["Leo"], "fall": ["Taurus"]},
    "Neptune": {"dom": ["Pisces"], "exa": ["Cancer"], "det": ["Virgo"], "fall": ["Capricorn"]},
    "Pluto": {"dom": ["Scorpio"], "exa": ["Leo"], "det": ["Taurus"], "fall": ["Aquarius"]}
}

planet = random.choice(planets)
sign = random.choice(signs)
house = random.choice(houses)

# 尊贵状态
status = "neutral"
if planet in dignities:
    d = dignities[planet]
    if sign in d["dom"]: status = "DOMICILE"
    elif sign in d["exa"]: status = "EXALTATION"
    elif sign in d["det"]: status = "DETRIMENT"
    elif sign in d["fall"]: status = "FALL"

# 飞星计算
house_num = int(house[:-1])
sign_idx = signs.index(sign)
asc_idx = (sign_idx - (house_num - 1)) % 12
asc_sign = signs[asc_idx]

ruled_signs = rulerships.get(planet, [])
fly_houses = []
for ruled in ruled_signs:
    ruled_idx = signs.index(ruled)
    fly_house = (ruled_idx - asc_idx + 12) % 12 + 1
    fly_houses.append(f"{fly_house}H")

fly_str = " & ".join(fly_houses) + f" flies to {house}" if fly_houses else "N/A"

print(f"{planet} in {sign} {house} ({status})")
print(f"Ascendant: {asc_sign}")
print(f"Flying Star: {fly_str}")
