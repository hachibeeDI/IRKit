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
usage: irkit [-h] {local,internet} ...

IRKit CLI Client for Python. v0.0.1 See also http://getirkit.com/#IRKit-
Device-API

positional arguments:
  {local,internet}  sub-command help
    local           api for locals.
    internet        api for internets.

optional arguments:
  -h, --help        show this help message and exit

```

Local API:

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

Internet API:

```
usage: irkit internet [-h] [-r] [-s signal-info] [--save signal-name]
                      [-c CLIENT_KEY] [-d DEVICE_ID] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -r, --retrieve        retrieve a signal
  -s signal-info, --send signal-info
                        send a signal. that excepted as json response or
                        raw_data or key name of store
  --save signal-name    you should appoint a name. save retrieved signal to
                        ~/.config/irkit-py/signal.json with name
  -c CLIENT_KEY, --client-key CLIENT_KEY
                        client key
  -d DEVICE_ID, --device-id DEVICE_ID
                        device id
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


#### Internet API

Then you want to send internet API, you need to appoint device_id or client_key or both.

```bash
## retrieve needs client key
$ irkit internet --retrieve --client-key YOUR_CLIENT_KEY

## send needs client key and device id
$ irkit internet --send '{"freq": 38, "data": [... ...], "format": "raw"}' \
  -c 0A9B3FFB240444A2BA70A9835BFE4F89 \
  --device-id 6B08F5EA443E4983864908B4AFF897AA
```

This tool haven't follow client-key and device-key smart integration (it can only get {*see --key option*}).
It'll be implemented next version (and I welcome to your contlibute!).


## as Library

You can also use as api.
Document is now writing... but `main.py` will help you to understand API interfaces.


## Support Versions

- 2.7

- 3.6 (might unstable)


## Bug report or request or something

GitHub issue is opend ;)

https://github.com/hachibeeDI/IRKit/issues
