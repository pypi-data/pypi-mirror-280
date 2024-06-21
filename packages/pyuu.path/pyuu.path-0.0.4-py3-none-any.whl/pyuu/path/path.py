#-*-conding:utf-8-*-
import typing
import os
import pathlib
import shutil
import heapq
from pyuu.iter import dfs



__all__ = ['Path']




def get_min_not_in_l(l:typing.List[int], min_val:int = 1):
    "Return min({r| r >= min_val and r is not in l})"
    if not len(l):
        return min_val
    heapq.heapify(l)
    v = heapq.heappop(l)
    if v>min_val:
        return min_val
    while len(l):
        v+=1
        u = heapq.heappop(l)
        if u != v:
            return v
    return v+1

def make_unique_name(name:str, src):
    "make a name which is different from names in src"
    if name not in src:
        return name
    d_nums = []
    for x in src:
        if f'{name}_' == f'{x[0:len(name)]}_':
            try: 
                d_num = int(x[len(name)+1: ])
            except ValueError:
                continue
            d_nums.append(d_num)
    uq_num = get_min_not_in_l(d_nums,1)
    return f'{name}_{uq_num}'


_Path = type(pathlib.Path(''))

__all__ = ['Path']


class Path(pathlib.Path):
    _Path = _Path

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def __new__(cls, *args, **kwargs):
    #     if len(args) == 1 and len(kwargs) == 0:
    #         p = args[0]
    #         if type(p) == Path:
    #             return p
    #     return super().__new__(cls, *args, **kwargs)

    @staticmethod
    def setcwd(path):
        os.chdir(path)
    
    @staticmethod
    def getcwd():
        return os.getcwd()

    @property
    def prnt(self):
        return Path(super().parent)

    @property
    def ext(self):
        return super().suffix[1:]

    @property
    def size(self):
        return self.stat().st_size

    @property
    def mtime(self):
        "time of most recent content modification"
        return self.stat().st_mtime

#begin iter
    def iter_child(self, *filters):
        if self.is_dir():
            if len(filters) == 0:
                return super().iterdir()
            return filter(lambda x: all(map(lambda f: f(x), filters)), super().iterdir())
        else:
            return iter([])

    def iter_child_file(self, *filters):
        return self.iter_child(Path.is_file, *filters)

    def iter_child_dir(self, *filters):
        return self.iter_child(Path.is_dir, *filters)

    def iter_sibling(self, *filters):
        return self.prnt.iter_child(lambda x: x!=self, *filters)

    @property
    def child_iter(self):
        return self.iter_child()

    @property
    def sibling_iter(self, *filters):
        return self.iter_sibling()

    @property
    def child_file_iter(self):
        return self.iter_child_file()

    @property
    def child_dir_iter(self):
        return self.iter_child_dir()

    @property
    def children(self):
        return list(self.child_iter)
    
    @property
    def siblings(self):
        return list(self.sibling_iter)

    @property
    def child_files(self):
        return list(self.child_file_iter)

    @property
    def child_dirs(self):
        return list(self.child_dir_iter)
