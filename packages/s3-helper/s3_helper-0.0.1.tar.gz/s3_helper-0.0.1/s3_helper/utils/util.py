import os
import stat
import boto3
import ctypes
import hashlib
import platform

from configparser import ConfigParser
from boto3.s3.transfer import TransferConfig




small_trans_config = TransferConfig(multipart_threshold=1024 * 256,
                                    max_concurrency=5,
                                    multipart_chunksize=1024 * 256,
                                    use_threads=True)


large_trans_config = TransferConfig(multipart_threshold=1024 * 1024 * 70,
                                    max_concurrency=30,
                                    multipart_chunksize=1024 * 1024 * 70,
                                    use_threads=True)

down_large_trans_config = TransferConfig(multipart_threshold=1024 * 1024 * 5,
                                         max_concurrency=30,
                                         multipart_chunksize=1024 * 1024 * 5,
                                         use_threads=True)


def validate_key(key:str) -> bool:
    '''Validates the given AWS key.

    Args:
        key (str): The AWS Key to validate.
    
    Return:
        bool: True of False. If True the Key is valid.
    '''

    return isinstance(key, str) and key.strip() != "" and key.strip().count(" ") == 0 and len(key.strip()) > 4





def is_admin() -> bool:
    '''Checks whether the code is running as admin.

    Args:
        None
    
    Return:
        bool: True of False. If True the code is running as admin.
    '''

    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    return is_admin





def load_config(file_path:str) -> ConfigParser:
    '''Load the given Config file.

    Args:
        file_path (str): The file path to load the config data.
    
    Return:
        ConfigParser: The instance of cofigparser to extract data from config.
    '''

    assert isinstance(file_path, str) and os.path.exists(file_path), "file_path must be a path in string and exists."
    assert os.path.isfile(os.path.join(file_path)), "No valid configuration found. Use 's3 config init'."

    config = ConfigParser()
    config.read(file_path)
    
    return config





def hide(file_path:str) -> bool:
    '''Hides the given file path including directories.

    Args:
        file_path (str): The file_path to hide.
    
    Return:
        bool: True of False. If True the is hided successfully.
    '''

    assert isinstance(file_path, str) and os.path.exists(file_path), "file_path must be a string and not starts with '.' and exists."

    plt = platform.uname().system
    dir, file = os.path.split(file_path)
    state = False

    if plt == "Linux":
        if file[0] != ".":
            os.rename(file_path, os.path.join(dir, "."+file))
        state = True
    
    elif plt == "Darwin":
        st = os.stat(file_path)
        os.chflags(file_path, st.st_flags | stat.UF_HIDDEN)
        state = True
    
    elif plt =="Windows":
        ret = ctypes.windll.kernel32.SetFileAttributesW(file_path, 0x02)
        if not ret:
            raise ctypes.WinError()
        state = True
    
    return state





def load_environ(profile:str) -> None:
    '''Loads the config environment Variables.

    Args:
        profile (str): The AWS profile to load.
    
    Return:
        None
    '''

    assert isinstance(profile, str), "profile must be a string."

    dir = os.path.expanduser("~")
    cred = load_config(os.path.join(dir, ".aws/credential"))
    conf = load_config(os.path.join(dir, ".aws/config"))
    cred._sections[profile].update(conf._sections[profile])

    for i,j in cred._sections[profile].items():
        os.environ[i] = j





def get_s3_config(path:str) -> tuple[str, str, list, list]:
    '''Retrives the local S3 config data.

    Args:
        path (str): The loacal S3 config path.
    
    Return:
        tuple: Contains bucket name, prefix, include items and exclude items.
    '''
    
    assert isinstance(path, str), "path must be a directory in string"
    assert os.path.exists(path), "No valid configuration found. Use 's3 config init' to create it."

    config = load_config(path)
    bucket = config.get('S3_CONFIG', 'bucket_name')
    prefix = config.get('S3_CONFIG', 'prefix')
    ignored_items = [item.strip() for item in config.get('S3_CONFIG', 'exclude', fallback='').split(',')]
    include_items = [item.strip() for item in config.get('S3_CONFIG', 'include', fallback='').split(',')]
    ignored_items = ignored_items + ["__pycache__"]

    return (bucket, prefix, ignored_items, include_items)






