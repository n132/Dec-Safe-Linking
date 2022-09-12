
# Dec-Safe-Linking

There are several ways to **Recover** Safe linking protected value/pointer.


In practicing, there are mainly at least three ways to fully recover the encoded pointer.

> knowing the address and the stored pointer are on the same page
knowing the offset between the address and the stored pointer
knowing the address's and the pointer's offset to the heap base


# TL;DR

According to these three ways, I think
these three sets have the following relation and the solver of set2 is the strongest cuz it can solve cases for all three sets.

Relation:
- Set1 and set3 have common parts and their own unique parts
- Set2 contains the union of set1 and set3


# Explanation

First, let's define these three sets clearly:
| Set	| Condition 0	| Condition 1	| Condition 2|
|--|--|--|--|
|Set1	|Encoded Leaked Data	|PAGE_OFF == 0|-|
|Set2	|Encoded Leaked Data	|PAGE_OFF|-|
|Set3	|Encoded Leaked Data	|Address's OFFSET to HEAPBASE| Value's OFFSET to HEAPBASE


It's easy to find:

- Set1 is a subset of set2
- All cases in set3 are in set2
- Cases in set1 may not be in set3, and vice versa


Assume there is a function solver(leaked, Pageoff) which could solve cases for set2. It can also solve cases in set1 and set3.

- For set1, solver(leaked,0)
- For set3, solver(leaked,(v1-v2)>>12)


# Solvers

- General Decoder
  - [z3 Decoder][3]
  - [math Decoder][4]
- limitted [Decoder][2] (storer and the value are at the same page, but this is the most useful decoder in real life)

# Reference

I wrote the classical decoder according to this [file][1]


[1]: https://github.com/shellphish/how2heap/blob/master/glibc_2.35/decrypt_safe_linking.c
[2]: ./dec_safe_linking.py
[3]: ./z3_general_decoder.py
[4]: ./ugly_general_decoder.py
