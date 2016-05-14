import sys
import inspect
import base

# Add custom behaviour to some class:
#class Device(base.BaseDevice):
#    def my_method(self):
#        ...

class RR(base.BaseRR):
    @property
    def label(self):
        return '%s.%s' % (self.name, self.zone)

class Ipblock(base.BaseIpblock):
    @property
    def label(self):
        return '%s/%s' % (self.address, self.prefix)

# Generate classes for each class in base module. But skip those already
# defined in this module.
my_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
my_names = [n for n,_ in my_classes]
for base_name, cls in inspect.getmembers(base, inspect.isclass):
    name = base_name.replace('Base', '')
    if name in my_names:
        continue
    globals()[name] = type(name, (cls,), {})