def format_size(size:int) -> str:
    '''Converts size in bytes to human understandable size format upto Terrabytes.

    Args:
        size (int): The value of size in bytes.

    Returns:
        str: Human understandable size format. 
    '''

    assert isinstance(size, int), "size must be an integer."

    if size < 1024:
        return f"{size} bytes"
    elif size < 1024 ** 2:
        return f"{size / 1024:.2f} KB"
    elif size < 1024 ** 3:
        return f"{size / (1024 ** 2):.2f} MB"
    elif size < 1024 ** 4:
        return f"{size / (1024 ** 3):.2f} GB"
    else:
        return f"{size / (1024 ** 4):.2f} TB"






def get_checksum(file:str|object, block_size:int = 71680) -> str:
    '''Generate MD5 checksum of a given file object.

    Args:
        file (str|file object): The file to generate MD5 checksum.
        block_size (int): The size of data to load at a time. It must be mentioned in bytes.
    
    Return:
        str: The MD5 checksum of the given file or file object.
    '''

    assert isinstance(block_size, int), "block_size must be an Integer represents number of bytes."

    checksum = hashlib.md5()

    if isinstance(file, str):

        assert os.path.exists(file) and os.path.isfile(file), "If file is string, It must be a path to a file and exists."
        
        with open(file, "rb+") as f:
            for block in iter(lambda: f.read(block_size), b""):
                    checksum.update(block)
    
    elif isinstance(file, bytes):
        checksum.update(file)

    else:
        for block in iter(lambda: file.read(block_size), b""):
                    checksum.update(block)
    
    return checksum.hexdigest()







def get_uploadable_objects(s3, cheksum_lst:list|tuple, obj_key:list|tuple, bucket:str, prefix:str) -> tuple[list, list]:
    '''Retrives the neccessary uploadable objects to S3 bucket.

    Args:
        s3 (client): The boto3 Client to connect to S3.
        checksum_lst (list|tuple): The MD5 checksum of all uploadable objects.
        obj_key (list|tuple): The path of the objects.
        bucket (str): The bucket name to upload the objects.
        prefix (str): The prefix to upload in S3 bucket.
    
    Return:
        tuple: Contains uploadable file list and re-uploadable file list.
    '''

    assert isinstance(cheksum_lst, (list,tuple)), "cheksum_lst must be a list or tuple."
    assert isinstance(obj_key, (list,tuple)), "obj_key must be a list or tuple."
    assert isinstance(bucket, str), "bucket must be a string."
    assert isinstance(prefix, str), "prefix must be a string."

    paginator = s3.get_paginator("list_objects_v2")
    response = paginator.paginate(Bucket=bucket, Prefix=prefix)

    objects_checksum = []
    reupable_objects = []
    upable_objects = []
    obj_file = []

    for k in  response:
        for i in k.get('Contents', []):

            if "-" not in i["ETag"].strip('"'):
                objects_checksum.append(i["ETag"].strip('"'))
            
            obj_file.append(os.path.split(i["Key"])[-1])

    for idx,(i,j) in enumerate(zip(cheksum_lst, obj_key)):

        file = os.path.split(j)[-1]

        if i not in objects_checksum and file not in obj_file:
            upable_objects.append(idx)
        
        elif i not in objects_checksum and file in obj_file:
            reupable_objects.append(idx)

    return (upable_objects, reupable_objects)
    





