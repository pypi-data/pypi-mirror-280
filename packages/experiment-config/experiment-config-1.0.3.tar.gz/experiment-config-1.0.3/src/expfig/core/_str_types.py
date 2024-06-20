import argparse


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


class TypeToNone:
    def __init__(self, _type):
        self.type = _type

    def __call__(self, v):
        if v in (None, 'None', 'null'):
            return None
        return self.type(v)

    def __repr__(self):
        return f'TypeToNone({repr(self.type)})'

    def __eq__(self, other):
        if isinstance(self, type(other)) or isinstance(other, type(self)):
            return self.type == other.type

        return NotImplemented

    def __hash__(self):
        return hash(self.type)

    @property
    def valid_types(self):
        return self.type, type(None)


str2none = TypeToNone(str)
