# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  JLX-helper
# FileName:     order_service.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/06/07
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from json import dumps
from jlx_helper.api import JLXApi
from jlx_helper.libs import logger
from jlx_helper.config import url_map, card_type_map, age_type_map
from jlx_helper.utils import timestamp_to_datetime_str, get_age, get_gender_code, get_current_dt_str, get_ulid_str


class OrderService(object):

    def __init__(self, user: str = None, password: str = None):
        self.__user = user or url_map.get("auth_username")
        self.__password = password or url_map.get("auth_password")
        self.__client = JLXApi(domain=url_map.get("domain"), protocol=url_map.get("procotol"))

    @property
    def user(self):
        return self.__user

    def get_token(self) -> str:
        response_data = self.__client.get_authorization_token(
            method="post", path=url_map.get("get_authorization_token"), user=self.__user, password=self.__password
        )
        token = ""
        if response_data.get("code") == 0 and response_data.get("success") is True:
            token = response_data.get("data").get("token")
            expire_time = response_data.get("data").get("expireTime")
            expire_time_str = timestamp_to_datetime_str(timestamp=expire_time)
            logger.debug("获取就旅行api鉴权token值：{}，有效期至：{}".format(token, expire_time_str))
        else:
            logger.warning("获取就旅行api鉴权token失败，接口返回内容：{}".format(dumps(response_data)))
        return token

    def get_flight_quotation(self, ticket_channel: str, channel_user: str, channel_password: str, departure_date: str,
                             departure_city_code: str, arrive_city_code: str, flight_no: str, cabin: str = None,
                             channel_token: str = None, jlx_token: str = None, product_type: str = 'cpa',
                             trace_id: str = None, trip_type: str = 'single_trip') -> dict:
        if not jlx_token:
            jlx_token = self.get_token()
            if not jlx_token:
                return dict()
        if trace_id is None:
            trace_id = get_ulid_str()
        response_data = self.__client.get_query_quotation(
            method="post", path=url_map.get("get_query_quotation"), token=jlx_token, ticket_channel=ticket_channel,
            channel_user=channel_user, channel_password=channel_password, departure_city_code=departure_city_code,
            arrive_city_code=arrive_city_code, departure_date=departure_date, flight_no=flight_no, cabin=cabin,
            channel_token=channel_token, product_type=product_type, trip_type=trip_type, trace_id=trace_id
        )
        if response_data.get("code") == 0 and response_data.get("success") is True:
            return dict(
                ticket_channel=ticket_channel, channel_user=channel_user, channel_password=channel_password,
                departure_date=departure_date, departure_city_code=departure_city_code, flight_no=flight_no,
                arrive_city_code=arrive_city_code, cabin=cabin, channel_token=channel_token, product_type=product_type,
                trip_type=trip_type, quotation_result=response_data.get("data")) if isinstance(
                response_data.get("data"), list
            ) and len(response_data.get("data")) > 0 else dict()
        else:
            logger.warning("渠道：{}，账号：{}，通过就旅行平台查询航班<{}>报价失败，原因：{}".format(
                ticket_channel, channel_user, flight_no, response_data.get("msg"))
            )
        return dict()

    def gen_jlx_order(self, ticket_channel: str, channel_user: str, order_id: int, departure_date: str,
                      departure_city_code: str, arrive_city_code: str, flight_no: str, passengers: list,
                      internal_phone: str, internal_contact: str, cabin: str = None, jlx_token: str = None,
                      price_context: str = None, conditions: list = None, trip_type: str = 'single_trip') -> dict:
        if not jlx_token:
            jlx_token = self.get_token()
            if not jlx_token:
                return dict()
        passengers = [{
            "passageName": x.get("passenger"), "cardType": card_type_map.get(x.get("card_type")),
            "cardNo": x.get("card_id"), "ageType": age_type_map.get(x.get("passenger_type")),
            "age": x.get("age") or get_age(birth_date=x.get("birth_day"), card_id=x.get("card_id")),
            "gender": get_gender_code(gender=x.get("gender")), "nationality": x.get("nationality"),
            "cardExpired": x.get("card_expired"), "cardIssuePlace": x.get("card_issue_place"),
            "birthDay": x.get("birth_day"), "phone": x.get("mobile")
        } for x in passengers]
        response_data = self.__client.gen_service_order(
            method="post", path=url_map.get("gen_service_order"), token=jlx_token, ticket_channel=ticket_channel,
            channel_user=channel_user, order_id=order_id, departure_city_code=departure_city_code, flight_no=flight_no,
            arrive_city_code=arrive_city_code, departure_date=departure_date, passengers=passengers, cabin=cabin,
            internal_phone=internal_phone, price_context=price_context, conditions=conditions, trip_type=trip_type,
            internal_contact=internal_contact
        )
        if response_data.get("code") != 0 or response_data.get("success") is False:
            logger.warning("渠道：{}，账号：{}，预售单：{}，通过就旅行平台创建订单失败，原因：{}".format(
                ticket_channel, channel_user, order_id, response_data.get("msg"))
            )
        data = response_data.get("data") or dict()
        return dict(
            ch_order_id=data.get("orderNo"), success=response_data.get("success"),
            out_ticket_amount=str(data.get("price")) if data.get("price") else None, code=response_data.get("code"),
            book_context=data.get("orderContext"), message=response_data.get("msg"),
            pre_order_id=order_id, ticket_channel=ticket_channel, channel_user=channel_user
        )

    def payment_jlx_order(self, ticket_channel: str, channel_user: str, pre_order_id: int, jlx_order_id: str,
                          pay_type: str, jlx_token: str = None, bank_card_info: dict = None,
                          pay_user_info: dict = None) -> dict:
        if not jlx_token:
            jlx_token = self.get_token()
            if not jlx_token:
                return dict()
        response_data = self.__client.payment_service_order(
            method="post", path=url_map.get("payment_service_order"), token=jlx_token, ticket_channel=ticket_channel,
            channel_user=channel_user, jlx_order_id=jlx_order_id, pay_type=pay_type, bank_card_info=bank_card_info,
            pay_user_info=pay_user_info
        )
        if response_data.get("code") != 0 or response_data.get("success") is False:
            logger.warning("渠道：{}，账号：{}，预售单：{}，就旅行订单：{} 支付未完成，原因：{}".format(
                ticket_channel, channel_user, pre_order_id, jlx_order_id, response_data.get("msg"))
            )
        # 0出票中，1出票完成，2出票失败
        payment_account = pay_user_info.get("username") if isinstance(pay_user_info, dict) else ""
        data = response_data.get("data") or dict()
        return dict(
            ch_order_id=data.get("orderNo"), code=response_data.get("code"), payment_type=pay_type,
            payment_amount=str(data.get("price")) if data.get("price") else None, payment_time=get_current_dt_str(),
            payment_context=data.get("orderContext"), payment_account=payment_account,
            success=response_data.get("success"), message=response_data.get("msg"), pre_order_id=pre_order_id,
            payment_status=data.get("status"), bill_no=data.get("billNo")
        )

    def get_jlx_order_itinerary_info(self, ticket_channel: str, channel_user: str, jlx_order_id: str,
                                     pre_order_id: int, jlx_token: str = None, order_context: str = None) -> dict:
        if not jlx_token:
            jlx_token = self.get_token()
            if not jlx_token:
                return dict()
        response_data = self.__client.get_itinerary_info(
            method="post", path=url_map.get("payment_service_order"), token=jlx_token, ticket_channel=ticket_channel,
            channel_user=channel_user, jlx_order_id=jlx_order_id, order_context=order_context
        )
        if response_data.get("code") != 0 or response_data.get("success") is False:
            logger.warning("渠道：{}，账号：{}，预售单：{}，就旅行订单：{} 获取票号失败，原因：{}".format(
                ticket_channel, channel_user, pre_order_id, jlx_order_id, response_data.get("msg"))
            )
        data = response_data.get("data") or dict()
        # 0出票中，1出票完成，2出票失败
        return dict(
            jlx_order_id=data.get("orderNo"), code=response_data.get("code"), error_message=data.get("errorMsg"),
            status=data.get("status"), success=response_data.get("success"), message=response_data.get("msg"),
            pre_order_id=pre_order_id, tickets=data.get("tickets") if isinstance(data.get("tickets"), list) else list())


if __name__ == "__main__":
    ser = OrderService()
    t = ser.get_token()
    logger.info(t)
