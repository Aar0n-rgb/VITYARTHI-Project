def mean_of_digits(n):
  """Returns the average of all digits in a number."""
  s = str(abs(n))
  digits = [int(d) for d in s]
  return sum(digits) / len(digits)
n=896
print(mean_of_digits(n))