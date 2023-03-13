import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", dest="url", required=False)

args = parser.parse_args()

print(args.url)