def show_info(sep=':', **info):
    # def show_info(**info, sep=':'):
    print('------info------')
    for key, value in info.items():
        print('{0} {2} {1}'.format(key, value, sep))
    return None  # return


show_info('->', name='Tony', age=18, sex=True)
# a = show_info('->', name='Tony', age=18, sex=True)
# print(a)
# 无返回值，因为def函数里无return xxx
