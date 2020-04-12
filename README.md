# Etc files

## Hosts

### Reload

Try first variant, if it's doesn't work, try other

- `sudo dscacheutil -flushcache`
- `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`

### Anti-duplication

```bash
uniq hosts > hosts.temp
mv hosts.temp hosts
rm -rf hosts.temp
```

### Link

`sudo ln -f hosts /etc/hosts`
