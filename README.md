# EPAI Session 7 Assignment by Sachin Dangayach

This assignment is based on the concepts of "# First Class Functions Part II". We have  used combination of map, reduce, filter, zip, lambda functions and partial functions. session7.py contains the code for assignment and test_session7.py file contains the various test cases.

# Below are test cases to test the assignment solutions in test_session7.py file.

## Check for coding standards-

## 1. test_readme_exists :
Test for readme exists

## 2. test_readme_contents :
Test for readme contents are more than 500 words

## 3. test_readme_proper_description :
Test for all important functions/class described well in your README.md file

## 4. test_readme_file_for_formatting :
Test for readme formatting

## 5. test_indentations :
Test for source code formatting. No tabs but four spaces are used for indentation

## 6. test_function_name_had_cap_letters :
Test for no function is with capitals in source code

# Test cases for assignments

## 7. test_fibonacci_by_reduce:
Test function using only list filter lambda that can take a list of number and return a list removing the  numbers which are not Fibonacci numbers. We prepare the fibonacci numbers list first and then compare the new numbers to be tested with it.

## 8. test_odd_even_sum :
Test add 2 iterables a and b such that a is even and b is odd using list comprehension (and zip/lambda/etc if required)

## 9. test_strip_vowel :
Test function to strips every vowel from a string provided. For example (tsai>>t s)

## 10. test_relu :
Test function acts like a ReLU function for a 1D array

## 11. test_sigmoid :
Test function acts like a sigmoid function for a 1D array

## 12. test_cyclic_shift_by_5 :
Test function which take a small character string and shifts all characters by 5 (handle boundary conditions) for example - tsai>>yxfn

## 13. test_swear_word :
Test function to check whether the given text comment contains any swear words, if yes call it as bad comment else good comment

## 14. test_add_only_even :
Test function to check the expression adds only even numbers in a list

## 15. test_biggest_char_in_string :
Test function to find the biggest character in a string (printable ascii characters). We use the ord() function to find the ASCII value of the characters and use it to compare the letters of string

## 16. test_add_every_third :
Test function to add every 3rd number in a list and return the sum. We used list comprehension to generate the list of every third elements from the given list and pass it to the reduce function

## 17. test_generate_num_plate :
Test expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999

## 18. test_generate_num_plate_partial_func:
Test partial function that generates 15 random KADDAADDDD number plates, where state initials are provided by user like 'DL' or 'KA' or 'TN', D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999. Here we

## 19. test_partial_func_locked_param_check:
Test test_partial_func_locked_param_check function for not allowing multiple argument to be passed which are locked while defining it as while defining partial function we already pass the start and end for the range of last four digits. If user attempts to pass these again, it should result in error.
