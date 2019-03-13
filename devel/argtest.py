import argparse

class FooAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(FooAction, self).__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        print("foo help here")
        # print('%r %r %r' % (namespace, values, option_string))
        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help', action = FooAction)
# parser.add_argument('text', nargs='+', help='for standard text')
args = parser.parse_args()
print(args)
