# Week 4, Session 1: Task 4

# You are given four functions. Inspect the function definition and pay
# special attention to the parameters.

# Your task is to inspect the code, run the program and observe the output
# by uncomment one line after another. Is the output as you have expected?
# Identify why some do not work.


def standard_arg(arg1, arg2):
    print(arg1, arg2)


def position_only_arg(arg1, arg2, arg3, /):
    print(arg1, arg2, arg3)


def keyword_only_arg(*, arg1, arg2):
    print(arg1, arg2)


def mix_both_args(pos_only_arg, /, std_arg, *, key_only_arg):
    print(pos_only_arg, std_arg, key_only_arg)


# Check if the functions work with different arguments.
# Uncomment each line one by one to find out. If it
# does not work, why?

standard_arg(5, 6)
# standard_arg(arg1=7, arg2=9)
# position_only_arg("hi", "there", "here")
# position_only_arg(arg2=6, arg1=3, arg3=9)
# keyword_only_arg(8, 9)
# keyword_only_arg(arg1=10, arg2=8)
# mix_both_args(9, 1, 1)
# mix_both_args(9, 1 , key_only_arg=1)
# mix_both_args(pos_only_arg=9, std_arg=1, key_only_arg=1)
