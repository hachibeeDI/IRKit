# IRKit api interface for python

## Command Usage

```
usage: irkit [-h] {local,global} ...

IRKit CLI Client for Python. v0.0.1 See also http://getirkit.com/#IRKit-
Device-API

positional arguments:
  {local,global}  sub-command help
    local         api for locals.
    global        api for internets.

optional arguments:
  -h, --help      show this help message and exit

```


```
usage: irkit local [-h] [--host] [--keys] [--retrieve] [--send SEND]

optional arguments:
  -h, --help   show this help message and exit
  --host       show irkit host
  --keys       get a client token.
  --retrieve   retrieve a singnal
  --send SEND  send a signal data or api response
```
