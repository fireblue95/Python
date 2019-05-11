def bubble_sort(content):
  length = len(content)
  for i in range(length - 1):
    for j in range(length - 1 - i):
      if(content[j + 1] < content[j]):
        value = content[j + 1]
        content[j + 1] = content[j]
        content[j] = value
  return content
def main():
  num = input("Input the num:\n").split()
  result = list()
  for i in num:
    result.append(int(i))
  bubble_sort(result)
if __name__ == "__main__":
  main()
