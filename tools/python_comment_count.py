#!/usr/bin/python3
# encoding: utf-8
import os
import argparse


def readFilePath(path, debug=True, percent=20):
    # 代码总行数(不包含空行)、注释行数、空行数
    totalCodeCount, totalCommentCount, totalSpaceCount = 0, 0, 0
    files = os.listdir(path)  # 打开指定路径下所有文件及文件夹

    for file in files:
        # 获取.py文件
        if(os.path.isfile(path + '/' + file) and (file[file.rfind('.'):] == '.py')):
            ff = open(path + '/' + file, encoding='utf-8')
            codeCount = commentCount = spaceCount = 0
            flag = False  # 块注释标识
            first = True

            for line in ff.readlines():  # 逐行读取.py文件
                sLine = line.strip()
                if len(sLine) == 0:
                    spaceCount += 1
                    continue
                else:
                    codeCount += 1

                if sLine.find('#') >= 0:
                    commentCount = commentCount + 1
                elif sLine.find("'''") >= 0 or sLine.find('"""') >= 0:  # 块注释
                    flag = bool(1 - flag)

                if flag:
                    start_line = codeCount
                    first = False
                else:
                    if not first:
                        end_line = codeCount
                        commentCount = end_line - start_line + 1

            if debug:
                info, passed = showInfo(
                    'file', file, commentCount, codeCount, spaceCount, min_percent=percent)
                passed = passed
                print(info)

            totalCodeCount += codeCount
            totalCommentCount += commentCount
            totalSpaceCount += spaceCount

        if(os.path.isdir(path + '/' + file)):  # 文件夹则递归查找
            if(file[0] == '.'):
                pass
            else:
                codeCount, commentCount, spaceCount = readFilePath(
                    path + '/' + file, debug=debug)
                totalCodeCount += codeCount
                totalCommentCount += commentCount
                totalSpaceCount += spaceCount

    return totalCodeCount, totalCommentCount, totalSpaceCount


def showInfo(type, path, commentCount, codeCount, spaceCount, min_percent=20):
    if codeCount == 0:
        percent = 0
    else:
        percent = round(commentCount*100/codeCount, 2)

    if len(path) > 30:
        path = path[:27]+'...'
    info = '{0}: {1:30s}    comment/code:{2:4d}/{3:<4d}    space:{4:<4d}    percent:{5:.2f}%'.format(
        type, path, commentCount, codeCount, spaceCount, percent)
    if percent >= min_percent:
        info = '[√] ' + info
        passed = True
    else:
        info = '[×] ' + info
        passed = False
    return info, passed


def main(args):
    config = {
        'path': args.path,  # 要统计的文件夹
        'debug': args.debug,  # 是否显示每一个文件的统计信息
        'percent': args.percent  # 代码注释率最小有效值（针对整个文件夹）
    }
    print(config)
    dict_path = config.get('path')
    if os.path.isdir(dict_path):
        print('dealing with:%s' % dict_path)
        totalCodeCount, totalCommentCount, totalSpaceCount = readFilePath(
            dict_path, debug=config.get('debug'), percent=config.get('percent'))
        min_percent = config.get('percent')
        info, passed = showInfo('dict', dict_path, totalCommentCount,
                                totalCodeCount, totalSpaceCount, min_percent=min_percent)
        print('*' * len(info))
        print(info)
        print('*' * len(info))
        if not passed:
            err = 'code comments less than {0}%'.format(min_percent)
            raise Exception(err)
    else:
        print('%s not found' % dict_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage="it's usage tip.", description="help info.")
    parser.add_argument("--path", default='./',
                        help="the folder to process.", dest="path")
    parser.add_argument("--debug", choices=[True, False], type=bool,
                        default=False, help="whether to show each file.", dest="debug")
    parser.add_argument("--percent", type=int, default=20,
                        help="minimum code coverage")
    args = parser.parse_args()
    main(args)
