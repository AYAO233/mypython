#一个使用get()的简单数据库

people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name: ')

#要查找电话还是地址？
request = input('Phone number (p) or address (a)? ')

#使用正确的键
key = request #如果request既不是'p'也不是'a'
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

#使用get提供默认值
person = people.get(name,{})
label = labels.get(key, key)
result = person.get(key, 'not available')

print("{}'s {} is {}.".format(name, label, result))

print('Hello,', end='')
print('world!')