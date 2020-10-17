import time
def bubble_sort(data,drawData,speed):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                time.sleep(speed)
            drawData(data, ["green" if x == j or x == j + 1 or x >= len(data) - i else "red" for x in range(len(data))])
