import sys, yaml, pprint
pprint.pprint(list(yaml.load_all(''.join(sys.stdin.readlines()))))

