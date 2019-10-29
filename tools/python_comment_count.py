#!/usr/bin/python3
# encoding: utf-8
import os


def readFilePath(path, debug=True):
    # 代码总行数(不包含空行)、注释行数、空行数
    totalCodeCount, totalCommentCount, totalSpaceCount = 0, 0, 0
    files = os.listdir(path)  # 打开指定路径下所有文件及文件夹

    for file in files:
        # 获取.py文件
        if(os.path.isfile(path + '\\' + file) and (file[file.rfind('.'):] == '.py')):
            ff = open(path + '\\' + file, encoding='utf-8')
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
                percent = round(commentCount*100/codeCount, 2)
                info = '文件：{0}    注释行数/有效行数：{1}/{2}    空行数：{3}    代码注释率：{4}%'.format(
                    file, commentCount, codeCount, spaceCount, percent)
                print(info)

            totalCodeCount += codeCount
            totalCommentCount += commentCount
            totalSpaceCount += spaceCount

        if(os.path.isdir(path + '\\' + file)):  # 文件夹则递归查找
            if(file[0] == '.'):
                pass
            else:
                codeCount, commentCount, spaceCount = readFilePath(
                    path + '\\' + file, debug=debug)
                totalCodeCount += codeCount
                totalCommentCount += commentCount
                totalSpaceCount += spaceCount

    return totalCodeCount, totalCommentCount, totalSpaceCount


def main():
    config = {
        'path': './',  # 要统计的文件夹
        'debug': True,  # 是否显示每一个文件的统计信息
        'percent': 20  # 代码注释率最小有效值（针对整个文件夹）
    }
    file_path = config.get('path')
    if os.path.isdir(file_path):
        print('正在处理：%s' % file_path)
        totalCodeCount, totalCommentCount, totalSpaceCount = readFilePath(
            file_path, debug=config.get('debug'))
        percent = round(totalCommentCount*100/totalCodeCount, 2)
        info = '文件夹：{0}    注释行数/有效行数：{1}/{2}    空行数：{3}    代码注释率：{4}%'.format(
            file_path, totalCommentCount, totalCodeCount, totalSpaceCount, percent)
        print('*'*len(info))
        print(info)
        print('*' * len(info))
        if percent < config.get('percent'):
            raise Exception('code comments less than %s' %
                            (config.get('percent')))
    else:
        print('%s not found' % file_path)


if __name__ == "__main__":
    main()
