# Largnumber_array
### creating largest combination of a given array numbers
to achieve this goal we have come up whit the idea of combining two numbers and comparing their combination with each other.

**for example:**
we take the aaray **[44,50 ,6 ,5 ,9]** and combine two numbers 44 and 50 the outcome is 4450 and 5044 then we compare these two and because 5044 is a bigger number then 50 should
come first we swap the numbers and then move on to next one now our numbers are 50 and 6 so we have 506 and 650 so again 6 should be first this continues until all our numbers are sorted
in desired order then we simlpy join all of them together to get the largest possible number out of the given number.
### test
to test this algorithm we have prepared the **test.py** file which uses unittest package to run the testcases to use this file just put your testcases in the **self.test_cases** list
and run the file.
