def fibinfinite():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

#----------------------------
def fibobounded(n):
  a, b = 0, 1
  while True:
    if a > n: return

    yield a
    a, b = b, a + b
#---------------------------

fi = fibinfinite()
total = 0

for x in fi:
  if (x%2 == 0):
    total += x

  if (x > 4000000): break

print(total)

fb = fibobounded(4000000)
total = 0

for x in fb:
  if (x%2 == 0):
    total += x

print(total)
        