
def get_profile(*args, name='julian', profession='programmer'):
    if args:
        raise TypeError
    return f"{name} is a {profession}"




def get_profile(**kwargs):
    name = kwargs.get('name', 'julian')
    profession = kwargs.get('profession', 'programmer')
    if name or profession:
        return f"{name} is a {profession}"
    raise TypeError('erro')


print(get_profile('helo'))