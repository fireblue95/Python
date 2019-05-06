def insertion_sort(content):
  length = len(content)
  if(length == 1):
    return content
  for i in range(1, length):
    for j in range(i, 0, -1):
      if(content[j] < content[j - 1]):
        value = content[j]
        content[j] = content[j - 1]
        content[j - 1] = value
      else:
        break
  return content
if __name__ == "__main__":
  num = input("Input the num:\n").split()
  result = list()
  for i in num:
    result.append(int(i))
  insertion_sort(result)