import requests
import json

print("正在获取地震数据，请稍候...")

url ="https://api.wolfx.jp/cenc_eqlist.json"

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("成功！数据已保存到 data.json 文件中。")
    else:
        print(f"获取失败，状态码: {response.status_code}")
except Exception as e:
    print(f"发生错误: {e}")