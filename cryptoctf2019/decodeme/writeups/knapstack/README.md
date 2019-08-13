# DecodeMe

### knapstack

We are provided the following text

```
D: mb xwhvxw mlnX 4X6AhPLAR4eupSRJ6FLt8AgE6JsLdBRxq57L8IeMyBRHp6IGsmgFIB5E :ztey xam lb lbaH
```

It looks like the `D:` might be an emoji `:D` which is reversed. By this intuition, I reverse the whole string

```python
>>> x="""D: mb xwhvxw mlnX 4X6AhPLAR4eupSRJ6FLt8AgE6JsLdBRxq57L8IeMyBRHp6IGsmgFIB5E :ztey xam lb lbaH"""
>>> x[::-1]
'Habl bl max yetz: E5BIFgmsGI6pHRByMeI8L75qxRBdLsJ6EgA8tLF6JRSpue4RALPhA6X4 Xnlm wxvhwx bm :D'
```

After ROT-7 on both numbers-alphabets, we get the following

```
Ohis is the flag: L2IPMntzNP3wOYIfTlP5S42xeYIkSzQ3LnH5aSM3QYZwbl1YHSWoH3E1 Eust decode it :K
```

There seems to be some issue with the uppercase character. I wrote a script to fix that, running it would give

```
$ python solve.py

This is the flag: Q2NURntzSU3wTDNfYlU5X42xeDNkXzV3QnM5aXR3VDEwbl1DMXBoM3J1 Just decode it :P
```

But, decoding it gives garbage again. So, I took first couple of bytes and tried to decode

```
Q2NURntz
CcTF{s
```

The flag format is `CCTF{...}` , Hence, I shifted a byte.

```
Q0NURntz
CCTF{s
```

Interesting, Hence the number are shifted different times compared to the string. 

After shifting those, I get

```
This is the flag: Q0NURntzSU1wTDNfYlU3X20xeDNkXzV1QnM3aXR1VDEwbl9DMXBoM1J9 Just decode it :P
```

Decoding gives

##### Flag: CCTF{sIMpL3_bU7_m1x3d_5uBs7ituT10n_C1ph3R}