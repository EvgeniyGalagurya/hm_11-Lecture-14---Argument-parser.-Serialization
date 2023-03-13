import argparse
from helpers.github import get_github_repositories, json_parser
from helpers.writter import write

parser = argparse.ArgumentParser()

parser.add_argument("-q", dest="query")

args = parser.parse_args()

body = get_github_repositories(args.query)
repositories = json_parser(body)
write(repositories)
print("Done!")
