from warskald import utils
from warskald.ws_config import EnvPropsReader
from warskald.attr_dict import AttrDict

ENV_PROPS = EnvPropsReader()

def main():
    app_props = ENV_PROPS.config
    print(__name__)

if(__name__ == '__main__'):
    main()