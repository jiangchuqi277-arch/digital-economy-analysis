import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据
data = {
    "年份": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "数字经济规模(万亿)": [18.6, 22.3, 26.4, 31.3, 35.8, 39.2, 45.5, 50.2, 55.4],
    "GDP(万亿)": [68.6, 74.0, 83.2, 91.9, 98.7, 103.5, 114.3, 120.4, 126.1],
    "占GDP比重(%)": [27.1, 30.1, 31.7, 34.1, 36.2, 37.9, 39.8, 41.7, 43.9]
}

df = pd.DataFrame(data)

# 画图
plt.figure(figsize=(10,5))
plt.plot(df["年份"], df["占GDP比重(%)"], marker="o", linewidth=3, color="#4285F4")
plt.title("中国数字经济占GDP比重（2015-2023）", fontsize=14)
plt.xlabel("年份")
plt.ylabel("占比 (%)")
plt.grid(alpha=0.3)
plt.savefig("digital_economy_trend.png", dpi=300)
plt.show()