#end iter

    @property
    def str(self):
        return self.__str__()

    @property
    def quote(self):
        if Path._Path == pathlib.WindowsPath:
            s = self.str.replace('"', r'\"')
            return f'"{s}"'

    def is_empty_dir(self):
        if self.is_dir():
            for _ in self.child_iter:
                return False
            return True
        return False

    def rel_to(self,path):
        return super().relative_to(path)

    def open(self, mode, buffering=-1, encoding='utf8', newline='', *args, **kwargs):
        if 'b' in mode:
            encoding=None
            newline=None
        if not self.prnt.exists():
            self.prnt.mkdir()
        return super().open(mode=mode,buffering=buffering, encoding=encoding, newline=newline, *args,**kwargs)
    
    def write(self, content):
        if isinstance(content, bytes):
            with self.open('wb') as f:
                f.write(content)
        elif isinstance(content, str):
            with self.open('w') as f:
                f.write(content)
        else:
            raise TypeError
        
    def read_text(self, encoding='utf8'):
        with self.open('r',encoding=encoding) as f:
            return f.read()
    
    def mkdir(self, *args, update =False, parents =True, **kwargs):
        '''
        Ignore if the directory already exists.
        Create parent directories if not exist.
        '''
        if self.exists():
            if update:
                self.remove()
                super().mkdir(*args, parents=parents, **kwargs)
        else:
            super().mkdir(*args, parents=parents, **kwargs)

    def remove(self):
        if self.exists():
            if self.is_dir():
                shutil.rmtree(self.to_str())
            else:
                os.remove(self.to_str())

    def remove_sons(self):
        assert(self.is_dir())
        for son in self.child_iter:
            son.remove()
    
    def to_str(self):
        return str(self)

    def copy_to(self, dst:'Path', is_prefix = True, update = True, overwrite = True):
        '''
        会自动创建当前不存在的父目录
        
        若is_prefix == False:
        将该路径复制，复制后的路径为dst
        若is_prefix == True:
        则将该路径复制到dst目录下，复制后的名字不变
        
        若路径为目录，则会递归复制
        '''
        if is_prefix:
            dst = dst/self.name

        if not self.exists():
            raise FileNotFoundError
    
        def copy_func(src, dst):
            if update and Path(src).newer_than(Path(dst)):
                shutil.copy(src, dst)
            else:
                if not overwrite and dst.exists():
                    raise FileExistsError
                shutil.copy(self, dst)

        dst.prnt.mkdir()
        if self.is_file():
            if dst.is_dir():
                raise FileExistsError
            copy_func(self, dst)
        else:
            if dst.is_file():
                raise FileExistsError
            shutil.copytree(self, dst, copy_function=copy_func, dirs_exist_ok=overwrite)

    def copy_sons_to(self, dst, update = True):
        dst = Path(dst)
        assert self.is_dir()
        for son in self.child_iter:
            son.copy_to(dst/son.name, is_prefix=False, update=update)

    def make_copy(self, name:'str', update=False):
        self.copy_to(self.prnt/name, is_prefix=False, update=update)

    def move_to(self, dst, is_prefix=True, update=True, recursive=True):
        dst = Path(dst)
        if is_prefix:
            dst = dst/self.name
        if recursive:
            for src in dfs(self, Path.iter_child, lambda p: p.is_file() or p.is_empty_dir()):
                src:Path
                if update and dst.exists():
                    dst.remove()
                shutil.move(src.str, (dst/src.rel_to(self)).str)
        else:
            if update and dst.exists():
                dst.remove()
            shutil.move(self.str, dst.str)


    def make_archive(self, dst, format = None):
        dst = Path(dst)
        if format == None:
            format = dst.detect_format_by_suffix()
            if format == None:
                format = 'zip'
        a = self.absolute().to_str()
        b = dst.absolute().to_str()
        shutil.make_archive(b, format, a)

    def unpack_archive_to(self, dst, format = None):
        if format == None:
            format = self.detect_format_by_suffix()
        a = self.absolute().to_str()
        b = Path(dst).absolute().to_str()
        shutil.unpack_archive(a,b,format)

    def detect_format_by_suffix(self):
        m = {
            'zip' : 'zip',
            'tar' : 'tar',
            'gz' : 'gztar',
            'bz' : 'bztar',
            'xz' : 'xztar'
        }
        ext = self.ext
        if ext:
            format = m.get(ext)
            if format:
                return format
            else:
                return ext

    def get_unique_path(self):
        '''
        return a path which is different from its siblings.
        '''
        ext = self.ext
        stem_list = [x.stem for x in self.siblings if x.ext == ext]
        stem = make_unique_name(self.stem, stem_list)
        name = f'{stem}.{ext}'
        return self.prnt/name

    def make_temp_dir(self):
        if self.is_file():
            dir_ = self.prnt
        else:
            dir_ = self
        uqtmp = (dir_/'temp').get_unique_path()
        uqtmp.mkdir()
        return uqtmp

    def remove_temp_sons(self):
        assert(self.is_dir())
        for son in self.children:
            if son.name.startswith('temp'):
                son.remove()

    def rename_inplace(self, name:'str'):
        new_path = self.prnt/name
        self.rename(new_path)

    def move_all_sons_to(self, dst):
        for son in self.children:
            son.move_to(dst)

    def move_all_out(self):
        assert(self.is_dir())
        uq_name = make_unique_name(self.name,[x.name for x in self.child_iter] + [x.name for x in self.siblings])
        if uq_name!=self.name:
            self.rename_inplace(uq_name)
            self = self.prnt/uq_name
        self.move_all_sons_to(self.prnt)
        self.remove()

    def newer_than(self, other:'Path'):
        other=Path(other)
        if not other.exists():
            return self.exists()
        if self.exists():
            return self.mtime>other.mtime
        return False

del _Path




