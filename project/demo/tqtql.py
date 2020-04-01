import numpy as np


def validate(a):
    j, combo = 1, 1
    while j < len(a):
        if a[j] - a[j - 1] == 1:
            combo += 1
        else:
            combo = 1
        j += 1
        if combo >= 5:
            return True
    return False


def one_man(a):
    ht, ch, fq, hx = [], [], [], []
    for j in range(18):
        if a[j] >= 52:
            continue
        if a[j] % 4 == 0:
            ht.append(a[j] // 4)
        elif a[j] % 4 == 1:
            ch.append(a[j] // 4)
        elif a[j] % 4 == 2:
            fq.append(a[j] // 4)
        elif a[j] % 4 == 3:
            hx.append(a[j] // 4)

    ht.sort()
    ch.sort()
    fq.sort()
    hx.sort()

    if validate(ht) or validate(ch) or validate(fq) or validate(hx):
        print(ht)
        print(ch)
        print(fq)
        print(hx)
        return True
    else:
        return False


card = np.array(range(54))
test_times = 10000
cnt_success = 0
for i in range(test_times):
    np.random.shuffle(card)
    print("----")
    for j in range(3):
        print(card[j * 18: (j + 1) * 18])
        if one_man(card[j * 18: (j + 1) * 18]):
            cnt_success += 1
            break

score = cnt_success / test_times
print(score)

# one_man([8, 39, 1, 23, 49, 19, 31, 9, 51, 37, 3, 29, 41, 7, 47, 11, 40, 44])
