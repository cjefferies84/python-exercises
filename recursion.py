# good comment about recursion by Sarah:  my understanding is that the pow() inside each pow()
# is waiting for a return value. once we hit the last pow() return 1,
#  then each pending pow() get its return value and terminates. I think the key idea is that
# once pow() gets a return value, it terminates, and becomes a value


def sum_list(l):
    # this is our base case
    if len(l) <= 0:
        # by returning 0 we will not effect the result we will get the same number because we are adding 0
        return 0

    current_val = l.pop()
    current_val += current_val
    return current_val

sum_list([1, 2, 3, 4, 5])

# this stops when you reach the global scope of current_value 5