x = 20


def print_value():
    global x
    x = 10
    print('x = {0}'.format(x))


print_value()


users = ['Tony', 'THom', 'Bob', 'KK']

# users_filter = filter(lambda u: u.startswith('T'), users)
# users_map = filter(lambda u: u.lower(), users_filter)
users_map = map(lambda u: u.lower(), filter(lambda u: u.startswith('T'), users))


print(list(users_map))
