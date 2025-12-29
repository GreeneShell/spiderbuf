from DrissionPage import ChromiumPage
from pprint import pprint
from pathlib import Path
from tqdm import tqdm
import json
import re
import requests

script_dir = Path(__file__).parent

m3u8_url = "https://c760ffea7f178701fa95b1026c2f500d.v.smtcdns.com/moviets.tc.qq.com/Z_5iGYvBq7paEe6a35N4zjMlVEndInx1sEESlIKHSpsySXO2f_ZFY-Tb0SjTyEHx3HarcXzevJkCv4zhs_CwKs5Hgzti-wutWKPDdoOLCcnm2AFxPGpKJRrImEKQQse97VIe1dJ4Ob-ItC_ESS-lQc53Y5PDhpy_Pepfha1tP3HxE=/B_WtMvpihMdCkFS7pzpMyZflTQciqGyOZBXebdVaBxpKQ1VeDuwzfaRrMOXP3qAwzW0UJDIxUl_KYRNVqumoVGZdvsF2PnEIa4NixLhTpHirRnjjB60aJR8DHxKMJSA1VF_lQvo8wGU93_iGZi2QGpkQ/svp_50112/XkA_-xuPvgJX8ZbmDLMhi_fbSvpB05LPtojiKDru6iejVUQGMvyXqWW43sgw99zTxJHpS8oVSRmasow3KWG3ab6bQt5UNg-G050cbdrthSm0IdDyWLpTqe6xoXuD6wlTQpUUmrQW79MTA7dzi87TgReDlNFBLTf3HGwIQPB1CpOlGp-7Knltx9vOHec_lnAhIsVJemQ6LNLYXjriaYO25sV6vZGr2XtrFshIKQauZ-a_E8-zQsHkFg/gzc_1000102_0b53peacqaaavaajq7cmebu4a6odfb7qalca.f322457.ts.m3u8?ver=4"
m3u8 = requests.get(m3u8_url).text
ts_name = "/".join(m3u8_url.split("/")[:-1]) + "/"
ts_list = re.findall(",\n(.*?)\n", m3u8)
# 循环提取列表元素，拼接完整链接
for ts in tqdm(ts_list):
    # 构建完整地址
    ts_url = ts_name + ts
    # 获取ts分片内容
    ts_content = requests.get(ts_url).content
    # 保存ts分片文件
    with open(script_dir / "tencent_videos" / "svip.mp4", "ab") as f:
        f.write(ts_content)
    # pprint("ts_list: " + ts_list[i])
