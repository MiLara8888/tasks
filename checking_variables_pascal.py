#проверить можно ли использовать переменную в языке паскаль
n=input()
def checking(x):
    return (all(64<ord(i)<123  or ord(i)==95 or 47<ord(i)<58 for i in n) and n[0] not in "1234567890")
print(checking(n))



