#!/usr/bin/python3
# encoding: utf-8
import os
import shutil


def main():
    hooks = [
        {
            'name': 'hooks: pre_commit',
            'src': './tools/pre-commit',
            'dst': './.git/hooks/pre-commit'
        }
    ]

    for hook in hooks:
        name = hook.get('name')
        src = hook.get('src')
        dst = hook.get('dst')
        if os.path.isfile(dst):
            print('%s already exists' % name)
        else:
            shutil.copy(src, dst)
            print('%s creat successfully' % name)


if __name__ == "__main__":
    main()
