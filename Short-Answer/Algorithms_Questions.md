# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
"""
a is equal to zero, and in order to enter the loop, the value of n must be negative 
and will continue to loop until a reaches 0. 
A larger negative number will increase the runtime,
(n * n * n) has a runtime complexity O(n^3)

"""

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
"""
to enter the for loop, n needs to be a positive number. Will loop through the 
index n amount of times. While j is less than n, j will be multiplied by 2, and have an O(n^2)
runtime complexity because the value of j will increase exponentially when multiplied more than
one time. The sum will increase each time the while loop is entered, which is O(1) runtime complexity. 

"""

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
"""
This is a recursive call, the base case is that there are zero bunnies, and zero ears. For each bunny,
return two ears and make one recursive call. If the input increases the runtime space will grow at the 
same rate because there is only one recursive call. Runtime complexity linear O(n).

"""

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


"""
Whether or not an egg breaks is divided by f, because below f it survives and above f it breaks

We need to start from the first floor and test if an egg breaks or survives. Once an egg breaks, we have found the value of f, and the higher
floors aren't as important because all eggs will break above that point.

Because this solution would only have one recursive call, the runtime complexity would be O(n)

#n should be the first floor
def egg_drop(n):  
  #base case
  if n == 0:
    return 0
  elif:
    if drop == break
    f = True
  else:
    f = False
    #recursive call increment n to move up a floor
    n +=1 
    return egg_drop(n)


"""