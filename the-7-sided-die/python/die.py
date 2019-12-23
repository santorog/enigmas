#!/usr/bin/python3

import random as rd
import time as t

class the_6_sided_die:

    def roll():
        return rd.randint(1,6)

class the_7_sided_die:

    def roll():
        return rd.randint(1,7)

    def roll_with_partition():
        i,j=the_6_sided_die.roll(), the_6_sided_die.roll()
        if (j == 6):
            if (i == 6):
                return the_7_sided_die.roll_with_partition()
            else:
                return 7
        else:
            return i

    def roll_with_formula():
        i,j=the_6_sided_die.roll(), the_6_sided_die.roll()
        if (i == 6 & j == 6):
            return the_7_sided_die.roll_with_formula()
        else:
            return (((i-1)*6+j)%7+1)

class benchmark:

    def run(f):
        r={}
        start = t.time()
        for i in range(int(1E6)):
            tmp=f()
            r[tmp]=r.get(tmp,0)+1
        end = t.time()

        print("Rolling with",f.__name__,"took",round(end-start,2), "seconds. Distribution is :", sep=' ')
        for elt in r.items():
            print(elt)

benchmark.run(the_7_sided_die.roll)
benchmark.run(the_7_sided_die.roll_with_partition)
benchmark.run(the_7_sided_die.roll_with_formula)
