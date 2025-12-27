from pathlib import Path

import pandas as pd
import requests
from lxml import etree

url = "https://spiderbuf.cn/playground/s03"

# 获取脚本所在目录
script_dir = Path(__file__).parent

html_file = script_dir / "S03.html"

# 检查本地 HTML 文件是否存在，如果不存在则下载并保存，否则读取
if html_file.exists():
    with open(html_file, "r", encoding="utf-8") as f:
        html = f.read()
else:
    html = requests.get(url).text
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)

root = etree.HTML(html)
trs = root.xpath("//tr")

# 收集数据
data = []
for tr in trs:
    cells = tr.xpath("./th | ./td")  # 获取所有 th 和 td 元素
    tds = [
        cell.xpath("string(.)").strip() if cell.xpath("string(.)") else "" for cell in cells
    ]  # 如果 text 为 None，用空字符串
    print(tds)
    data.append(tds)

# 使用 pandas 创建 DataFrame 并保存为 Excel
df = pd.DataFrame(data)
df.to_excel(script_dir / "S03.xlsx", index=False, header=False)
