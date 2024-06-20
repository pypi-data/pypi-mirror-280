def nvl(v, default):
    if v is None:
        return default
    else:
        return v
    
def nvl_call(v, default_call):
    if v is None:
        return default_call()
    else:
        return v

def cast_if_type(v, cast_func, desired_type:type):
    if isinstance(v, desired_type):
        return cast_func(v)
    else:
        return v



