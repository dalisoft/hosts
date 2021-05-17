# Hosts file

## Check

Check at [here](https://checkadblock.ru)

## Copy your current hosts

> Your current host-file should be without any of ad-blocking hosts
> see `defaults.txt` example attached in repo

- `cp /etc/hosts defaults.txt`

## Build hosts

`python build.py`

## Link to system

`sudo python link.py && sudo chmod 0644 /etc/hosts`

## Reload hosts

### macOS

`sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`
