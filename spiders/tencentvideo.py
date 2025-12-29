from DrissionPage import ChromiumPage
from pprint import pprint
from pathlib import Path
from tqdm import tqdm
import json
import re
import requests


# 获取脚本所在目录
script_dir = Path(__file__).parent
# 打开浏览器实例
dp = ChromiumPage()
# 监听数据接口
dp.listen.start("proxyhttp")
# 访问网站
dp.get("https://v.qq.com/x/cover/mzc00200xxpsogl/j4101ouc4ve.html")
# 等待数据包加载
resp = dp.listen.wait()
# 获取响应数据
json_data = resp.response.body
with open(
    script_dir / "temp_files" / "tencentvideosvip.json", "w", encoding="utf-8"
) as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
# pprint(json_data)
# 将json数据转换为Python对象
v_info = json.loads(json_data["vinfo"])
with open(
    script_dir / "temp_files" / "tencentvideo_vinfosvip.json", "w", encoding="utf-8"
) as f:
    json.dump(v_info, f, ensure_ascii=False, indent=4)
# pprint(v_info)
# 提取m3u8链接
m3u8_url = v_info["vl"]["vi"][0]["ul"]["ui"][-1]["url"]
# pprint("m3u8_url: " + m3u8_url)
# 提取视频标题
title = v_info["vl"]["vi"][0]["ti"]
pprint("title: " + title)
# 提取m3u8文件内容
m3u8 = requests.get(m3u8_url).text
# pprint("m3u8 content:\n" + m3u8)
# 提取ts分片链接
ts_name = "/".join(m3u8_url.split("/")[:-1]) + "/"
ts_list = re.findall(",\n(.*?)\n", m3u8)
# 循环提取列表元素，拼接完整链接
for ts in tqdm(ts_list):
    # 构建完整地址
    ts_url = ts_name + ts
    # 获取ts分片内容
    ts_content = requests.get(ts_url).content
    # 保存ts分片文件
    with open(script_dir / "tencent_videos" / f"{title}svip-1.mp4", "ab") as f:
        f.write(ts_content)
    # pprint("ts_list: " + ts_list[i])
