for t in range(0, 16):
  a = list(input())

  index = 1
  ans = 0
  negative = 0
  if a[15] == '1':
    if a[0] == '1':
      a[0] = '0'
    else:
      for x in range(1, 16):
        if a[x] == '1':
          a[x] = '0'
          for y in range(x - 1, -1, -1):
            if a[y] == '1':
              a[y] = '0'
              break
            else:
              a[y] = '1'
          break
    for x in range(0, 16):
      if a[x] == '1':
        a[x] = '0'
      else:
        a[x] = '1'
    negative = 1

  for x in range(0, 15):
    ans = ans + index * int(a[x])
    index *= 2
  if negative == 1:
    ans *= -1
  print(ans)

