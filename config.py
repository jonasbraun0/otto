# My thought is that we shouldn't enforce too much structure wrt config
# formatting. Simply create the config directory and any yaml file in the
# directory will get recursively parsed into the global config. This will
# allow users to organize configs however they want.
import yaml

def parse():
    stream = open('config.yaml', 'r')

    # TODO: Apparently calling this way is deprecated
    data = yaml.load(stream)
    
    for a in data:
    	print(a)
