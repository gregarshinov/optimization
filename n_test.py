import numpy as np

f = open("data.txt", 'r')

a = f.readline().split(" ")

n = int(a[0])

m = int(a[1][:-1])

print(n)
print(m)

data = np.zeros((n, m), dtype=np.int64)

for i in range(n):
    line = f.readline().split(" ")
    line[m-1] = line[m-1][:-1]
    for j in range(m):
        data[i,j] = int(line[j])

line = [int(x) for x in f.readline()[:-1].split(" ")]
t_m = np.array(line)

line = [int(x) for x in f.readline()[:-1].split(" ")]
t_d = np.array(line)

f.close()


def calculate_f(data, t_m, t_d):
    n1in = 0
    n0in = 0
    n1 = np.sum(data)

    for i in range(n):
        for j in range(m):
            if t_m[i] == t_d[j]:
                if data[i, j] == 1:
                    n1in += 1
                else:
                    n0in += 1

    return n1in/(n1 + n0in)


def local_search(data, t_m):
    f = calculate_f(data, t_m, t_d)
    k = max(t_m)
    if step == 1:  #t_m
        for i in range(n):
            for j in range(k):
                if j + 1 != t_m[i]:
                    t_m[i] = j + 1
                    if f < calculate_f(data, t_m, t_d):
                        break
                    t_m[i] = tmp
