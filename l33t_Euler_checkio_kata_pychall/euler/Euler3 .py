
don’t make a list, rather, multiply each success and store it in a new value until that product because the big fuckin number.

-----------Conclusion

things i did for the first time
installed and improrted numpy in a flash, no confusion, just did it

used all()
had good ‘number sense’
solved it in probably x<1hour


--------Code

import numpy as np

i=1
z=i
while i<10000000:
  if 600851475143%i==0: #looking for factors
     print(i,'before prime filtration')
     if all(i%(np.arange(2,i/2))) !=0: #checking the primage' of factors (if all of them aren’t modulating, then they aren’t factors, if ALLthen prime
        print(i, 'after prime filtration')
  i+=1

q=1
for i in np.arange(1,104442):
  if 104441%i==0:
     print(i)


Overall did this one pretty quick. at first i was thinking lists, i was thinking lamda for the modulus, for some reason, and i fixed things. plus i imported a tool and bambam easy peasy used command line...wht i did last year stuck.


-------------other human’s solutions
this persons solution is pretty. i like how he counts only odds (evens being inherently non-prime)

from math import sqrt

primes = set([2])
value = 3
number = 317584931803
while value < sqrt(number):
    isPrime = True
    for k in primes:
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        primes.add(value)
        if number % value == 0:
            print value
            number /= value
print number


----------------Notes/Overview

1This can be improved upon by the following key realisation: every number n can at most have one prime factor greater than sqrt(n) .
so take sqrt(n) as the limit...try next time.

2 in some languages it would have been necessary to use long/int64 since 600...>(2^31)-1
