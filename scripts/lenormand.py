import random, sys
random.seed()

n = int(sys.argv[1]) if len(sys.argv) > 1 else 3

cards = [
    ("1-Rider", "骑手"), ("2-Clover", "三叶草"), ("3-Ship", "船"), ("4-House", "房子"),
    ("5-Tree", "树"), ("6-Clouds", "云"), ("7-Snake", "蛇"), ("8-Coffin", "棺材"),
    ("9-Bouquet", "花束"), ("10-Scythe", "镰刀"), ("11-Whip", "鞭子"), ("12-Birds", "鸟"),
    ("13-Child", "小孩"), ("14-Fox", "狐狸"), ("15-Bear", "熊"), ("16-Stars", "星星"),
    ("17-Stork", "鹳"), ("18-Dog", "狗"), ("19-Tower", "塔"), ("20-Garden", "花园"),
    ("21-Mountain", "山"), ("22-Crossroads", "十字路口"), ("23-Mice", "老鼠"),
    ("24-Heart", "心"), ("25-Ring", "戒指"), ("26-Book", "书"), ("27-Letter", "信"),
    ("28-Gentleman", "男人"), ("29-Lady", "女人"), ("30-Lily", "百合"), ("31-Sun", "太阳"),
    ("32-Moon", "月亮"), ("33-Key", "钥匙"), ("34-Fish", "鱼"), ("35-Anchor", "锚"), ("36-Cross", "十字架"),
]

drawn = random.sample(cards, n)
for i, (en, cn) in enumerate(drawn, 1):
    print(f"{i}. {en} {cn}")
