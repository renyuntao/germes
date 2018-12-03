## What is germes

**germes** is a SQLite file with special table struct.

## SYNOPSIS

**germesctl** - Create germes or delete info from germes use YAML config file  

**dump** - Dump germes in YAML format

## Config File Example

```yaml
demo:           # DB name
  info:         # Table name
    user: Tom   # item in table
  shbt@1:
    - host1.shbt.example.com
  zzzc@1:
    - host2.zzzc.example.com
  alias:
    monitor.example.com: host2.zzzc.example.com
```

## Example

```bash
$ ./germesctl -C config -c
====== zzzc@1 ======
Success.
====== shbt@1 ======
Success.
====== info ======
Success.
====== alias ======
Success.

$ ./dump demo
---
demo:
  alias:
    monitor.example.com: host2.zzzc.example.com
  info:
    user: Tom
  shbt@1:
    host1.shbt.example.com: '1'
  zzzc@1:
    host2.zzzc.example.com: '1'

$ ./dump demo -t 'shbt@1'
---
demo:
  shbt@1:
    host1.shbt.example.com: '1'

$ ./dump demo -t 'shbt@1' -k
=== shbt@1 ===
host1.shbt.example.com

$ ./dump demo -t 'shbt@1' -r '1~10'
---
demo:
  shbt@1:
    host1.shbt.example.com: '1'
```
