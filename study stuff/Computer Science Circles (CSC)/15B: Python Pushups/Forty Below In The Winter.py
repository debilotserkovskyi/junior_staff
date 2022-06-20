temp = input()

if temp.endswith('C'):
    print(str(float(temp.replace('C', '')) * 9/5 + 32)+'F')
elif temp.endswith('F'):
    print(str((float(temp.replace('F', '')) - 32) * 5/9)+'C')
