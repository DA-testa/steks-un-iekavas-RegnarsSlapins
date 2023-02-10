# python3
"""
2) Ko darit gadijuma, ja lietotajs ievada tikai aizverosas iekavas? })}]]
"""
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            try:
                if are_matching(opening_brackets_stack[-1], next):
                    opening_brackets_stack.pop()
                else:
                    return i+1
                pass
            except:
                return i+1
    if len(opening_brackets_stack) != 0:
        return i+1
    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()