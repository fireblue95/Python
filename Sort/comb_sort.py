def comb_sort(content):
  length = len(content)
  gap = length
  swap = 1
  while(gap > 1 or swap):
    if(gap > 1):
      gap = int(gap * 0.8)
    swap = 0
    for i in range(length - gap):
      if(content[i] > content[i + gap]):
        value = content[i + gap]
        content[i + gap] = content[i]
        content[i] = value
        swap = 1
if __name__ == "__main__":
  num = input("Input the num:\n").split()
  result = list()
  for i in num:
    result.append(int(i))
  comb_sort(result)
