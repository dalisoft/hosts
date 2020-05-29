# Hosts file

## Check

Check at [here](https://checkadblock.ru)

## Copy your current hosts

> Your current host-file should be without any of ad-blocking hosts
> see `hosts.orig` example attached in repo

- `cp /etc/hosts hosts.orig`

## Build hosts

`sh build.sh`

## Reload hosts

### macOS

`sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`


## Link to system

> There hard-linked because of most of time soft-link does not work

`sudo ln -f hosts /etc/hosts`
