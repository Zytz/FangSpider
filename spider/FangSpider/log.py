#_*_coding:utf-8_*_

import logging
from datetime import datetime

class Logger():
    def __init__(self, logger):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''
        self.format_dict = {
            1: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
        }

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        nowtime = datetime.now().strftime('%Y%m%d')
        fh = logging.FileHandler('{0}.log'.format(nowtime))
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = self.format_dict[1]
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        # self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

logger = Logger(logger='fox').getlog()
