#!/usr/bin/python3
# encoding: utf-8
import filecmp
import os
import shutil
import yaml


def yamlToDic(file_path):
    dic = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        dic = yaml.safe_load(f)

    return dic


def main():
    file_path = './tools/githooks_config.yml'
    config = yamlToDic(file_path)

    for hook in config.get('hooks'):
        name = hook.get('name')
        src = hook.get('src')
        dst = hook.get('dst')
        # exist already and two files are the same
        if os.path.isfile(dst) and filecmp.cmp(src, dst):
            print('%s already exists' % name)
        else:
            shutil.copy(src, dst)
            print('%s creat successfully' % name)


if __name__ == "__main__":
    main()
