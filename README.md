# TL;DR

There is a general way to **Recover** Safe linking protected value/pointer as long as we know the page offset between the storer and the pointer.


- If you tolerate a tiny failure rate(<0.01), check this [solver][6]. It's a general solver. This solver only takes the leaked data and the page_off as inputs.
- You can find a general decoder [here][3], which needs an additional value to reach a 100% success rate.



Also, I implement the solver with math rather than z3. Check the solver [here][4]

Moreover, there is a limited but super useful [Solver][2]. I implemented this according to [how2heap][1].

# Dec-Safe-Linking

There are several ways to **Recover** Safe linking protected value/pointer.


In practice, there are mainly at least three ways to fully recover the encoded pointer.

> knowing the address and the stored pointer are on the same page
> 
> knowing the offset between the address and the stored pointer
> 
> knowing the address's and the pointer's offset to the heap base
> 
> (This summary comes from Kyle-Kyle)

According to these three ways, I think
these three sets have the following relation and the solver of set2 is the strongest cuz it can solve cases for all three sets.

Relation:
- Set1 and set3 have common parts and their own unique parts
- Set2 contains the union of set1 and set3


# Explanation

First, let's define these three sets clearly:
| Set | Condition 0 | Condition 1 | Condition 2|
|--|--|--|--|
|Set1 |Encoded Leaked Data  |PAGE_OFF == 0|-|
|Set2 |Encoded Leaked Data  |PAGE_OFF|-|
|Set3 |Encoded Leaked Data  |Address's OFFSET to HEAPBASE| Value's OFFSET to HEAPBASE


It's easy to find:

- Set1 is a subset of set2
- All cases in set3 are in set2
- Cases in set1 may not be in set3, and vice versa


Assume there is a function solver(leaked, Pageoff) which could solve cases for set2. It can also solve cases in set1 and set3.

- For set1, solver(leaked,0)
- For set3, solver(leaked,(v1-v2)>>12)


# Reference

- How2Heap's [Solver][1]
- [Safe-linking][5]

# Thanks

- [Kyle][7]
- [CSAW][8]

[1]: https://github.com/shellphish/how2heap/blob/master/glibc_2.35/decrypt_safe_linking.c
[2]: ./sol.py
[3]: ./z3_gen_sol.py
[4]: ./gen_sol.py
[5]: https://research.checkpoint.com/2020/safe-linking-eliminating-a-20-year-old-malloc-exploit-primitive/
[6]: ./0racle/
[7]: https://github.com/Kyle-Kyle
[8]: https://www.csaw.io/