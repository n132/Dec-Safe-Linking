# Dec-Safe-Linking

There are several ways to Decode Safe linking protected value.
- General Decoder
  - [z3 Decoder][3]
  - [math Decoder][4]
- limitted [Decoder][2] (storer and the value are at the same page, but this is the most useful decoder in real life)

# reference

I wrote the classical decoder according to this [file][1]


[1]: https://github.com/shellphish/how2heap/blob/master/glibc_2.35/decrypt_safe_linking.c
[2]: ./dec_safe_linking.py
[3]: ./z3_general_decoder.py
[4]: ./ugly_general_decoder.py
