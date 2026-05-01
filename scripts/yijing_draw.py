#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
易经起卦脚本
使用三个随机数（1-99）生成本卦和之卦
"""

import random
import sys
import io

# 确保标准输出使用 UTF-8 编码
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 八卦对应
TRIGRAMS = {
    1: "乾", 2: "兑", 3: "离", 4: "震",
    5: "巽", 6: "坎", 7: "艮", 8: "坤"
}

# 八卦属性
TRIGRAM_ATTRS = {
    "乾": "☰", "兑": "☱", "离": "☲", "震": "☳",
    "巽": "☴", "坎": "☵", "艮": "☶", "坤": "☷"
}

# 64卦对照表 (上卦, 下卦) -> (卦名, 卦序, 所属宫, 类型)
HEXAGRAMS = {
    ("乾", "乾"): ("乾为天", 1, "乾宫", "本宫卦"),
    ("乾", "兑"): ("天泽履", 10, "乾宫", "一世卦"),
    ("乾", "离"): ("天火同人", 13, "乾宫", "二世卦"),
    ("乾", "震"): ("天雷无妄", 25, "乾宫", "三世卦"),
    ("乾", "巽"): ("天风姤", 44, "乾宫", "四世卦"),
    ("乾", "坎"): ("天水讼", 6, "乾宫", "五世卦"),
    ("乾", "艮"): ("天山遁", 33, "乾宫", "游魂卦"),
    ("乾", "坤"): ("天地否", 12, "乾宫", "归魂卦"),

    ("兑", "乾"): ("泽天夬", 43, "兑宫", "一世卦"),
    ("兑", "兑"): ("兑为泽", 58, "兑宫", "本宫卦"),
    ("兑", "离"): ("泽火革", 49, "兑宫", "二世卦"),
    ("兑", "震"): ("泽雷随", 17, "兑宫", "三世卦"),
    ("兑", "巽"): ("泽风大过", 28, "兑宫", "四世卦"),
    ("兑", "坎"): ("泽水困", 47, "兑宫", "五世卦"),
    ("兑", "艮"): ("泽山咸", 31, "兑宫", "游魂卦"),
    ("兑", "坤"): ("泽地萃", 45, "兑宫", "归魂卦"),

    ("离", "乾"): ("火天大有", 14, "离宫", "一世卦"),
    ("离", "兑"): ("火泽睽", 38, "离宫", "二世卦"),
    ("离", "离"): ("离为火", 30, "离宫", "本宫卦"),
    ("离", "震"): ("火雷噬嗑", 21, "离宫", "三世卦"),
    ("离", "巽"): ("火风鼎", 50, "离宫", "四世卦"),
    ("离", "坎"): ("火水未济", 64, "离宫", "五世卦"),
    ("离", "艮"): ("火山旅", 56, "离宫", "游魂卦"),
    ("离", "坤"): ("火地晋", 35, "离宫", "归魂卦"),

    ("震", "乾"): ("雷天大壮", 34, "震宫", "一世卦"),
    ("震", "兑"): ("雷泽归妹", 54, "震宫", "二世卦"),
    ("震", "离"): ("雷火丰", 55, "震宫", "三世卦"),
    ("震", "震"): ("震为雷", 51, "震宫", "本宫卦"),
    ("震", "巽"): ("雷风恒", 32, "震宫", "四世卦"),
    ("震", "坎"): ("雷水解", 40, "震宫", "五世卦"),
    ("震", "艮"): ("雷山小过", 62, "震宫", "游魂卦"),
    ("震", "坤"): ("雷地豫", 16, "震宫", "归魂卦"),

    ("巽", "乾"): ("风天小畜", 9, "巽宫", "一世卦"),
    ("巽", "兑"): ("风泽中孚", 61, "巽宫", "二世卦"),
    ("巽", "离"): ("风火家人", 37, "巽宫", "三世卦"),
    ("巽", "震"): ("风雷益", 42, "巽宫", "四世卦"),
    ("巽", "巽"): ("巽为风", 57, "巽宫", "本宫卦"),
    ("巽", "坎"): ("风水涣", 59, "巽宫", "五世卦"),
    ("巽", "艮"): ("风山渐", 53, "巽宫", "游魂卦"),
    ("巽", "坤"): ("风地观", 20, "巽宫", "归魂卦"),

    ("坎", "乾"): ("水天需", 5, "坎宫", "一世卦"),
    ("坎", "兑"): ("水泽节", 60, "坎宫", "二世卦"),
    ("坎", "离"): ("水火既济", 63, "坎宫", "三世卦"),
    ("坎", "震"): ("水雷屯", 3, "坎宫", "四世卦"),
    ("坎", "巽"): ("水风井", 48, "坎宫", "五世卦"),
    ("坎", "坎"): ("坎为水", 29, "坎宫", "本宫卦"),
    ("坎", "艮"): ("水山蹇", 39, "坎宫", "游魂卦"),
    ("坎", "坤"): ("水地比", 8, "坎宫", "归魂卦"),

    ("艮", "乾"): ("山天大畜", 26, "艮宫", "一世卦"),
    ("艮", "兑"): ("山泽损", 41, "艮宫", "二世卦"),
    ("艮", "离"): ("山火贲", 22, "艮宫", "三世卦"),
    ("艮", "震"): ("山雷颐", 27, "艮宫", "四世卦"),
    ("艮", "巽"): ("山风蛊", 18, "艮宫", "五世卦"),
    ("艮", "坎"): ("山水蒙", 4, "艮宫", "游魂卦"),
    ("艮", "艮"): ("艮为山", 52, "艮宫", "本宫卦"),
    ("艮", "坤"): ("山地剥", 23, "艮宫", "归魂卦"),

    ("坤", "乾"): ("地天泰", 11, "坤宫", "一世卦"),
    ("坤", "兑"): ("地泽临", 19, "坤宫", "二世卦"),
    ("坤", "离"): ("地火明夷", 36, "坤宫", "三世卦"),
    ("坤", "震"): ("地雷复", 24, "坤宫", "四世卦"),
    ("坤", "巽"): ("地风升", 46, "坤宫", "五世卦"),
    ("坤", "坎"): ("地水师", 7, "坤宫", "游魂卦"),
    ("坤", "艮"): ("地山谦", 15, "坤宫", "归魂卦"),
    ("坤", "坤"): ("坤为地", 2, "坤宫", "本宫卦"),
}

def get_trigram(num):
    """根据数字获取卦象"""
    remainder = num % 8
    if remainder == 0:
        remainder = 8
    return TRIGRAMS[remainder]

def get_yao_position(num):
    """根据数字获取变爻位置"""
    remainder = num % 6
    if remainder == 0:
        remainder = 6
    return remainder

def change_yao(upper, lower, yao_pos):
    """根据变爻位置改变卦象"""
    # 爻位：1=初爻(下卦初), 2=二爻(下卦中), 3=三爻(下卦上)
    #       4=四爻(上卦初), 5=五爻(上卦中), 6=上爻(上卦上)

    # 找到当前卦的数字表示
    upper_num = [k for k, v in TRIGRAMS.items() if v == upper][0]
    lower_num = [k for k, v in TRIGRAMS.items() if v == lower][0]

    # 转换为二进制（乾=111, 坤=000）
    trigram_binary = {
        1: [1, 1, 1],  # 乾
        2: [0, 1, 1],  # 兑
        3: [1, 0, 1],  # 离
        4: [0, 0, 1],  # 震
        5: [1, 1, 0],  # 巽
        6: [0, 1, 0],  # 坎
        7: [1, 0, 0],  # 艮
        8: [0, 0, 0],  # 坤
    }

    upper_bits = trigram_binary[upper_num].copy()
    lower_bits = trigram_binary[lower_num].copy()

    # 改变对应的爻
    if yao_pos <= 3:
        # 下卦的爻
        lower_bits[3 - yao_pos] = 1 - lower_bits[3 - yao_pos]
    else:
        # 上卦的爻
        upper_bits[6 - yao_pos] = 1 - upper_bits[6 - yao_pos]

    # 转换回卦象
    def bits_to_trigram(bits):
        for num, b in trigram_binary.items():
            if b == bits:
                return TRIGRAMS[num]
        return None

    new_upper = bits_to_trigram(upper_bits)
    new_lower = bits_to_trigram(lower_bits)

    return new_upper, new_lower

def main():
    # 生成三个随机数
    random.seed()
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    num3 = random.randint(1, 99)

    # 获取上卦、下卦、变爻
    upper = get_trigram(num1)
    lower = get_trigram(num2)
    yao_pos = get_yao_position(num3)

    # 获取本卦信息
    original_hex = HEXAGRAMS.get((upper, lower))
    if not original_hex:
        print(f"错误：找不到卦象 ({upper}, {lower})")
        sys.exit(1)

    hex_name, hex_num, palace, hex_type = original_hex

    # 计算之卦
    new_upper, new_lower = change_yao(upper, lower, yao_pos)
    changed_hex = HEXAGRAMS.get((new_upper, new_lower))
    if not changed_hex:
        print(f"错误：找不到变卦 ({new_upper}, {new_lower})")
        sys.exit(1)

    changed_name, _, changed_palace, _ = changed_hex

    # 爻位名称
    yao_names = ["初爻", "二爻", "三爻", "四爻", "五爻", "上爻"]

    # 输出结果
    print("=== 易经起卦 ===")
    print(f"随机数：{num1}, {num2}, {num3}")
    print(f"上卦：{upper}{TRIGRAM_ATTRS[upper]} ({num1}%8={num1%8 if num1%8!=0 else 8})")
    print(f"下卦：{lower}{TRIGRAM_ATTRS[lower]} ({num2}%8={num2%8 if num2%8!=0 else 8})")
    print(f"变爻：{yao_names[yao_pos-1]} ({num3}%6={num3%6 if num3%6!=0 else 6})")
    print()
    print(f"本卦：{hex_name}({palace}-{hex_type})")
    print(f"之卦：{changed_name}({changed_palace})")
    print()
    print(f"完整表达：{hex_name}({palace}-{hex_type}) 之 {changed_name}({changed_palace})")
    print(f"变爻位置：{yao_names[yao_pos-1]}")
    print()
    print(f"参考链接：https://www.zhouyi.cc/zhouyi/yijing64/{hex_num:02d}.html")

if __name__ == "__main__":
    main()
