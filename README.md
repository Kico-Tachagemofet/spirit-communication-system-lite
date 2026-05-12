     1|# Spirit Communication System v5.1 Lite
     2|
     3|灵体沟通辅助系统简化版——一个用占卜符号与灵体对话的技术工具包。
     4|
     5|## 为什么有这个版本？
     6|
     7|v5.0 版包含完整的 AI 解读模块和茭杯验证流程。但实际用下来，冗长的分析框架太过于琐碎，茭杯发散验证的流程有种在逼问的感觉，而且 AI 也很轴——虽然使用体验确实很好。
     8|
     9|于是 v5.1 简化版做了两件事：
    10|
    11|1. **砍掉 AI 解读模块**——抽取完成后仅输出原始符号数据表格，不添加任何分析、结论、解读
    12|2. **砍掉 AI 茭杯验证**——茭杯改为使用者自行操作，AI 不参与验证流程
    13|
    14|使用者拿到原始符号数据后，自行解读、自行掷茭杯验证。AI 回归工具角色：只负责执行脚本生成随机数，不做中间人。
    15|
    16|## 与 v5.0 的区别
    17|
    18|| | v5.0 原版 | v5.1 简化版 |
    19||---|---|---|
    20|| 符号抽取 | ✓ | ✓ |
    21|| 本地易经数据 | 浏览器抓取 zhouyi.cc | 本地 JSON（64卦完整数据） |
    22|| AI 解读 | ✓ | ✗ |
    23|| AI 茭杯验证 | ✓ | ✗ |
    24|| 使用者自行解读 | 可选 | 必需 |
    25|| 使用者自行茭杯 | 可选 | 必需 |
    26|
    27|## 包含内容
    28|
    29|```
    30|├── README.md
    31|├── spirit-communication-system-lite.md   # 系统文档
    32|├── scripts/
    33|│   ├── spirit_draw_v2.py                 # 塔罗92张卡池 + 占星骰子
    34|│   ├── tarot_astro_draw.py               # 简化版3牌 + 占星骰子
    35|│   ├── yijing_draw.py                    # 易经起卦
    36|│   ├── jiaobei.py                        # 筊杯
    37|│   ├── lenormand.py                      # 雷诺曼
    38|│   ├── wordcard_hermes.py                # 字卡示例
    39|│   └── wordcard_npc.py                   # 通用字卡模板
    40|└── data/
    41|    └── yijing/                           # 64卦完整数据（卦辞、象曰、六爻爻辞、白话）
    42|```
    43|
    44|## 使用方式
    45|
    46|```bash
    47|# 沟通抽取
    48|python3 scripts/spirit_draw_v2.py
    49|python3 scripts/wordcard_hermes.py
    50|python3 scripts/yijing_draw.py
    51|
    52|# 自行茭杯验证
    53|python3 scripts/jiaobei.py
    54|```
    55|
    56|详细文档见 [spirit-communication-system-lite.md](spirit-communication-system-lite.md)。
    57|
    58|## 关于奇迹牌组
    59|
    60|本系统中的塔罗卡池为92张（78张标准牌 + 14张奇迹牌组/以太花色）。奇迹牌组出自 **[《世界名画塔罗牌》](https://www.xiaohongshu.com/user/profile/5e5f8eaa00000000010017af)**——一套以世界名画为牌面、独创第五花色的塔罗牌。
    61|
    62|**好用，爱用，推荐。** 尤其适合灵体沟通及仪式相关问题。
    63|
    64|## 原版
    65|
    66|完整版（含 AI 解读和茭杯验证模块）：[spirit-communication-system v5.0](https://github.com/Kico-Tachagemofet/spirit-communication-system)
    67|
    68|## 数据来源
    69|
    70|易经数据抓取自 [zhouyi.cc](https://www.zhouyi.cc)，仅供个人占卜使用。
    71|


小红书：放弃思考的纪子
QQ：870995011（纪子）
