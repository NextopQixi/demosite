'''
Created on 2016年4月6日

@author: wujianxin
'''
import doctest
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

def multiply(a,b):
    """
    >>> multiply(2,3)
    6
    >>> multiply('baka~',3)
    'baka~baka~baka~'
    """
    return a*b
'''
doctest 的测试用例就像文档字符串一样，
这句话的内涵在于：测试用例的位置必须放在整个模块文件的开头，或者紧接着对象声明语句的下一行。
也就是可以被 __doc__ 这个属性引用到的地方。并非像普通注释一样写在哪里都可以。
另：
'''
if __name__ == '__main__':
    '''verbose 参数用于控制是否输出详细信息，默认为 False，如果不写，那么运行时不会输出任何东西，除非测试 fail'''
    doctest.testmod(verbose=True)   # 自动验证嵌入测试