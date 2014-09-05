# Print the numbers from 1 to 100, but replace factors of 3 with Fizz, 5 with Buzz, and factors of both with FizzBuzz

import sys

# Beginning and ending of the range of number to do this with. Becuase this is such a useful program, you'll want to repurpose it!
start_no = 1
end_no = 100

# What numbers get replaced. Again, you'll probably find this indespensible.
first_find = 3
second_find = 5

#What to replace them with. [Insert more snark]
first_replace = 'Fizz'
second_replace = 'Buzz'


for count in range(start_no , end_no + 1):               # "for" will only go up to the the last number minus one, hence the "+ 1"
	if (count % (first_find * second_find)) == 0:    # Check for both first, otherwise the other two will prevent it from ever getting hit
		print first_replace, second_replace            		
	elif (count % first_find) == 0:                  # Then look for the first target 
		print first_replace                      # and print the replacement instead of the number
	elif (count % second_find) == 0:                 # IBID
		print second_replace
	else:
		print(count)                             # If none of the replacements hit, just print a boring old number. Yawn.

