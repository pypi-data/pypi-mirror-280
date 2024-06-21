import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 33
project_path = file_path[0:end]
sys.path.append(project_path)


# 下单
def order_buy(symbol, buy_price, buy_volume):
    return None


# 自动一键打新
def auto_ipo_buy():
    return None


# 卖出
def order_sell(symbol, sell_price, sell_volume):
    return None


# 取消
def order_cancel(entrust_no):
    return None
