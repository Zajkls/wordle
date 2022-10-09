num_list = [1,2,3,4,5]

def binary_search(target, xlist, low, high):
  mid = (low + high) // 2
  if xlist[mid] == target:
    return xlist[mid]
  elif xlist[mid] < target:
    return binary_search(target, xlist, mid + 1, high)
  elif xlist[mid] > target:
    return binary_search(target, xlist, low, mid - 1)

print(binary_search(2, num_list, 0, 4))


