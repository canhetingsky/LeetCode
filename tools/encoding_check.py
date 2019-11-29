import codecs
import chardet
import os
import argparse
"""
用于本地githooks，pre-commit文件编码检查、转换、重新提交
"""


def showInfo(path, src_encoding, dst_encoding):
    """
    控制台输出信息
    :param file:文件的路径
    :param src_encoding:文件的原始编码
    :param dst_encoding:文件的目标编码
    :return info:要显示的字符串
    """
    if len(path) > 30:
        path = path[:27]+'...'
    info = "{0:30s}: {1}->{2}".format(os.path.basename(path),
                                      src_encoding, dst_encoding)
    return info


def gitAddFile(file):
    # run command 'git add ...' to add the changed files
    os.system('git add ' + file)


def convertFile(file, dst_encoding='utf-8', debug=True):
    """
    对文件进行编码转换
    :param file:文件的路径
    :param dst_encoding:文件的目标编码
    :param debug:True-开启输出显示;False-关闭输出显示;
    """
    content = codecs.open(file, 'rb').read()
    result = chardet.detect(content)
    src_encoding = result['encoding']  # 如果文件为空，src_encoding=None
    exclude = ['ascii'] + [dst_encoding]  # 不需要进行转换的编码
    if src_encoding and src_encoding not in exclude:
        if debug:
            info = showInfo(file, src_encoding, dst_encoding)
            print(info)
        content = content.decode(src_encoding).encode(dst_encoding)  # 重新编码
        codecs.open(file, 'wb').write(content)  # 按照目标编码写入文件
        gitAddFile(file)


def convertPath(path):
    files = os.listdir(path)
    for file in files:
        sub_path = os.path.join(path, file)  # the relative path of the file
        if os.path.isfile(sub_path):
            convertFile(sub_path)
        if os.path.isdir(sub_path):
            if(file[0] == '.'):  # 隐藏文件夹，不处理
                pass
            else:
                convertPath(sub_path)  # backtracking


def main(args):
    path = args.path  # 要转换编码的文件夹
    if os.path.isdir(path):
        print('encoding check:%s' % path)
        convertPath(path)
    else:
        print('%s not found' % path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage="it's usage tip.", description="help info.")
    parser.add_argument("--path", default='./',
                        help="the folder to process.", dest="path")
    args = parser.parse_args()
    main(args)
