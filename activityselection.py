def pair_compare(A, B):
  return A[1] - B[1]
  
def activityselect(L):
  result = []
  temp = sorted(L, cmp = pair_compare)
  result.append(temp[0])
  last = temp[0]
  for x in temp:
    if (last[1] <= x[0]):
      result.append(x)
      last = x
  return result
