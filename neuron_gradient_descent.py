# -*- coding: utf-8 -*-
"""
让神经元学习到逻辑与这个规则
@author: 知乎@Ai酱
"""
# 先随便猜w1,w2,b是多少
w1 = 0.666
w2 = 0.333
b = 0.233



def train():
    # 用于训练的数据（四行）一行样本数据格式为 [x1,x2,g(x1,x2)]
    data = [
            [1,  0,     -1],
            [0,  1,     -1],
            [0,  0,     -1],
            [1,  1,     1]
            ]
    global w1,w2,b # 告诉计算机我修改的是全局变量（每个函数都能修改这个变量）
    
    epoch = 20 # 同样的数据反复训练20次
    for _ in range(epoch):
        # 逐个样本更新权重
        for i in data:
            # 这里的i = [x1,x2,g(x1,x2)]，它是data中的一行
            # 求各自导函数在(x1,x2,g(x1,x2))处的导函数值
            d_w1 = 2*(w1*i[0]+w2*i[1]+b-i[2])*i[0]
            d_w2 = 2*(w1*i[0]+w2*i[1]+b-i[2])*i[1]
            d_b = 2*(w1*i[0]+w2*i[1]+b-i[2])
            
            # 接下来就是愉快的理性猜环节了        
            # 设置学习率，防止蹦的步子太大
            learning_rate = 0.01
            # 下次猜的数 = 本次猜的数 - 学习率*导数值
            w1_next = w1 - learning_rate*d_w1
            w2_next = w2 - learning_rate*d_w2
            b_next = b - learning_rate*d_b
            
            # 更新各参数
            w1 = w1_next
            w2 = w2_next
            b = b_next
            
            pass
        pass


def f(x1,x2):
    """
    这是一个神经元（本质就是一个表达式）
    经过训练，我们期望它的返回值是x1&x2
    返回值是 w1*x1+w2*x2 + b > 0? 1:0;
    计算这个用于判断(x0,x1)的分类。
    大于0则是点(x0,x1)在右上输出1，小于0则点在左下输出0；
    """
    global w1,w2,b # 告诉计算机我修改的是全局变量（每个函数都能修改这个变量）
    if w1*x1+w2*x2 + b > 0:
        return 1
    else:
        return 0


# 我们首先执行下训练，让神经元自己根据四条数据学习逻辑与的规则
train()
# 打印出模型计算出来的三个比较优的参数
print(w1,w2,b)
"""
输出：0.4514297388906616 0.2369025056182418 -0.611635769357402
"""

# 好我们测试下，看神经元有没有自己学习到逻辑与的规则
print("0&1",f(0,1))
print("1&0",f(1,0))
print("0&0",f(0,0))
print("1&1",f(1,1))
"""
输出：
0&1= 0
1&0= 0
0&0= 0
1&1= 1
"""