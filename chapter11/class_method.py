# coding=utf-8
# 代码文件：chapter11/class_method.py


class Account:
    """定义银行账户类"""

    interest_rate = 0.0668  # 类变量利率

    def __init__(self, owner, amount):
        self.owner = owner  # 定义实例变量账户名
        self.amount = amount  # 定义实例变量账户金额

    # 声明类方法
    # 类方法与类绑定，不属于个体实例，不需要与实例绑定
    @classmethod
    def interest_by(cls, amt):
        # cls 是type类型，是当前Account类型的实例
        print(cls)
        return cls.interest_rate * amt


interest = Account.interest_by(12_000.0)
print('计算利息：{0:.4f}'.format(interest))
