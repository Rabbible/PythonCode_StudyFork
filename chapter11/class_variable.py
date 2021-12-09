# coding=utf-8
# 代码文件：chapter11/class_variable.py

# 针对以下例子做的分析：
# 类变量：所有账户共享
# 实例变量：与账户个体实例有关
class Account:
    """定义银行账户类"""

    interest_rate = 0.0668  # !类变量! 利率

    def __init__(self, owner, amount):
        # self 指向当前对象实例的引用
        self.interest_rate1 = None
        self.owner = owner  # 定义 !实例变量! 账户名
        self.amount = amount  # 定义 !实例变量! 账户金额


account = Account('Tony', 1_800_000.0)

print('账户名：{0}'.format(account.owner))
print('账户金额：{0}'.format(account.amount))
print('利率：{0}'.format(Account.interest_rate))

# 不要通过实例存取类变量数据。
# 当通过实例读取变量时，python解释器会先在实例中寻找这个变量，如果没有再到类中去找；
# 当通过实例为变量赋值时，无论类中是否有该同名变量，python解释器都会创建一个同名实例变量。
print('Account利率：{0}'.format(Account.interest_rate))
print('ac1利率：{0}'.format(account.interest_rate1))

print('ac1实例所有变量：{0}'.format(account.__dict__))
account.interest_rate = 0.01
account.interest_rate2 = 0.01
print('ac1实例所有变量：{0}'.format(account.__dict__))
