import ConfigParser
import argparse
import csv
import json
import os
import re
import sys

DOMAIN = ''
GROUP_ID = ''


def parse_git_url(url_string):
    """
    Parse a git URL to extract the domain, group, repository name, and branch.

    :param url_string: str - The git URL to parse.
    :return: dict or None - Dictionary with parsed components or None if the URL doesn't match the pattern.
    """
    global DOMAIN
    global GROUP_ID
    pattern = (r"git@(?P<domain>[\w\.]+):(?P<group_id>[\w\-]+)/(?P<repo_name>[^/\.]+[\w\.-]*)\.git"
               r"\s+branch=(?P<branch>[^\s]+)")
    match = re.search(pattern, url_string)
    if match:
        DOMAIN = match.group('domain')
        GROUP_ID = match.group('group_id')
        return {'domain': match.group('domain'),
                'group_id': match.group('group_id'),
                'repo_name': match.group('repo_name'),
                'branch': match.group('branch')}
    return None


def get_src_branches(rcfg_filepaths):
    """
    Extract source branches from release configuration files.

    :param rcfg_filepaths: list - List of file paths to release configuration files.
    :return: dict - Dictionary of repository names to branch information.
    """
    src_branches = {}
    for rcfg_filepath in rcfg_filepaths:
        config = ConfigParser.ConfigParser()
        config.optionxform = str
        config.read(rcfg_filepath)
        if config.has_section('sources'):
            for key, value in config.items('sources'):
                repo_name = key.strip()
                url_info = parse_git_url(value.strip())
                if url_info:
                    src_branches[repo_name] = url_info
    return src_branches


def get_src_tags(vcfg_filepaths):
    """
    Extract source tags from version configuration files.

    :param vcfg_filepaths: list - List of file paths to version configuration files.
    :return: dict - Dictionary of repository names to tag information.
    """
    src_tags = {}
    for vcfg_filepath in vcfg_filepaths:
        config = ConfigParser.ConfigParser()
        config.optionxform = str
        config.read(vcfg_filepath)
        if config.has_section('versions'):
            for key, value in config.items('versions'):
                repo_name = key.strip()
                src_tags[repo_name] = {'tag': 'v{}'.format(value.strip())}
    return src_tags


def write_to_csv(csv_filepath, data_dict):
    """
    Write repository information to a CSV file.

    :param csv_filepath: str - File path to the CSV file.
    :param data_dict: dict - Dictionary containing repository information.
    """
    with open(csv_filepath, mode='wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for key, value in data_dict.items():
            writer.writerow([key, value['group_id'], value['ssh_url'], value['branch']])


def get_git_src_info(product_rcfg, custom_rcfg, product_vcfg, custom_vcfg, extra_sources, pattern):
    """
    Obtain source information for git repositories based on configuration files and additional sources.

    :param product_rcfg: str - Path to the product's release.cfg file.
    :param custom_rcfg: str - Path to the custom release.cfg file.
    :param product_vcfg: str - Path to the product's versions.cfg file.
    :param custom_vcfg: str - Path to the custom versions.cfg file.
    :param extra_sources: str - Additional source information in the format "user_id:name:branch".
    :param pattern: str - Regex pattern to filter repositories.
    :return: dict - Dictionary with source information.
    """
    domain = ''
    compiled_pattern = re.compile(pattern)
    rcfg_filepaths = [product_rcfg, custom_rcfg]
    vcfg_filepaths = [product_vcfg, custom_vcfg]

    rinfo = get_src_branches(rcfg_filepaths)
    vinfo = get_src_tags(vcfg_filepaths)

    src_dict = {}
    for key, value in vinfo.items():
        if compiled_pattern.match(key):
            if key in rinfo:
                domain = rinfo[key]['domain']
                group_id = rinfo[key]['group_id']
            else:
                domain = DOMAIN
                group_id = GROUP_ID
            ssh_url = 'git@{}:{}/{}.git'.format(domain, group_id, key)
            src_dict[key] = {'group_id': group_id, 'ssh_url': ssh_url, 'branch': value['tag']}

    crinfo = get_src_branches([custom_rcfg])
    for key, value in crinfo.items():
        if compiled_pattern.match(key):
            domain = value['domain']
            group_id = value['group_id']
            branch = value['branch']
            ssh_url = 'git@{}:{}/{}.git'.format(domain, group_id, key)
            src_dict[key] = {'group_id': group_id, 'ssh_url': ssh_url, 'branch': branch}

    if extra_sources:
        for each in extra_sources.split('|'):
            group_id, name, branch = each.split(':')
            ssh_url = 'git@{}:{}/{}.git'.format(domain, group_id, name)
            src_dict[name] = {'group_id': group_id, 'ssh_url': ssh_url, 'branch': branch}

    return {'count': len(src_dict.keys()), 'data': src_dict}


def main():
    """
    Main function to parse arguments and obtain git repositories source information.

    :return: None
    """
    parser = argparse.ArgumentParser(description='Obtain source information for git repositories')
    parser.add_argument('-pr', '--product_rcfg', help='Path to the product release.cfg file', required=True)
    parser.add_argument('-cr', '--custom_rcfg', help='Path to the custom release.cfg file', required=True)
    parser.add_argument('-pv', '--product_vcfg', help='Path to the product versions.cfg file', required=True)
    parser.add_argument('-cv', '--custom_vcfg', help='Path to the custom versions.cfg file', required=True)
    parser.add_argument('-e', '--extra_sources', help='Extra source information in the format "user_id:name:branch"')
    parser.add_argument('-o', '--csv_filepath', help='Path to the CSV file to write the source information')
    parser.add_argument('-p', '--pattern', help='Regex pattern to filter the repositories', required=True)
    parser.add_argument('-j', '--json', action='store_true', help='Output the source information in JSON format')
    args = parser.parse_args()

    for file_arg in [args.product_rcfg, args.custom_rcfg, args.product_vcfg, args.custom_vcfg]:
        if not os.path.isfile(file_arg):
            print '{} does not exist'.format(file_arg)
            sys.exit(1)

    src_info = get_git_src_info(product_rcfg=args.product_rcfg, custom_rcfg=args.custom_rcfg,
                                product_vcfg=args.product_vcfg, custom_vcfg=args.custom_vcfg,
                                extra_sources=args.extra_sources, pattern=args.pattern)

    if args.csv_filepath:
        write_to_csv(csv_filepath=args.csv_filepath, data_dict=src_info['data'])

    if args.json:
        print json.dumps(src_info, indent=4, sort_keys=True)


if __name__ == '__main__':
    main()
