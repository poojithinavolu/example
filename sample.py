print('hello')
for i in range(10):
    if i == 5:
        continue
    if i == 8:
        break
    if i % 2 == 0:
        print('even')
    else:
        print('odd')
  print('i : ',i)