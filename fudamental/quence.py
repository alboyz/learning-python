from collections import deque
antrian = deque([1, 2, 3, 4, 5])
print('antrian adalah', antrian)
# add data
antrian.append(6)
print("data masuk ", 6)
print('antrian adalah', antrian)
antrian.append(7)
print("data masuk ", 7)
print('antrian adalah', antrian)
# minus antrian
out = antrian.popleft()
print("data keluar", out)
print('antrian adalah', antrian)
