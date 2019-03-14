def new_decorator(func):

    def wrap_func():
        print("Code here before exucuting func")
        func()
        print("func() has been called")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is need of a decorator")

'''
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
'''
func_needs_decorator()
