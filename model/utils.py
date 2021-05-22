import sys
import os
import yaml
from collections import OrderedDict


def yml_dumper(file, dictData, flowStyle=False) :
    # input dictionary data
    data = ordered_dump(dictData, Dumper=yaml.SafeDumper, default_flow_style=flowStyle)
    with open(file, 'w') as f:
        f.write(data)
    return True


def yml_loader(file) :
    class Loader(yaml.Loader):
        """ add !include yaml constructor """
        def __init__(self, stream):
            self._root = os.path.split(stream.name)[0]
            super(Loader, self).__init__(stream)

        def include(self, node):
            filename = os.path.join(self._root, self.construct_scalar(node))

            with open(filename, 'r') as f:
                return ordered_load(f, Loader)

    Loader.add_constructor('!include', Loader.include)

    with open(file, 'r') as stream:
        dictData = ordered_load(stream, Loader)

        return dictData


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


def ordered_dump(data, stream=None, Dumper=yaml.Dumper, **kwds):
    class OrderedDumper(Dumper):
        pass
    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())
    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)


def get_latest_price(crypto, compare_coin='USDT'):
    import cryptocompare
    price = cryptocompare.get_price(crypto, compare_coin)
    return price
