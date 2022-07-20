K = int(input())

h, m = 21, 0

h += int(K/60)
m += K % 60

print('{}:{}'.format(h,str(m).zfill(2)))