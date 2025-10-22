# COMP1850 Worksheet 1.2

You will need to implement all three of these programs and upload them
to Gradescope for grading.

## `task_a.py`

In a file named `task_a.py`, write a program that

* Asks users to enter an integer grade in the range 0 to 100

* Converts that grade into a result of Pass, Fail or Distinction, where

  - Fail = 0-39
  - Pass = 40-69
  - Distinction = 70-100

* Prints out the numeric grade and the result on a single line, with
  *exactly* same format as the examples below:

      82 is a Distinction
      57 is a Pass
      36 is a Fail

If the user enters something that isn't a number, or they enter an integer
value outside the required range, the program should immediately exit, after
first displaying this exact error message on the standard error channel:

    Error: Grade must be an integer between 0 and 100

Use the `exit()` function from Python's `sys` module to achieve this. Here
is an example of how you import this module and use the `exit()` function:

```python
import sys

sys.exit("Error!")
```

## `task_b.py`

In online publications, it is common for the URL of an article to end in a
**slug**: a short identifier for the article, which is often based on the
article's title.

An article's title is transformed into a slug via operations such as making
all letters lowercase, removing short words like 'a', and replacing spaces
with hyphens. A slug may also be truncated so that it is substantially
shorter than the title.

For example, the tech news site *Ars Technica* recently [published an
article][ars] entitled

>*Hollow Knight: Silksong* is breaking Steam, Nintendo's eShop

The slug for this article is

    hollow-knight-silksong-is-breaking-steam

In a file named `task_b.py`, write a program that transforms a title entered
by the user into a slug suitable for online publishing.

Your slug must

* Not contain any uppercase letters
* Not contain the words "a" or "the" at the start or between other words
* Use hyphens in place of spaces
* Have a maximum length of 25 characters

Use a variable named `slug` to represent the final value for the slug,
after applying the transformations listed above.

Use *exactly* the following code to display the slug. **This should be the
only print statement in your program.**

```python
print(f"Slug = {slug}")
```

### Hints

* Investigate Python's [string methods][str]. You will find that most of the
  transformations can be implemented fairly simply, just by using
  the appropriate method.

* Investigate [slicing of strings][slice]. You'll find this technique useful,
  e.g., for limiting the length of the slug.

* Think carefully about how to remove the words "a" and "the". You should
  not be remove these character sequences if they are part of another word!

## `task_c.py`

In a file named `task_c.py`, write a program that

* Obtains a list of `float` values from the user
* Finds the minimum, maximum, mean and median of these values
* Prints these statistics

For example, given the list

    [4.5, 3.0, 1.2, 7.0, 6.3]

Your program should print this as its output:

    Minimum = 1.2
    Maximum = 7.0
    Mean    = 4.4
    Median  = 4.5

If no numbers were entered, the program should terminate with a non-zero
exit status and display the following error on the standard error channel.

    Error: no numbers provided

Use the `sys.exit()` function to do this, as you did in `task_a.py`.

### Notes

* **Read the numbers from the user using the function that we have provided
  for this purpose.** The function is defined in the file `util.py`.

  You can use it like this:

  ```python
  from util import read_numbers

  numbers = read_numbers()
  ```

* Your program must NOT use any Python modules other than the `sys` and
  `util` modules mentioned above.

* Your program should perform its calculations without using loops.

### Hints

* Minimum, maximum and mean can be determined in a fairly straightforward
  manner, using four of Python's [built-in functions][funcs].

* The **median** is the 'middle' number, after arranging numbers in
  ascending order. You can use [one of Python's list methods][list] to help
  you arrange the numbers in this way.

  Note that there won't be a single middle number when the list size is even.
  Your code will need to handle this appropriately. See the [definition of
  median][med] for further information on this.


[ars]: https://arstechnica.com/gaming/2025/09/hollow-knight-silksong-is-breaking-steam/
[str]: https://docs.python.org/3/library/stdtypes.html#string-methods
[slice]: https://runestone.academy/ns/books/published/thinkcspy/Strings/TheSliceOperator.html
[funcs]: https://docs.python.org/3/library/functions.html
[list]: https://docs.python.org/3/library/stdtypes.html#lists
[med]: https://en.wikipedia.org/wiki/Median#Finite_set_of_numbers
