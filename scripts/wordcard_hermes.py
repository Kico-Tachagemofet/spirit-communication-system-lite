#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hermes Word Card Draw Script
从字卡文件中随机抽取3张字卡（中文）
"""

import random
import sys
import os

# 确保标准输出使用 UTF-8 编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_word_cards(file_path):
    """从文件中加载字卡池"""
    cards = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 跳过空行、注释行和 YAML front matter
                if line and not line.startswith('---') and not line.startswith('#') and ':' not in line[:10]:
                    # 移除引号
                    if line.startswith('"') and line.endswith('"'):
                        line = line[1:-1]
                    if line:
                        cards.append(line)
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"错误：读取文件时出错 - {e}", file=sys.stderr)
        sys.exit(1)

    return cards

def draw_cards(cards, n=3):
    """随机抽取 n 张字卡"""
    if len(cards) < n:
        print(f"警告：字卡池只有 {len(cards)} 张，少于请求的 {n} 张", file=sys.stderr)
        n = len(cards)

    random.seed()  # 使用系统时间作为随机种子
    drawn = random.sample(cards, n)
    return drawn

def main():
    # 获取脚本所在目录，字卡文件在 data/ 目录中
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)  # scripts 的上级目录
    card_file = os.path.join(project_root, 'data', '字卡-Hermes.md')

    # 加载字卡池
    cards = load_word_cards(card_file)

    # 抽取字卡
    drawn_cards = draw_cards(cards, 3)

    # 输出结果
    print("=== WORD CARDS (Hermes) ===")
    for i, card in enumerate(drawn_cards, 1):
        print(f"{i}. {card}")

if __name__ == "__main__":
    main()
