counter = 0

while True:
  lineIn = input()
  if lineIn=='END':
    break
  elif lineIn=='SKIP':
      continue
  counter = counter+1
  print('line', counter, '=', lineIn)
