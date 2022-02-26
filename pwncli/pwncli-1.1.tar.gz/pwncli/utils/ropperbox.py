#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    : ropperbox.py
@Time    : 2021/11/23 12:33:55
@Author  : Roderick Chan
@Email   : ch22166@163.com
@Desc    : Use ropper api from https://github.com/sashs/Ropper
'''

from ropper import RopperService, RopperError, Gadget
from enum import Enum, unique
from pwncli.utils.misc import log_ex
import os
from typing import List, Union

__all__ = ['RopperOptionType', 'RopperArchType', 'RopperBox']

@unique
class RopperOptionType(Enum):
    rop = 'rop'
    jop = "jop"
    sys = 'sys'
    all = 'all'


@unique
class RopperArchType(Enum):
    x86 = 'x86'
    x86_64 = 'x86_64'
    arm = 'ARM'
    armbe = 'ARMBE'
    armthumb = 'ARMTHUMB'
    arm64 = 'ARM64'
    mips = 'MIPS'
    mipsbe = 'MIPSBE'
    mips64 = 'MIPS64'
    mips64be = 'MIPS64BE'
    ppc = 'PPC'
    ppc64 = 'PPC64'
    sparc64 = 'SPARC64'


class RopperBox:
    def __init__(self, *, badbytes: str='', show_all: bool=False, 
                inst_count: int=6, op_type: RopperOptionType=RopperOptionType.all, detailed: bool=False, debug=False):
        self._rs = RopperService(options={
            'color': False,
            'badbytes': badbytes,
            'all': show_all,
            'inst_count': inst_count, 
            'type': op_type.value,
            'detailed': detailed
            })
        self._all_cache = {"string":{}, "gadget": {}, "opcode": {}}
        self._search_func = {"string": self._rs.searchString, "gadget": self._rs.searchdict, "opcode": self._rs.searchOpcode}
        self._debug = debug


    def _log(self, msg):
        if self._debug:
            log_ex(msg)


    def update_option(self, **kwargs):
        for k, v in kwargs.items():
            self._rs.options[k] = v


    def set_debug(self, val: bool):
        self._debug = val


    def add_file(self, name:str, filepath:str, arch:RopperArchType):
        if not os.path.exists(filepath):
            raise RopperError("filepath error! %s doesn't exist!" % filepath)
        self._rs.addFile(name, open(filepath, 'rb').read(), arch.value, False)
        self._rs.loadGadgetsFor(name)
        self._log("Load gadgets from %s success!" % filepath)
        for k in self._all_cache:
            self._all_cache[k][name] = {}


    def remove_file(self, name: str=None):
        if name is None:
            for f in self._rs.files:
                self._rs.removeFile(f.name)
                self._log("remove file: %s success!" % f.name)
        else:
            self._rs.removeFile(name)
            self._log("remove file: %s success!" % name)
        
    
    def get_allgadgets(self, name: str=None) -> List[Gadget]:
        if not name and len(self._rs.files) == 1:
            name = self._rs.files[0].name
        
        return self._rs.getFileFor(name).gadgets

    def print_gadgets(self, name: str=None):
        self._rs.printGadgetsFor(name)


    def clear_cache(self):
        self._rs.clearCache()
        for k in self._all_cache:
            self._all_cache[k].clear()
        self._log("clear cache success!")


    def set_imagebase(self, name:str, base: int=0):
        self._rs.setImageBaseFor(name, base)


    def _inner_search(self, stmt, name, search_type, get_list):
        if search_type not in self._all_cache:
            raise RopperError("Wrong search_type: %s" % search_type)
        data = self._all_cache[search_type]
        
        if name and (name in data) and (stmt in data[name]):
            return data[name][stmt][0]
        
        if not name:
            for n, s in data.items():
                if stmt in s:
                    return s[stmt][0]
        
        _l = None
        res = (self._search_func[search_type])(stmt, name=name)
        for n, ds in res.items():
            if ds:
                _l = data[n].get(stmt, [])
                for d in ds:
                    if search_type == 'string':
                        _v = d[0]
                    else:
                        _v = d.address
                    if _v not in _l:
                        self._log("find one {} ---> {}".format(search_type, d))
                        _l.append(_v)

        if not _l:
            raise RopperError("Cannot find %s." % stmt)
        
        return _l if get_list else _l[0]


    def search_gadget(self, search: str, name: str=None, get_list: bool=False) -> Union[List[int], int]:
        return self._inner_search(search, name, "gadget", get_list)


    def search_string(self, string: str, name: str=None, get_list: bool=False) -> Union[List[int], int]:
        return self._inner_search(string, name, "string", get_list)


    def search_opcode(self, opcode: str, name: str=None, get_list: bool=False) -> Union[List[int], int]:
        return self._inner_search(opcode, name, "opcode", get_list)


    def get_pop_rdi_ret(self, name: str=None) -> int:
        try:
            return self.search_gadget("pop rdi; ret;", name)
        except RopperError:
            return self.search_opcode("5fc3", name)


    def get_pop_rsi_ret(self, name: str=None) -> int:
        try:
            return self.search_gadget("pop rsi; ret;", name)
        except RopperError:
            return self.search_opcode("5ec3", name)


    def get_pop_rdx_ret(self, name: str=None) -> int:
        try:
            return self.search_gadget("pop rdx; ret;", name)
        except RopperError:
            return self.search_opcode("5ac3", name)


    def get_ret(self, name: str=None) -> int:
        try:
            return self.search_gadget("ret;", name)
        except RopperError:
            return self.search_opcode("c3", name)


    def get_syscall(self, name: str=None) -> int:
        try:
            return self.search_gadget("syscall;", name)
        except RopperError:
            return self.search_opcode("0f05", name)


    def get_syscall_ret(self, name: str=None) -> int:
        try:
            return self.search_gadget("syscall; ret;", name)
        except RopperError:
            return self.search_opcode("0f05c3", name)
    