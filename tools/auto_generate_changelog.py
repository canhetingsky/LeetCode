#!/usr/bin/python3
# encoding: utf-8
import os


changelog = 'conventional-changelog -p angular -i ../CHANGELOG.md -s -r 0'
os.system(changelog)
