def quick_sort(content):
  if(len(content) <= 1):
    return content
  mid = content.pop()
  less = list()
  great = list()
  for item in content:
    if(item < mid):
      less.append(item)
    else:
      great.append(item)
  return quick_sort(less) + [mid] + quick_sort(great)

def main():
  num = input("Input the num:\n").split()
  result = list()
  for i in num:
    result.append(int(i))
  quick_sort(result)

if __name__ == "__main__":
  main()