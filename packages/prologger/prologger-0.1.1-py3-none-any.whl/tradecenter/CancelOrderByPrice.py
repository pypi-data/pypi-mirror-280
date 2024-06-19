# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/8 21:25
@Auth ： yuslience
@File ：CancelOrderByPrice.py
@IDE ：CLion
@Motto: Emmo......
"""
from loguru import logger


def cancel_order_by_price_offset(tick: dict, open_orders: dict, tracing_account_td_api, config):
    """
    价格偏移撤单执行逻辑
    :param config:
    :param tracing_account_td_api:
    :param open_orders:
    :param tick:
    :return:
    """
    # 对字节类型进行解码操作
    raw_symbol = tick["code"]
    if not isinstance(raw_symbol, str):
        raw_symbol = raw_symbol.decode("utf-8")
    # 获取当前code对应的未成交订单
    order_symbol = "".join(raw_symbol.split(".")[1:])
    cur_code_orders = open_orders.get(order_symbol, {})
    if not cur_code_orders:
        return
    # 遍历所有的挂单
    for order_local_id, order in cur_code_orders.items():
        # 获取挂单价格偏移
        cur_price_offset = abs(tick["price"] - order["LimitPrice"])

        # 判断发单时间时候超过预设时间
        if cur_price_offset > config.price_offset:
            logger.info(f"Cancel OrderId By PriceOffset: {order_local_id}")

            order_sys_id = order["OrderSysID"]
            exchange = order["ExchangeID"]
            symbol = order["InstrumentID"]
            cancel_order_res = tracing_account_td_api.order_cancel1(exchange, symbol, order_sys_id)
            logger.info(f"Cancel OrderId By PriceOffset Res: {cancel_order_res}")
