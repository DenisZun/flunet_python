# -*- coding:utf-8 -*-
# 二维数组表示向量

"""
len(x) 的速度会非
常快。背后的原因是 CPython 会直接从一个 C 结构体里读取对象的长度,完全不会调用任
何方法。获取一个集合中元素的数量是一个很常见的操作,在 str、list、memoryview
等类型上,这个操作必须高效。
"""

from math import hypot

class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        这就是“字符串表示形式”。repr 就是通过 __repr__ 这个特殊方法来得到一个对象的字
        如果没有实现 __repr__,当我们在控制台里打印一个向量的实例时,
        得到的字符串可能会是 <Vector object at 0x10e100070>。

        __repr__ 和 __str__ 的区别在于,后者是在 str() 函数被使用,或是在用 print 函数
        打印一个对象的时候才被调用的,并且它返回的字符串对终端用户更友好。

        __repr__前者方便我们调试和记录日志,
        __str__后者则是给终端用户看的。
        这就是数据模型中存在特殊方法 __repr__ 和 __str__ 的原因。
        """
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__ == '__main__':

    # v1 = Vector(2, 4)
    # v2 = Vector(2, 1)
    #
    # print(v1 + v2)

    v = Vector(3, 4)
    print(abs(v))
    print(v * 3)
    print(abs(v * 3))
