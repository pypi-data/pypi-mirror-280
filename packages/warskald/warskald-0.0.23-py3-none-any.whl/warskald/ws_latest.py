from warskald.utils import cmdx, load_data
import time

PACKAGE_JSON = '/home/joseph/coding_base/ws-ui-2/package.json'

package_json = load_data(PACKAGE_JSON,use_global_data_path=False)

version = package_json.get('version', 'latest')

def main():
    #time.sleep(3)
    cmdx(f'npm install warskald-ui@{version}')
    
if(__name__ == '__main__'):
    main()