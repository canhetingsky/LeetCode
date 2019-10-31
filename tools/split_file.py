#!/usr/bin/python3
# encoding: utf-8


def file_create(file_name, txt):
    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write(txt)


def main():
    file_name = ''
    txt = ''
    nums = 0
    first = True
    with open('../Question.md', mode='r', encoding='utf-8') as f:
        for s in f.readlines():
            if s[0] == '#':
                if first:
                    first = False
                else:
                    file_create(file_name + '.md', txt)
                    txt = ''
                nums += 1
                file_name = str(nums) + '.' + s.split('[')[1].split(']')[0]
                print(file_name)
            txt += s

    file_create(file_name + '.md', txt)


if __name__ == "__main__":
    main()
