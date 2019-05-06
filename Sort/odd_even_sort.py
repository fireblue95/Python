def odd_even_sort(content):
  length = len(content) - 1
  while(True):
    sort = True
    for i in range(0, length, 2):
      if(content[i] > content[i + 1]):
        value = content[i + 1]
        content[i + 1] = content[i]
        content[i] = value
        sort = False
    for i in range(1, length, 2):
      if(content[i] > content[i + 1]):
        value = content[i + 1]
        content[i + 1] = content[i]
        content[i] = value
        sort = False
    if(sort):
      break
if __name__ == "__main__":
  num = input("Input num:\n").split()
  result = list()
  for i in num:
    result.append(int(i))
  odd_even_sort(result)