def get_total_upload_objects(directory:str, prefix:str, exclude_list:list, include_list:list, size_list:bool) -> tuple[int, int|list, list, list]:
    """Count the total number and retrive absolute path of the objects (files and directories) in a directory and also retrive the total file size.

    Args:
        directory (str): The directory to count objects in.
        prefix (str): The prefix to upload.
        exclude_list (list): List of items to exclude from uploading.
        include_list (list): List of items startswith '.' to include in uploading.
        size_list (bool): If set True, retuen file size in list. If set False, return sum of file sizes.

    Returns:
        int: The total number of objects in the directory.
        int: The total file size of the uploading objects.
        list: Absolute path of the objects in the directory.
    """

    assert isinstance(directory, str) and os.path.exists(directory), "directory must be a path to a directory in string and exists."
    assert isinstance(exclude_list, (list,tuple)), "exclude_list must be a list or tuple of strings."
    assert isinstance(include_list, (list,tuple)), "include_list must be a list or tuple of strings."

    total_obj_count = 0
    file_size = []
    obj_paths = []
    checksum_list = []

    if platform.uname().system == "Windows":
        splitter = "\\"
    else:
        splitter = "/"

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_list and d[0] != "." or d in include_list]
        
        for file in files:
            if file not in exclude_list and file[0] != "." or file in include_list:
                total_obj_count += 1
                file_size.append(os.stat(os.path.join(root, file)).st_size)
                
                if file_size[-1] <= 52428800:
                    checksum_list.append(get_checksum(os.path.join(root, file)))
                
                obj_paths.append(os.path.join(root.replace(directory, prefix), file))
    
    if not size_list:
        file_size = sum(file_size)
    
    return total_obj_count, file_size, obj_paths, checksum_list






def get_downloadable_objects(directory:str, cheksum_lst:list|tuple, obj_key:list|tuple) -> tuple[list, list]:
    '''Retrives the neccessary downloadable objects from S3 bucket.

    Args:
        directory (str): The directory to save the downloaded files.
        checksum_lst (list|tuple): The MD5 checksum of all downloadable objects.
        obj_key (list|tuple): The path of the objects.
    
    Return:
        tuple: Contains downloadable file list and re-downloadable file list.
    '''

    assert isinstance(directory, str), "directory must be a string."
    assert isinstance(cheksum_lst, (list,tuple)), "cheksum_lst must be a list or tuple."
    assert isinstance(obj_key, (list,tuple)), "obj_key must be a list or tuple."

    loc_obj = []
    redown_obj = []
    down_obj = []

    for _,_, files in os.walk(directory):
        loc_obj.extend(files)

    for idx,i in enumerate(obj_key):
        if os.path.split(i)[-1] in loc_obj:
            redown_obj.append(idx)
        else:
            down_obj.append(idx)
    
    return down_obj, redown_obj
    




def get_total_download_objects(bucket:str, prefix:str, exclude_list:list, size_list:bool) -> tuple[int, int|list, list, list]:
    """Count the total number and retrive absolute path of the objects (files and directories) in a bucket with a given prefix and also retrive the total file size.

    Args:
        bucket (str): The name of the S3 bucket.
        prefix (str): The prefix to filter objects by.
        exclude_list (list): List of items to exclude from downloading.
        size_list (bool): If set True, retuen file size in list. If set False, return sum of file sizes.

    Returns:
        int: The total number of objects in the S3 bucket with the given prefix.
        int: The total file size of the downloading objects.
        list: Absolute path of the objects in the S3 bucket.
        list: Checksum of each file in the S3 bucket.
    """
    
    assert isinstance(bucket, str), "bucket must be a string."
    assert isinstance(prefix, str), "prefix must be a string."
    assert isinstance(exclude_list, (list,tuple)), "exclude_list must be a list or tuple of strings."
    
    s3 = boto3.client('s3',
                      aws_access_key_id = os.environ["AWS_ACCESS_KEY"],
                      aws_secret_access_key = os.environ["AWS_SECRET_KEY"],
                      endpoint_url = os.environ["ENDPOINT_URL"]
                    )

    paginator = s3.get_paginator("list_objects_v2")
    response = paginator.paginate(Bucket=bucket, Prefix=prefix)

    total_obj_count = 0
    file_size = []
    obj_paths = []
    checksum_list = []

    for k in response:
        for i in k.get('Contents', []):
            
            dir, file = os.path.split(i["Key"])

            flg = False
            for d in dir.split("/"):
                if d in exclude_list:
                    flg=True
                    break
            
            if flg:
                continue
            
            if file not in exclude_list:
                obj_paths.append(i["Key"])
                checksum_list.append(i["ETag"].strip('"'))
                file_size.append(int(i["Size"]))
                total_obj_count += 1
        
    if not size_list:
        file_size = sum(file_size)

    return total_obj_count, file_size, obj_paths, checksum_list