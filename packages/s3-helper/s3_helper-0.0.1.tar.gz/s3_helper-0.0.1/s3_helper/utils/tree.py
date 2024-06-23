import os
import platform

import rich
from rich.tree import Tree
from rich.text import Text

from s3_helper.utils import util


def draw_tree(path:str|list|tuple, size_list:list, is_s3:bool) -> None:
    '''Draws a Tree like File structure.

    Args:
        path (str|list|tuple): The path to create a Tree like file structure.
        size_list (list): The size_list of all the files in the path.
        is_s3 (bool): It is a flg whether the give path is from s3 or not.
    
    Return:
        None
    '''

    assert isinstance(path, (str,list,tuple)), "path must be a string or list or tuple."
    assert isinstance(size_list, (list, tuple)), "size_list must be a list or tuple of integers."

    tree_dict = {}

    if platform.uname().system == "Windows":
        splitter = "\\"
    else:
        splitter = "/"


    if isinstance(path, str):

        assert os.path.exists(path) and os.path.isdir(path), "if path is a string, It represent the path to a directory and exists."
           
        path = path.strip(splitter)
        splroot = path.split(splitter)

        for i in range(1,len(splroot)+1):
            
            if splroot[i-1] not in tree_dict and i == 1:
                tree_dict[splroot[i-1]] = Tree(f":file_folder: {splroot[i-1]}", guide_style="bold bright_blue")
                tree_dict["main_tree"] = tree_dict[splroot[i-1]]
            
            else:
                tree_dict[splitter.join(splroot[:i])] = tree_dict[splitter.join(splroot[:i-1])].add(f":file_folder: {splroot[i-1]}")

        for root, dir, file in os.walk(path):
            
            for d in dir:
                tree_dict[os.path.join(root, d)] = tree_dict[root].add(f":file_folder: {d}")

            for f in file:
                icon = "🐍 " if f.endswith(".py") else "📄 "
                tree_dict[root].add(f"{Text(icon)}{f} ==============> [{util.format_size(int(os.stat(os.path.join(root,f)).st_size))}]")

    else:

        if is_s3:
            splitter = "/"

        sort_lst = sorted(path, key=lambda x:len(x.split(splitter)), reverse=True)

        for idx, i in enumerate(sort_lst):

            dirs, file = os.path.split(i)
            spldir = dirs.split(splitter)
            
            if idx == 0:
                tree_dict[spldir[0]] = Tree(f":file_folder: {spldir[0]}", guide_style="bold bright_blue")
                tree_dict["main_tree"] = tree_dict[spldir[0]]

            for d in range(1,len(spldir)+1):
                if splitter.join(spldir[:d]) not in tree_dict:
                    tree_dict[splitter.join(spldir[:d])] = tree_dict[splitter.join(spldir[:d-1])].add(f":file_folder: {spldir[d-1]}")

            icon = "🐍 " if file.endswith(".py") else "📄 "
            tree_dict[dirs].add(f"{Text(icon)}{file} ==============> [{util.format_size(int(size_list[path.index(i)]))}]")

    print("\n")
    rich.print(tree_dict["main_tree"])