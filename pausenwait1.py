x = 1

j = 1
while True:
  s = raw_input('Input [{0:d}]: '.format(j))
  j += 1
  n = len(s)
  if n > 0 and s.lower() == 'break'[0:n]:
    break
  exec(s)

print 'x = ', x
print 'I am out of the loop.'