dev = True
prod = False
test = False

if dev:
    from settings.dev import *
elif prod:
    from settings.prod import *
elif test:
    from settings.test import *