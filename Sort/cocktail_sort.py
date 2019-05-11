def cocktail_sort(content):
  left = 0
  right = len(content) - 1
  while(left < right):
    for i in range(left, right):
      if(content[i] > content[i + 1]):
        value = content[i + 1]
        content[i + 1] = content[i]
        content[i] = value
    right = right - 1
    for i in range(right, left, -1):
      if(content[i] < content[i - 1]):
        value = content[i]
        content[i] = content[i - 1]
        content[i - 1] = value
    left = left + 1
  return content
def main():
  num = input("Input the num:\n").split()
  result = list()
  for i in num:
    result.append(int(i))
  cocktail_sort(result)
if __name__ == "__main__":
  main()
