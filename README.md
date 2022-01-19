## ipy2d

A small library to convert IP addresses to integers

### Usage

```py
from ipy2d import fun

print(fun.from_4("127.0.0.1")) # -> 2130706433
print(fun.to_4(134744072)) # -> 8.8.8.8

print(fun.from_6("::1")) # -> 1
print(fun.to_6(1051570404137199630024704)) # -> 0000:0000:0000:dead:beef:0000:0000:0000
```

#### Development

* Install dependencies from `setup.py` `python3 setup.py install`
* run *__main__.py* `python3 -m ipy2d`

#### Test

If `pytest` is installed, you can run `pytest test/*`

#### Deploy

* create *dist* `python3 setup.py sdist bdist_wheel`
* check *dist* `twine check dist/*`
* publish *dist* `twine upload dist/* ` 
