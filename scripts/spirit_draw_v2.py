import random
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
random.seed()

# === TAROT DRAW (92-card pool: 78 standard + 14 miracle) ===

# Standard 78 cards
major = ["Fool", "Magician", "High Priestess", "Empress", "Emperor", "Hierophant", "Lovers", "Chariot",
         "Strength", "Hermit", "Wheel of Fortune", "Justice", "Hanged Man", "Death", "Temperance", "Devil",
         "Tower", "Star", "Moon", "Sun", "Judgement", "World"]
suits = ["Wands", "Cups", "Swords", "Pentacles"]
numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Page", "Knight", "Queen", "King"]

standard_deck = major.copy()
for suit in suits:
    for num in numbers:
        standard_deck.append(f"{num} of {suit}")

# Miracle suit (14 cards)
miracle_numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Page", "Knight", "King", "Queen"]
miracle_deck = [f"{num} of Miracles" for num in miracle_numbers]

# Full 92-card pool
full_deck = standard_deck + miracle_deck

positions = [
    "我的状态（他视角下的我）",
    "他的状态（他在这件事上的能量状态）",
    "当前语境（我们之间正在发生什么）",
    "他的态度（他对这件事的态度）",
    "态度的原因（为什么）",
    "他想说的",
]

# Draw 6 cards from 92-card pool (no replacement)
drawn_indices = random.sample(range(len(full_deck)), len(positions))

print("=== TAROT (6-Position Spread) ===")

# Track which positions got miracle cards
miracle_positions = []
drawn_cards_info = []

for i, idx in enumerate(drawn_indices):
    card = full_deck[idx]
    orientation = random.choice(["Upright", "Reversed"])
    is_miracle = card.endswith("of Miracles")
    drawn_cards_info.append((i, card, orientation, is_miracle))

    tag = " [MIRACLE]" if is_miracle else ""
    print(f"Pos {i+1} [{positions[i]}]: {card} ({orientation}){tag}")

    if is_miracle:
        miracle_positions.append(i)

# === SUPPLEMENT DRAW (for miracle card positions) ===
if miracle_positions:
    print(f"\n=== SUPPLEMENT DRAW ({len(miracle_positions)} miracle card(s) detected) ===")

    # Build remaining standard pool: 78 standard cards minus any standard cards already drawn
    used_standard_indices = [idx for idx in drawn_indices if idx < len(standard_deck)]
    remaining_standard = [i for i in range(len(standard_deck)) if i not in used_standard_indices]

    # Draw supplement cards from remaining standard pool
    supplement_indices = random.sample(remaining_standard, len(miracle_positions))

    for j, pos_idx in enumerate(miracle_positions):
        sup_card = standard_deck[supplement_indices[j]]
        sup_orientation = random.choice(["Upright", "Reversed"])
        orig_card = drawn_cards_info[pos_idx][1]
        orig_orient = drawn_cards_info[pos_idx][2]
        print(f"Pos {pos_idx+1} [{positions[pos_idx]}]: {orig_card} ({orig_orient}) -> Supplement: {sup_card} ({sup_orientation})")

# === WORD CARDS ===
# REMOVED: Word cards moved to separate per-entity scripts (wordcard_astarion.py, wordcard_hermes.py, etc.)
# Reason: Different entities have different card pools

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

# 飞星计算：根据星座落宫推算上升，再计算行星主宰星座落在哪些宫位
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

# === JIAOBEI ===
# REMOVED: Jiaobei module has been moved to separate jiaobei.py script
# Reason: To enforce "interpret first, verify later" workflow
# Agent must call jiaobei.py separately AFTER completing interpretation
# See: 2026-02-06 audit report - preventing procedural premature issues
