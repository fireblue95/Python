def gnome_sort(content):
  length = len(content)
  count = 0
  while(count < length):
    print(content)
    if(count == 0 or content[count] >= content[count - 1]):
      count = count + 1
    else:
      value = content[count]
      content[count] = content[count - 1]
      content[count - 1] = value
      count = count - 1
  return content
if __name__ == "__main__":
  num = input("Input the num:\n").split()
  result = list()
  for i in num:
    result.append(int(i))
  gnome_sort(result)
  print(result)