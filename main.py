# 这是一个简单的开源计算器测试脚本
# 作者：曾若熙

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "错误：不能除以零"
    return x / y

print("开源计算器已加载")
print("测试 5 + 3 =", add(5, 3))
print("测试 10 - 4 =", subtract(10, 4))
print("测试 6 * 7 =", multiply(6, 7))
print("测试 8 / 2 =", divide(8, 2))
