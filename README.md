# IRKit api interface for python

## What is IRKit?

That is kind of a learning remote control system which has HTTP API interface.

Details is http://getirkit.com/


## install

```bash
$ pip install irkit
```


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
usage: irkit local [-h] [--host] [-k] [-r] [--save signal-name] [-l]
                   [-s signal-info] [-v]

optional arguments:
  -h, --help            show this help message and exit
  --host                show irkit host
  -k, --keys            get a client token.
  -r, --retrieve        retrieve a signal
  --save signal-name    you should appoint a name. save retrieved signal to
                        ~/.config/irkit-py/signal.json with name
  -l, --list            list of stored signals
  -s signal-info, --send signal-info
                        send a signal. that excepted as json response or
                        raw_data or key name of store
  -v, --verbose         put verbose logs
```

### Example

copy and paste style

```bash
## you must send signal to IRKit before
$ irkit local --retrieve
{"freq": 38, "data": [... ...], "format": "raw"}

## copy and paste the json
$ irkit local --send '{"freq": 38, "data": [... ...], "format": "raw"}'
```

store with key

```bash
$ irkit local --retrieve --save toggle-room-light
{"freq": 38, "data": [... ...], "format": "raw"}

$ cat ~/.config/irkit-py/signal.json
{"freq": 38, "data": [... ...], "format": "raw"}

$ irkit local --send movie-room-toggle
```


## as Library

You can also use as api.
Document is now writing... but `main.py` will help you to understand API interfaces.


## Bug report or request or something

GitHub issue is opend ;)

https://github.com/hachibeeDI/IRKit/issues
