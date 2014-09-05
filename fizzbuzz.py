# Print the numbers from 1 to 100, but replace factors of 3 with Fizz, 5 with Buzz

import sys

start_no = 1
end_no = 100
first_find = 3
second_find = 5
first_replace = 'Fizz'
second_replace = 'Buzz'

for count in range(start_no , end_no + 1):
	if (count % (first_find * second_find)) == 0:
		print first_replace, second_replace		
	elif (count % first_find) == 0:
		print first_replace
	elif (count % second_find) == 0:
		print second_replace
	else:
		print(count)

