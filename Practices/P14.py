def removeDups(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

a = [1,2,3,4,3,2,1]