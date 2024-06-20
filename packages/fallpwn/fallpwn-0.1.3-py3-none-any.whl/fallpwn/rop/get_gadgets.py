from os import popen
from pwn import *

class GadgetsDict(dict):
    def __init__(self, libc, ver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.libc = libc
        self.ver = ver
    
    def __getitem__(self, key):
        if key not in self:
            self[key] = self._handle_missing_key(key)
        return super().__getitem__(key)
    
    def _handle_missing_key(self, key):
        gadgets = {
            'pop_rdi': b'_\xc3',
            'pop_rsi': b'^\xc3',
            'pop_rdx': b'Z\xc3',
            'pop_rax': b'X\xc3',
            'pop_r10': b'AZ\xc3',
            'pop_r8': b'AX\xc3',
            'pop_r9': b'AY\xc3',
            'pop_rcx': b'Y\xc3',
            'syscall': b'\x0f\x05\xc3',
            'leave_ret': b'\xc9\xc3',
            'ret': b'\xc3',
            '/bin/sh': b'/bin/sh\x00',
            '/bin/sh\x00': b'/bin/sh\x00',
            'sh': b'sh\x00',
            'sh\x00': b'sh\x00'
        }

        if key == 'pop_rdx_2':
            try:
                return next(self.libc.search(b'Z[\xc3', executable=True))
            except StopIteration:
                try:
                    return next(self.libc.search(b'ZA\\\xc3', executable=True))
                except StopIteration:
                    print(f'\033[31m[x] Gadgets ({key} ; ret) NOT FOUND. [X]\033[0m')
                    exit(0)

        if key == 'setcontext' or key == 'magic_gadget':
            if '2.27' in self.ver or '2.26' in self.ver or '2.25' in self.ver or '2.24' in self.ver or '2.23' in self.ver:
                try:
                    if key == 'setcontext':
                        return next(self.libc.search(b'H\x8b\xa7\xa0\x00\x00\x00H\x8b\x9f\x80\x00\x00\x00', executable=True))
                except StopIteration:
                    print('\033[31m[x] Gadgets (setcontext) NOT FOUND. [X]\033[0m')
                    exit(0)
            elif '2.29' in self.ver:
                try:
                    if key == 'setcontext':
                        return next(self.libc.search(b'H\x8b\xa2\xa0\x00\x00\x00H\x8b\x9a\x80\x00\x00\x00', executable=True))
                    elif key == 'magic_gadget':
                        return next(self.libc.search(b'H\x8bW\x08H\x8b\x07H\x89\xd7\xff\xe0', executable=True))
                except StopIteration:
                    print(f'\033[31m[x] Gadgets ({key}) NOT FOUND. [X]\033[0m')
                    exit(0)
            else:
                try:
                    if key == 'setcontext':
                        return next(self.libc.search(b'H\x8b\xa2\xa0\x00\x00\x00H\x8b\x9a\x80\x00\x00\x00', executable=True))
                    elif key == 'magic_gadget':
                        return next(self.libc.search(b'H\x8bW\x08H\x89\x04$\xffR ', executable=True))
                except StopIteration:
                    print(f'\033[31m[x] Gadgets ({key}) NOT FOUND. [X]\033[0m')
                    exit(0)

        if key in gadgets:
            try:
                if '/bin/sh' in key:
                    return next(self.libc.search(gadgets[key]))
                return next(self.libc.search(gadgets[key], executable=True))
            except StopIteration:
                if key == 'pop_rdx':
                    print('\033[33m[!] You may try to access pop_rdx_2 instead. [!]\033[0m')
                print(f'\033[31m[x] Gadgets ({key} ) NOT FOUND. [X]\033[0m')
                exit(0)
        else:
            print(f'\033[31m[x] Unsupported gadget key: {key}. [X]\033[0m')
            exit(0)

class GadgetsFinder:
    def __init__(self, libc:ELF):
        '''
        传入一个参数，即libc对象
        '''
        self.libc = libc
        self.libcpath = libc.path
        self.ver = self.__get_ver(self.libcpath)
        self._gadgets = GadgetsDict(self.libc, self.ver)
    
    def __get_ver(self, filename):
        data = popen(f'strings "{filename}" | grep "GNU C Library"').read()
        try:
            ver = re.search(r'GLIBC (.*?)\)', data).group(1)
        except:
            print('[x] Cannot find GLIBC version! [x]')
            exit(0)
        return ver
    
    def get_gadgets(self) -> GadgetsDict:
        '''
        返回一个gadgets字典，使用如下方式调用：
        gadgets['pop_rdi']
        gadgets['leave_ret']
        ...
        '''
        return self._gadgets