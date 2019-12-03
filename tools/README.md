
# 文件说明

## auto_generate_changelog.py

根据 git 提交历史自动生成 `CHANGELOG.md` 文件在根目录

在此文件夹执行 `python auto_generate_changelog.py`

## split_file.py

将项目根目录的 `README.md` 中的 `LeetCode` 题目分隔为单个文件，并保存在 `Questions` 文件夹

在此文件夹执行 `python split_file.py`
## git hooks 设置
### git_hooks.py
在项目根目录执行 `python ./tools/git_hooks.py`
### githooks_config.yml
git hooks 的配置文件
### post-commit 
git hooks 文件
### pre-commit 
git hooks 文件

### python_comment_count.py

检查文件夹内的 `.py` 文件的注释率
> 可选参数

    --path：要统计的文件夹，默认是当前文件夹
    --debug：是否显示每一个文件的统计信息，默认不显示
    --percent：代码注释率最小有效值（针对整个文件夹），单位是百分比，默认是20
### encoding_check.py

检查文件编码，可以根据可选参数转换编码

> 可选参数

    --path：要转换编码的文件夹
    --debug：是否显示每一个文件的编码转换结果，默认显示
    --encoding：文件编码，默认为空，不进行编码转换
