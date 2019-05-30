a = [3, 0, 2, 5, -1, 4, 1]

n = 0
m = len(a) - 2

i = len(a)-1
pivot = a[i]

while n < m:
	if a[n] > pivot or a[m] < pivot:
		temp = a[m]
		a[m] = a[n]
		a[n] = temp
	n += 1
	m -= 1
b = 0
if n < m:
    b = n
else:
    b = m
if pivot < a[b-1]:
    a[i] = a[b-1]
    a[b-1] = pivot
elif pivot < a[b]:
    a[i] = a[b]
    a[b] = pivot

print(a)