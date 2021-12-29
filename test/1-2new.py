import sys
try:
    items = []
    while True:
        item = sys.stdin.readline().strip()
        if item == '':
            break
        item = list(map(int,list(item.split())))
        items.append(item)
    #print(items)
    for im in items:
        if len(im) == 1:
            continue
        print(im[0]+im[1])
except:
    pass