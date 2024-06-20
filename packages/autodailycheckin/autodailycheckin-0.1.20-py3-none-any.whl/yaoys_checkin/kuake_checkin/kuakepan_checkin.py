# -*- coding: utf-8 -*-
# @FileName  :kuakepan_checkin.py
# @Time      :2024/6/5 22:16
# @Author    :yaoys
# @Desc      :
import json
import os
import time

import requests
import urllib3

from yaoys_checkin.checkin_util.logutil import log_info
from yaoys_checkin.checkin_util.checkin_log import get_checkin_logger
from yaoys_checkin.model.all_class_parent import allClassParent

# 解决出现警告 Adding certificate verification is strongly advised.
urllib3.disable_warnings()
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"


class kuake(allClassParent):
    def __init__(self, **kwargs):
        super(kuake, self).__init__(**kwargs)

        self.session = None
        if self.logger is None:
            self.logger, log_config = get_checkin_logger(config_file=self.config_file, log_name=str(os.path.basename(__file__)).split('.')[0])

        self.checkin_message, self.is_success = self.kuake_sign()

        # self.get_checkin_message()

    def kuake_checkin(self):
        self.session = requests.sessions.session()

        header = {'Cookie': self.cookie, 'User-Agent': userAgent}

        account_info_url = 'https://pan.quark.cn/account/info?fr=pc&platform=pc'
        resp = self.session.get(account_info_url, headers=header, verify=False).json()
        if 'success' in resp and resp['success'] is not True:
            return "Cookie已失效,请更新"

        if 'data' not in resp:
            return '签到错误，请重试'
        account_name = resp['data']['nickname']

        url_info = "https://drive-m.quark.cn/1/clouddrive/capacity/growth/info?pr=ucpro&fr=pc&uc_param_str="
        resp = self.session.get(url=url_info, headers=header, verify=False).json()
        check_message = ''

        if 'status' in resp and resp['status'] != 200:
            return "Cookie已失效,请更新"

        if 'data' not in resp:
            return '签到错误，请重试'
        is_sign = resp.get("data", {}).get("cap_sign", {}).get("sign_daily")
        if is_sign:
            reward = resp["data"]["cap_sign"]["sign_daily_reward"] / (1024 * 1024)
            check_message = f"{account_name}: 今天已经签到过了,获得容量{reward}MB"
        else:
            sign_url = "https://drive-m.quark.cn/1/clouddrive/capacity/growth/sign?pr=ucpro&fr=pc&uc_param_str="
            body = {"sign_cyclic": "True"}
            data = self.session.post(sign_url, headers=header, data=json.dumps(body)).json()
            if 'status' in data and data['status'] != 200:
                return "Cookie已失效,请更新"
            reward = data.get("data", {}).get("sign_daily_reward", 0) / (1024 * 1024)
            check_message = f"{account_name}: 签到成功，今日签到奖励{reward}MB"
        return check_message

    def kuake_checkin_main(self):
        if self.cookie is not None and len(self.cookie) > 0:
            account_checkin_message = self.kuake_checkin()

            # 存在账户签到信息，说明成功执行了签到
            if account_checkin_message is not None and len(account_checkin_message) > 0:
                log_info(f"[Kuake_Wangpan_Account_{self.account_index}]:" + str(account_checkin_message), my_logger=self.logger)
                self.checkin_message.append(f"[Kuake_Wangpan_Account_{self.account_index}] :" + str(account_checkin_message) + "      \n")
        return self.checkin_message

    def kuake_sign(self):

        if self.checkin_verification is None or self.checkin_verification == '':
            return ''.join(self.checkin_message), False
        try:
            # bilibili请求,获取硬币
            log_info('*******************************Kuake_Wangpan checkin*******************************', my_logger=self.logger)
            if isinstance(self.checkin_verification, str) is True:
                self.cookie = self.checkin_verification
                self.account_index = 1
                self.checkin_message = self.kuake_checkin_main()
            elif isinstance(self.checkin_verification, list) is True:
                for i in range(0, len(self.checkin_verification)):
                    if isinstance(self.checkin_verification[i], dict) is True:
                        self.cookie = self.checkin_verification[i]['cookie']
                        self.account_index = i + 1
                        self.checkin_message = self.kuake_checkin_main()
                    else:
                        log_info('Kuake_Wangpan config error' + '    \n', my_logger=self.logger)
                        self.checkin_message.append('Kuake_Wangpan config error' + '    \n')

                    if self.more_time_sleep > 0:
                        time.sleep(self.more_time_sleep)
            else:
                log_info('Kuake_Wangpan config error' + '    \n', my_logger=self.logger)
                self.checkin_message.append('Kuake_Wangpan config error' + '    \n')
            log_info('*******************************Kuake_Wangpan checkin complete*******************************', my_logger=self.logger)
            return ''.join(self.checkin_message), True
        except Exception as e:
            self.checkin_message.append('main function: Kuake_Wangpan checkin error, the error is ' + str(e) + '    \n')
            log_info('main function: Kuake_Wangpan checkin error, the error is ' + str(e) + '    \n', my_logger=self.logger)
            log_info('*******************************Kuake_Wangpan error*******************************', my_logger=self.logger)
            return ''.join(self.checkin_message), False
