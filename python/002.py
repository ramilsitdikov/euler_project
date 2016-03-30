first_number = 1
second_number = 2
third_number = first_number + second_number

result_sum = second_number
border = 4000000
while (third_number < border):
  if third_number % 2 == 0:
    result_sum += third_number
  first_number = second_number
  second_number = third_number
  third_number = first_number + second_number

print result_sum
