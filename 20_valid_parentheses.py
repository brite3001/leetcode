from math import floor
import time


def isValid(s: str) -> bool:
    brackets = {")": "(", "]": "[", "}": "{"}
    temp = []

    for bracket in s:
        if bracket in list(brackets.values()):
            # found left bracket, adding to temp list
            temp.append(bracket)
        elif bracket in brackets:
            # found a right braket, lets try remove matching left bracket from list
            # poping to preserve the order of the brackets
            if temp != [] and temp.pop() == brackets[bracket]:
                pass
            else:
                return False

    return temp == []

    # while (s.find("()") + s.find("[]") + s.find("{}")) >= -2:
    #     s = s.replace("()", "")
    #     s = s.replace("[]", "")
    #     s = s.replace("{}", "")

    # return True if len(s) == 0 else False


print(isValid("(((())))))))"))
