import datetime

def module_show():
    Module_type = dir(datetime)
    print(dir(Module_type))

def date_now():
    return datetime.datetime.now()
