# Etc files

## Hosts

### Anti-duplication

```bash
uniq hosts > hosts.temp
mv hosts.temp hosts
rm -rf hosts.temp
```

### Link

`sudo ln -f hosts /etc/hosts`
