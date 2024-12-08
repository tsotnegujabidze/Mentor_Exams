# 1) Check If Two Strings Are Anagrams

def checking(num1, num2):
    num1 = num1.replace(' ', '').lower()
    num2 = num2.replace(' ', '').lower()
    return sorted(num1) == sorted(num2)

print(checking("triangle", "integral"))