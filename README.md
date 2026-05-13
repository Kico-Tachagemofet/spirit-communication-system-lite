# Spirit Communication System v5.1 Lite

灵体沟通辅助系统简化版。它负责抽取原始符号材料，把塔罗、字卡、占星骰子、易经等结果整理成表格；解读、追问和筊杯验证交给使用者自己判断。

这一版承担的工作很明确：让 AI 回到工具位，执行脚本、生成随机结果、输出原始材料。

## 适合谁

- 已经有自己的解读习惯，只需要干净的抽取结果。
- 希望减少 AI 代读、代问、代验证带来的干扰。
- 日常需要把塔罗、字卡、占星骰子、易经放在同一轮记录里。
- 想把原始结果交给其他 Skill 继续处理，例如塔罗交给 Symbol Anchor Check，易经交给梅花易数 Skill。

## 与 v5.0 的区别

v5.0 是 AI Agent 全流程版：抽取、解读、Roleplay、筊杯验证和自动海龟汤都会由 Agent 推进。它的体验更完整，适合想测试沉浸式 Agent 协作的人。

v5.1 Lite 是边界修正版。它保留符号抽取，移除 AI 解读、AI 筊杯验证和自动追问流程。原因很简单：有些问题技术上可以继续问，关系上需要停。Lite 把是否继续追问的权力留给使用者。

| 功能 | v5.0 全流程版 | v5.1 Lite |
|---|---|---|
| 符号抽取 | 有 | 有 |
| 塔罗 92 张卡池 | 有 | 有 |
| 字卡脚本 | 有 | 有 |
| 占星骰子 | 有 | 有 |
| 易经本地数据 | 有 | 有 |
| AI 解读 | 有 | 移除 |
| AI 筊杯验证 | 有 | 移除 |
| 自动海龟汤追问 | 有 | 移除 |
| 使用者自行解读 | 可选 | 核心流程 |
| 使用者自行决定是否追问 | 可选 | 核心流程 |

## 推荐搭配

日常推荐工作流：

1. 用 v5.1 Lite 抽取原始符号材料。
2. 塔罗结果交给 [Symbol Anchor Check](https://github.com/Kico-Tachagemofet/symbol-anchor-check) 做 Book T 属性校验。
3. 易经结果交给 [梅花易数 Skill](https://github.com/Kico-Tachagemofet/meihua-yishu) 走体用、生克、旺衰、主互变和取象。
4. 使用者自己判断本轮沟通说到哪里，是否继续追问。

可以理解为：

- v5.1 Lite 给材料。
- Anchor Check 管塔罗属性。
- 梅花易数 Skill 管卦象流程。
- 使用者保留分寸、关系边界和最终判断。

## 包含内容

```text
spirit-communication-system-lite/
├── README.md
├── spirit-communication-system-lite.md   # Agent / Skill 使用说明
├── scripts/
│   ├── spirit_draw_v2.py                 # 六位塔罗牌阵 + 占星骰子
│   ├── tarot_astro_draw.py               # 简化三牌 + 占星骰子
│   ├── yijing_draw.py                    # 易经起卦
│   ├── jiaobei.py                        # 筊杯，供使用者自行调用
│   ├── jiaobei_gua.py                    # 筊杯起卦
│   ├── lenormand.py                      # 雷诺曼
│   ├── wordcard_hermes.py
│   └── wordcard_npc.py                   # 通用字卡模板
└── data/
    └── yijing/                           # 64 卦本地数据
```

## 使用方式

```bash
# 塔罗六位牌阵 + 占星骰子
python3 scripts/spirit_draw_v2.py

# 字卡示例
python3 scripts/wordcard_hermes.py
python3 scripts/wordcard_astarion.py

# 易经起卦
python3 scripts/yijing_draw.py

# 使用者自行验证或补充抽取
python3 scripts/jiaobei.py
python3 scripts/lenormand.py
python3 scripts/tarot_astro_draw.py
```

Agent / Skill 详细流程见 [spirit-communication-system-lite.md](spirit-communication-system-lite.md)。

## 输出边界

v5.1 Lite 的输出只包含原始结果和必要的数据字段：

- 塔罗牌名、位置、正逆位。
- 字卡原文。
- 占星骰子的行星、星座、宫位、尊贵状态、飞星。
- 易经本卦、变爻、之卦、卦辞、爻辞、象辞和白话。
- 四元素统计，奇迹牌组单独处理。

它不会输出结论、建议、关系判断或后续追问。需要解读时，请显式调用其他 Skill，或由使用者自行分析。

## 关于奇迹牌组

本系统中的塔罗卡池为 92 张：78 张标准塔罗 + 14 张奇迹牌组。奇迹牌组出自 [《世界名画塔罗牌》](https://www.xiaohongshu.com/user/profile/5e5f8eaa00000000010017af)，这是一套以世界名画为牌面、带有独创第五花色的塔罗牌。

奇迹牌组在本系统中用于描述人格结构、内在转化和仪式性经验。它不计入四元素统计，出现时需要单独处理。

## 来源与边界

本项目包含四类内容：

1. 传统与公开来源：塔罗、占星骰子、易经文本、筊杯、雷诺曼等符号系统。
2. 作者整理：六位牌阵、字卡脚本、输出格式、四元素统计、v5.1 Lite 使用流程。
3. 程序生成：脚本随机抽取结果、本地 JSON 数据读取、表格输出。
4. AI 参与：在 Lite 流程中仅承担执行和整理任务；解读、验证、追问由使用者决定。

易经数据抓取自 [zhouyi.cc](https://www.zhouyi.cc)，仅供个人占卜、符号分析、创作和实验性工作流使用。

本项目不提供现实决策担保，不替代医疗、法律、财务或心理咨询建议。

## 原版

完整版见 [spirit-communication-system v5.0](https://github.com/Kico-Tachagemofet/spirit-communication-system)。

## License

MIT
