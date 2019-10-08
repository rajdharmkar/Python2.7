def catch(func, handle=lambda e : e, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return handle(e)

eggs = (1,3,0,3,2)
[catch(lambda : 1/egg) for egg in eggs]

#[1, 0, ('integer division or modulo by zero'), 0, 0]

# a = (1,3,0,3,2)
# def spam(a):
#     try:
#         #for i in a:
#         return 1/a, None
#     except ZeroDivisionError as err:
#         # handle division by zero error
#         return None, err
# spam(a)