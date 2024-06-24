import argparse
import csv
import os
import shutil
import sys


def get_pkg_names_from_csv(csv_filepath):
    """
    Retrieves package names from a CSV file.

    Args:
    - csv_filepath (str): Path to the CSV file containing package names.

    Returns:
    - list: List of unique package names extracted from the CSV file.
    """
    pkg_names = set()
    with open(csv_filepath, mode='rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            pkg_names.add(row[0])
    return list(pkg_names)


def get_pkg_names_from_src_dir(src_dir):
    """
    Retrieves package names from a source directory.

    Args:
    - src_dir (str): Path to the source directory containing package directories.

    Returns:
    - list: List of unique package names found in the source directory.
    """
    pkg_names = set()
    for filename in os.listdir(src_dir):
        pkg_name = os.path.basename(filename)
        pkg_names.add(pkg_name)
    return list(pkg_names)


def remove_directory(directory_path):
    """
    Removes a directory and all its contents.

    Args:
    - directory_path (str): Path to the directory to be removed.
    """
    try:
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)
            print 'Deleted \'{}\' directory.'.format(directory_path)
    except Exception as e:
        print 'Error: {} : {}'.format(directory_path, e)


def main():
    """
    Main function to execute the script.
    """
    parser = argparse.ArgumentParser(description='Remove invalid git source repositories')
    parser.add_argument('-s', '--source_dir', help='Path to the source directory', required=True)
    parser.add_argument('-i', '--csv_filepath', help='Path to the CSV file to read the source information',
                        required=True)
    args = parser.parse_args()

    if not os.path.isfile(args.csv_filepath):
        print '{} does not exist'.format(args.csv_filepath)
        sys.exit(1)

    if not os.path.isdir(args.source_dir):
        print '{} is not a directory or does not exist'.format(args.source_dir)
        sys.exit(1)

    csv_pkg_names = get_pkg_names_from_csv(args.csv_filepath)
    src_pkg_names = get_pkg_names_from_src_dir(args.source_dir)

    for pkg in src_pkg_names:
        if pkg not in csv_pkg_names:
            print 'Package \'{}\' does not exist in the CSV file'.format(pkg)
            src_dir = os.path.join(args.source_dir, pkg)
            remove_directory(src_dir)


if __name__ == '__main__':
    main()
