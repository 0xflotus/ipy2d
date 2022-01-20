## ipy2d

[![ipy2d on pypi](https://badgen.net/pypi/v/ipy2d)](https://pypi.org/project/ipy2d/)

A small library to convert IP addresses to integers

### Usage

```py
from ipy2d import convert

print(convert.from_4("127.0.0.1")) # -> 2130706433
print(convert.to_4(134744072)) # -> 8.8.8.8

print(convert.from_6("::1")) # -> 1
print(convert.to_6(1051570404137199630024704)) # -> 0000:0000:0000:dead:beef:0000:0000:0000
print(convert.to_6(1051570404137199630024704, compressed=True)) # -> ::dead:beef:0:0:0
```
