from log_decorator import loger_constructor_decor
from path_file import result_file_name as f1, result_dir as f2
@loger_constructor_decor(f1,f2)
def some_func(a,b):
    return a+b
if __name__ == '__main__':
    some_func(1,5)
