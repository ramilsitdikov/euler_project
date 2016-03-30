import math
def is_prime(number):
  i = 2
  number_sqrt = math.sqrt(number)
  while(i < number_sqrt):
    if number % i == 0:
      return False
    i += 1
  return True

huge_num = 600851475143
huge_num_sqrt = math.sqrt(huge_num)
pretendent = 2
suited_divider = pretendent
while(pretendent < huge_num_sqrt):
  if huge_num % pretendent == 0 and is_prime(pretendent):
    suited_divider = pretendent
  pretendent += 1
print suited_divider

