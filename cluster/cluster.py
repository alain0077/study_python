import csv

cluster_num = 9
clusters = []
result = []
results = []
lists = []

#### 表データの読み込み ####

with open('データA.csv') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

for l in data:
    print(l)

del data[0]

for list in data:
    l1 = []
    l3 = []
    
    for n in list[1:len(list)]:
        l2 = [float(n)]

        l1.append(l2)
        l3.append(l2[0])  

    c = [list[0]]

    l1 = [c, l1]
    l3 = [c, l3, 0]

    lists.append(l1)
    clusters.append(l3)


#### 各データ間の距離の初期値を設定 ####

i = 1
result = []
for list1, c1 in zip(lists[1:], clusters[1:]):
    l = []
    s = []

    for list2, c2 in zip(lists[0:i], clusters[0:i]):
        sum = 0

        for l1, l2, s1, s2 in zip(list1[1], list2[1], c1[1], c2[1]):
            avg = ((s1 + s2) / (len(list1[0])+ len(list2[0])))
            
            for n in l1:
                sum += (n-avg)**2
        
            for n in l2:
                sum += (n-avg)**2

        s.append(sum)
        
    l = [list1[0], s]

    result.append(l)

    i += 1


#### クラスタリング ####

while len(clusters) != cluster_num:
    row = 1
    col = 0
    min = result[row-1][1][col]

    i = 1

    for l in result:
        j = 0
    
        for n in l[1]:
            if min > n:
                row = i
                col = j
                min = n

            j += 1

        i += 1

    if row > col:
        tmp = row
        row = col
        col = tmp

    l1 = []
    c = []
    list = []

    l1.extend(lists[row][0])
    l1.extend(lists[col][0])

    for n, m in zip(lists[row][1], lists[col][1]):
        l2 = []
        l2.extend(n)
        l2.extend(m)
        list.append(l2)

    for n, m in zip(clusters[row][1],clusters[col][1]):
        c.append(n + m)

    list = [l1, list]
    l1 = [l1, c, min + clusters[row][2] + clusters[col][2]]

    lists.append(list)
    clusters.append(l1)

    l = []

    l.append(lists[row][0])
    l.append(lists[col][0])
    l.append(min)
    l.append(l1[0])

    results.append(l)

    if row < col:
        lists.pop(col)
        lists.pop(row)
    else:
        lists.pop(row)
        lists.pop(col)

    if row < col:
        clusters.pop(col)
        clusters.pop(row)
    else:
        clusters.pop(row)
        clusters.pop(col)

    i = 1
    result = []

    for list1, c1 in zip(lists[1:], clusters[1:]):
        l = []
        s = []

        for list2, c2 in zip(lists[0:i], clusters[0:i]):
            sum = 0

            for l1, l2, s1, s2 in zip(list1[1], list2[1], c1[1], c2[1]):
                avg = (s1 + s2) / (len(list1[0])+ len(list2[0]))
            
                for n in l1:
                    sum += (n-avg)**2
            
                for m in l2:
                    sum += (m-avg)**2
            
            sum -= (c1[2] + c2[2])

            s.append(sum)
        
        l = [list1[0], s]

        result.append(l)

        i += 1


#### 分析結果の表示 ####

print('-----------------------------------------------------------')

i = 0
for l in results:
    i += 1
    print('%d' % i, end=" : ")
    print(l)

print('---------------------------------------------------------')

for l in clusters:
    print(l[0])