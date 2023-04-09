s = input()


def is_pellindrome(s):
    return s == s[::-1]


idx = 0

while True:
    if is_pellindrome(s):
        print(len(s))
        break
    else:
        x = s[:len(s) - idx]
        y = s[idx]
        z = s[len(s)- idx:]
        s = x+y+z
        idx += 1

