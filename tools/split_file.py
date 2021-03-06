#!/usr/bin/python3
# encoding: utf-8
import os


def file_create(file_name, txt):
    """
    write txt to a file
    :param file_name:the name of file
    :param txt:text
    """
    folder = '../Questions/'
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(os.path.join(folder, file_name), mode='w', encoding='utf-8') as f:
        f.write(txt)


def main():
    file_name = ''
    txt = ''
    first = True
    with open('../Question.md', mode='r', encoding='utf-8') as f:
        for s in f.readlines():
            if s[0] == '#':
                if first:
                    first = False
                else:
                    file_create(file_name + '.md', txt)
                    txt = ''
                nums = s.split('.')[0].split()[1]
                file_name = nums + '.' + s.split('[')[1].split(']')[0]
                print(file_name)
            txt += s

    file_create(file_name + '.md', txt)  # the last one


if __name__ == "__main__":
    main()
