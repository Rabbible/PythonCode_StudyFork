
print('欢迎来到嘤嘤嘤网，请选择注册或者登录')
name_list = []
code_list = []
black_list = []


# 读取已存在的用户信息
def read():
    with open('用户资料.txt', 'a+', encoding='utf-8') as f1:
        f1.seek(0)
        file_list = f1.readlines()
        for i in file_list:
            i_ = i.strip()
            a = i_.split(':')
            name_list.append(a[0])
            code_list.append(a[1])


read()


# 实现注册功能
def register():
    site1 = True  # 设置一个变量控制外循环
    while site1:
        # 用户输入用户名
        user_name = input('输入您的用户名：')
        if user_name in name_list:
            print('用户名已存在,请重新输入')
        else:
            while True:
                code1 = input('请输入密码：')
                code2 = input('请确认密码：')
                # 判断两次密码是否一致
                if code1 == code2:
                    with open('用户资料.txt', 'a+', encoding='utf-8') as f2:
                        f2.write(f'{user_name}:{code2}\n')
                        print(f'注册成功: 用户名:{user_name}')
                    site1 = False  # 结束外循环
                    break  # 结束内循环
                else:
                    print("密码不正确，请重新输入")


# 实现登录功能
def sign_in():
    read()
    with open('blackList.txt', 'a+', encoding='utf-8') as f4:  # 读取黑名单中的用户
        f4.seek(0)
        f4_list = f4.readlines()
        for i in f4_list:
            black_list.append(i.strip())
    user_list = dict(zip(name_list, code_list))  # 将读取到的正常的用户资料存入字典中，使得用户名和密码成键值对的形式
    site2 = True  # 定义一个参数控制外循环
    # 开始进行登陆
    while site2:
        input_name = input('请输入用户名：')
        if input_name not in name_list:
            print('用户名不存在，请重新输入')
        else:
            if input_name in black_list:
                print('该用户被锁定，谁叫你不记住密码，给我嘤嘤嘤')
            else:
                n = 1
                while True:
                    input_code = input('输入密码：')  # 登录密码的输入
                    # 登录密码的正确判断
                    if input_code == user_list.get(input_name) and n <= 3:
                        print('登录成功')
                        site2 = False  # 外循环结束
                        break  # 内循环结束
                    else:
                        n += 1  # 统计密码输入错误次数
                        # 根据错误次数，进行再次输入操作或锁定操作
                        if n < 4:
                            print('密码不正确，请重新输入密码')
                        if n == 4:
                            print('登录已被锁定，请联系相关人员')
                            with open('blackList.txt', 'a+', encoding='utf-8') as f3:
                                f3.write(f'{input_name}\n')
                            site2 = False
                            break


print('''输入0注册
输入1登录
输入end结束
''')
# 功能的选择
while True:
    num = input('请输入0或1或end：')
    if num == '0':
        print('请注册')
        register()

    elif num == '1':
        print('请登录,只有三次密码输入机会')
        sign_in()
        black_list = []  # 每调用一次该函数清空初始时读取到底黑名单列表，防止下次调用该函数，上一次的调用遗留下的列表数据，该处待优化
    else:
        break
    print()
