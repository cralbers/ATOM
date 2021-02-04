def convert(i, j, k):
  '''(int, int, int) -> int

  Reurn an integer from i, j, k where i is the least significant
  digit(ones place), j is the tens place and k is the hundreds place.

  >>> convert(1, 2, 3)
  321

  >>> convert(1, 0, 0)
  1

  '''
  result = (i*1)+(j*10)+(k*100)
  return result
