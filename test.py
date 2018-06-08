#coding=utf-8

print eval("3 + 2")

a = {
    'a': 3,
    'b': 9,
    'result': 0
}

exec("result = a + b", a)

print a['result']