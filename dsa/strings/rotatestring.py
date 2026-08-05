def rotateString(s,goal):

    if len(s)!=len(goal):
        return False

    return goal in (s+s)

s = "rotation"
goal = "tionrota"

print(rotateString(s,goal))


