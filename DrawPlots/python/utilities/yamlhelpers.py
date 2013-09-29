import ROOT
import re
import yaml
import yaml.constructor

try:
    # included in standard lib from Python 2.7
    from collections import OrderedDict
except ImportError:
    # try importing the backported drop-in replacement
    from ordereddict import OrderedDict

class ttHMultileptonYAMLLoader(yaml.Loader):
    def __init__(self, *args, **kwargs):
        yaml.Loader.__init__(self, *args, **kwargs)

        self.add_constructor(u'tag:yaml.org,2002:map', type(self).construct_yaml_map)
        self.add_constructor(u'tag:yaml.org,2002:omap', type(self).construct_yaml_map)
        self.add_constructor(u'!ROOT', type(self).root_scalar_constructor)
        self.add_constructor(u'!ROOT:color', type(self).root_color_constructor)
        possible_colors = re.compile('.*kWhite.*|.*kBlack.*|.*kGray.*|.*kRed.*|.*kGreen.*|.*kBlue.*|.*kYellow.*|.*kMagenta.*|.*kCyan.*|.*kOrange.*|.*kSpring.*|.*kTeal.*|.*kAzure.*|.*kViolet.*|.*kPink.*')
        self.add_implicit_resolver(u'!ROOT:color', possible_colors, None)

    def construct_yaml_map(self, node):
        data = OrderedDict()
        yield data
        value = self.construct_mapping(node)
        data.update(value)

    def construct_mapping(self, node, deep=False):
        if isinstance(node, yaml.MappingNode):
            self.flatten_mapping(node)
        else:
            raise yaml.constructor.ConstructorError(None, None,
                'expected a mapping node, but found %s' % node.id, node.start_mark)

        mapping = OrderedDict()
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                hash(key)
            except TypeError, exc:
                raise yaml.constructor.ConstructorError('while constructing a mapping',
                    node.start_mark, 'found unacceptable key (%s)' % exc, key_node.start_mark)
            value = self.construct_object(value_node, deep=deep)
            mapping[key] = value
        return mapping

    def root_color_constructor(loader, node, deep=False):
        color_string = loader.construct_scalar(node)
        parts = re.split('\+|\-', str(color_string), 1)
        color = getattr(ROOT, parts[0])
        if '+' in color_string:
            color += int(parts[1])
        if '-' in color_string:
            color -= int(parts[1])

        return color

    def root_scalar_constructor(loader, node, deep=False):
        value = loader.construct_scalar(node)
        attribute = getattr(ROOT, value)

        return attribute
