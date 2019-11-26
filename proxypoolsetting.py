# 基础设置

class ProxyPoolSetting():
    def __init__(self):
        # 最大代理池条数
        self.P00L_UPPER_THRESHOLD = 10000
        # 状态码
        self.VALID_STATUS_CODES = [200]
        # 测试代理网站
        self.TEST_URL = 'http://www.baidu.com'
        # 批量测试最大值
        self.BATCH_TEST_SIZE = 100
        # 休眠时间
        self.TESTER_CYCLE = 20
        self.GETTER_CYCLE = 30
        # 模块开关
        self.TESTER_ENABLED = True
        self.GETTER_ENABLED = True
        self.API_ENABLED = True