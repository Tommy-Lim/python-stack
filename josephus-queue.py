from collections import deque

def josephus(names, num):
    qq = deque()
    for name in names:
        qq.append(name)
    while len(qq)>1:
        for i in range(1,num+1):
            if i == num:
                print(i, qq.popleft(), "eliminated")
                # qq.popleft()
            else:
                person = qq.popleft()
                qq.append(person)
                print(i, person, "saved")
                # append(qq.popleft())

    print(qq.pop(), "survived")


names = ["Charlie", "Moe", "Curly", "johhny", "milo"]
josephus(names, 2)
