import akshare as ak
import pandas as pd
from datetime import datetime

# 自选股列表，在这里添加你的股票代码
stock_list = [
    "600036",
    "000001",
    "601318"
]

today_str = datetime.now().strftime("%Y%m%d")
watch_file = f"./daily/watchlist/{today_str}_watch.md"

def get_stock_info(code):
    df = ak.stock_zh_a_spot_em()
    row = df[df["代码"] == code]
    if row.empty:
        return None
    r = row.iloc[0]
    return {
        "code": r["代码"],
        "name": r["名称"],
        "price": r["最新价"],
        "change_pct": r["涨跌幅"],
        "volume": r["成交量"]
    }

lines = [
    f"# {today_str} 选股观察池（自动行情更新）\n",
    "|标的代码|名称|现价|涨跌幅|成交量|威科夫信号|支撑|压力|仓位|止损|备注|\n",
    "|---|---|---|---|---|---|---|---|---|---|---|\n"
]

for c in stock_list:
    info = get_stock_info(c)
    if info:
        line = f"|{info['code']}|{info['name']}|{info['price']}|{info['change_pct']}|{info['volume']}| | | | | | |\n"
        lines.append(line)

with open(watch_file, "w", encoding="utf-8") as f:
    f.writelines(lines)
print(f"已生成/更新 {watch_file}")
