import os
from datetime import datetime
def loger_constructor_decor(file_name, file_path=None):
    if file_path is None:
        file_place = os.path.join(os.getcwd())
    else:
        file_place = os.path.join(os.path.abspath(file_path))

    file_path = os.path.join(file_place, file_name)

    def decorator(old_function):
            def new_func(*args,**kwargs):
                output = old_function(*args,**kwargs)
                result = f'{old_function.__name__} was called at {datetime.today()} \n' \
                         f'Used args: {args} и {kwargs} \n' \
                         f'Result status {old_function.__name__}: {output}'
                with open(file_path, 'a', encoding='utf-8') as f:
                    f.write(result)
                return result
            return new_func

    return decorator


