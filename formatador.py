ns = ""

while True:
  n = input()
  if(n == 'okok'): break
  ns += f'"{n}",\n'

print()
for i in ns:
  print(i, end='')
