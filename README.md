# Python pkg for HazeDumper
## Install
```pip install hazedumper```

---
## Example
```python
import pymem
import pymem.process
from hazedumper import \
    dwLocalPlayer, m_iHealth


def main():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    player = pm.read_int(client + dwLocalPlayer) #get local player
    health = pm.read_int(player + m_iHealth) #get health

    print(health) #output: 100


if __name__ == '__main__':
    main()
```

---
`by @cxldxice with ❤`