import random, sys
random.seed()

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1

for i in range(n):
    cup1 = random.choice(['Yin', 'Yang'])
    cup2 = random.choice(['Yin', 'Yang'])
    if cup1 != cup2:
        result = 'HOLY CUP (Yes/Confirmed)'
    elif cup1 == 'Yang':
        result = 'LAUGHING CUP (Reserved)'
    else:
        result = 'YIN CUP (No/Deviation)'
    prefix = f"#{i+1}: " if n > 1 else ""
    print(f"{prefix}{cup1}/{cup2} -- {result}")
