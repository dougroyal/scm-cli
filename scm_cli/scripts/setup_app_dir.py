import os

print('##############################')

try:
    os.makedirs(os.path.expanduser(os.path.join('~', '.scm')))
except:
    print('already there')
    pass
