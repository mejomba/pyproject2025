dev = True
prod = False
test = True

if dev:
    from config.setting.dev import *
elif prod:
    from config.setting.prod import *
elif test:
    from config.setting.test import *
