import os
import boto3

import rich.box
from rich.table import Table
from rich.console import Console

from s3_helper.utils import util, tree





def set_s3_config(path:str, key:str, value) -> None:
    '''Updates a key value in local S3 configure.

    Args:
        path (str): The path to the local S3 config.
        key (str): The Key to change the value in local S3 config.
        value : The value to change in local S3 config.
    
    Returns:
        None
    '''
        
    try:
        assert isinstance(path, str) and os.path.exists(path), "path must be a path in string format and exists."
        assert isinstance(key, str), "Key must be a string."

        conf = util.load_config(os.path.join(path, ".s3_config/.config"))

        assert key in ["bucket_name", "prefix", "exclude", "include"], f"The given key named '\033[4m{key}\033[0m' does not supported. Available Keys are 'bucket_name', 'prefix', 'exclude' and 'include'."

        conf._sections["S3_CONFIG"][key] = value

        with open(os.path.join(path, ".s3_config/.config"), "w+") as f:
            conf.write(f)

        print("\nSuccessfully updated S3 config.")

    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()





def list_s3_config(path:str) -> None:
    '''Shows the data in local S3 configure in a table format.

    Args:
        path (str): The path to the local S3 config.
    
    Returns:
        None
    '''

    try:
        assert isinstance(path, str) and os.path.exists(path), "path must be a path in string format and exists."
        assert os.path.exists(os.path.join(path, ".s3_config/.config")), "No valid configuration found. Use 's3 config init'."

        cons = Console()
        conf = util.load_config(os.path.join(path, ".s3_config/.config"))
        data = {"profile": "S3_CONFIG"}
        data.update(conf._sections["S3_CONFIG"])

        print("\n")

        tab = Table(title = "S3 config", box=rich.box.MARKDOWN, padding=(0,3), leading=1)

        tab.add_column("Name", justify="right", vertical="middle")
        tab.add_column("value", justify="right", vertical="middle")

        for i, j in data.items():
            tab.add_row(i,j)
        
        cons.print(tab)
    
    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()





def list_s3_bucket_objects(s3_bucket:str, s3_prefix:str, exclude_list:list, profile:str, path:str) -> None:
    '''Shows the S3 bucket objects in a pretty tree like structure.

    Args:
        s3_bucket (str): The bucket name to list objects from S3.
        s3_prefix (str): The prefix to get objects from S3.
        exclude_list (list): The files to exclude from the bucket.
        profile (str): The profile to load the AWS config.
        path (str): The path to the local S3 config file.
    
    Returns:
        None
    '''

    try:
        assert isinstance(s3_bucket, str), "s3_bucket must be a string."
        assert isinstance(s3_prefix, str), "s3_prfix must be a string."
        assert isinstance(profile, str), "profile must be a string."
        assert isinstance(path, str) and os.path.exists(path), "path must be a string and exists."
        assert isinstance(exclude_list, (list,tuple)), "exclude_list must be a list or tuple of strings."

        util.load_environ(profile)

        ld_bucket, ld_prefix, ld_exclude, _ = util.get_s3_config(os.path.join(path, ".s3_config/.config"))

        s3_bucket = ld_bucket if s3_bucket == "" else s3_bucket
        s3_prefix = ld_prefix if s3_prefix == "" else s3_prefix
        exclude_list = ld_exclude if exclude_list == [] else exclude_list

        _, file_size, objects_path, _ = util.get_total_download_objects(s3_bucket, s3_prefix, exclude_list, size_list=True)

        if len(objects_path) > 0:
            tree.draw_tree(objects_path, file_size, is_s3=True)

            print("\nTotal file objects: ", len(objects_path))
            print("Total size of the file objects: ", util.format_size(sum(file_size)))
        
        else:
            print(f"\nThere is no objects present in the bucket named '\033[1m\033[4m{s3_bucket}\033[0m'")
            print("\n\033[91m\033[1mInitiating Termination process...........\033[00m")
            print("\nTermination successfully completed.")
            exit()

    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()





def list_s3_buckets(profile:str) -> None:
    '''Shows all Buckets present in the S3 in a table format.

    Args:
        profile (str): The profile to load the AWS config.

    Returns:
        None
    '''

    try:
        assert isinstance(profile, str), "profile must be a string."

        util.load_environ(profile)

        cons = Console()

        s3 = boto3.client('s3',
                        aws_access_key_id = os.environ["AWS_ACCESS_KEY"],
                        aws_secret_access_key = os.environ["AWS_SECRET_KEY"],
                        endpoint_url = os.environ["ENDPOINT_URL"]
                        )
        
        print("\n")

        tab = Table(title = "Amazon S3 Buckets", box=rich.box.MARKDOWN, padding=(0,3))

        tab.add_column("Bucket Name", justify="center", vertical="middle")
        tab.add_column("Creation Date", justify="center", vertical="middle")

        for i in s3.list_buckets()["Buckets"]:
            tab.add_row(i["Name"], i["CreationDate"].strftime("%d-%m-%Y %H:%M:%S"))

        cons.print(tab)
    
    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()





def delete_s3_bucket_objects(s3_bucket:str, s3_prefix:str, exclude_list:list, profile:str, path:str) -> None:
    '''Delete the S3 bucket objects from S3 bucket.

    Args:
        s3_bucket (str): The bucket name to list objects from S3.
        s3_prefix (str): The prefix to get objects from S3.
        exclude_list (list): The files to exclude from the bucket.
        profile (str): The profile to load the AWS config.
        path (str): The path to the local S3 config file.
    
    Returns:
        None
    '''

    try:
        assert isinstance(s3_bucket, str), "s3_bucket must be a string."
        assert isinstance(s3_prefix, str), "s3_prfix must be a string."
        assert isinstance(profile, str), "profile must be a string."
        assert isinstance(path, str) and os.path.exists(path), "path must be a string and exists."
        assert isinstance(exclude_list, (list,tuple)), "exclude_list must be a list or tuple of strings."

        util.load_environ(profile)

        ld_bucket, ld_prefix, ld_exclude, _ = util.get_s3_config(os.path.join(path, ".s3_config/.config"))

        s3_bucket = ld_bucket if s3_bucket == "" else s3_bucket
        s3_prefix = ld_prefix if s3_prefix == "" else s3_prefix
        exclude_list = ld_exclude if exclude_list == [] else exclude_list


        obj_count, file_size, objects_path, _ = util.get_total_download_objects(s3_bucket, s3_prefix, exclude_list, size_list=False)

        if obj_count <= 0:
            print("\nNo objects were found in the bucket with given prefix.")
            return

        print("\nNumber of deleting objects :", obj_count)
        print("Total size of deleting objects :", util.format_size(file_size), "\n")

        s3 = boto3.client('s3',
                            aws_access_key_id = os.environ["AWS_ACCESS_KEY"],
                            aws_secret_access_key = os.environ["AWS_SECRET_KEY"],
                            endpoint_url = os.environ["ENDPOINT_URL"]
                            )

        chc = input("\033[91m\033[1m\033[4mAre you sure? Do you still want to continue?\033[00m (yes/no): ")

        if chc.lower() == "yes" or chc.lower() =="y":

            s3.delete_objects(Bucket=s3_bucket, Delete={"Objects": [{"Key": i} for i in objects_path]})

            print("\nObjects Deleted Successfully.")
        
        else:
            print("\nTerminating the deletion Process..........")
            print("\nTermination Successfull.")
    
    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()






def delete_s3_bucket(s3_bucket:str, profile:str, path:str) -> None:
    '''Delete the S3 bucket from S3.

    Args:
        s3_bucket (str): The bucket name to list objects from S3.
        profile (str): The profile to load the AWS config.
        path (str): The path to the local S3 config file.
    
    Returns:
        None
    '''

    try:
        assert isinstance(s3_bucket, str), "s3_bucket must be a string."
        assert isinstance(profile, str), "profile must be a string."
        assert isinstance(path, str) and os.path.exists(path), "path must be a string and exists."

        util.load_environ(profile)

        print("\nInitiating Bucket deletion process.........")

        ld_bucket, _, _, _ = util.get_s3_config(os.path.join(path, ".s3_config/.config"))

        s3_bucket = ld_bucket if not s3_bucket else s3_bucket

        s3 = boto3.client('s3',
                            aws_access_key_id = os.environ["AWS_ACCESS_KEY"],
                            aws_secret_access_key = os.environ["AWS_SECRET_KEY"],
                            endpoint_url = os.environ["ENDPOINT_URL"]
                            )
        
        if s3_bucket not in [i["Name"] for i in s3.list_buckets()["Buckets"]]:
            print(f"\nNo buckets were found in the S3 with the given bucket name '\033[4m{s3_bucket}\033[0m'.")
            return
        
        print("\nBucket selected for Deletion :", s3_bucket)

        bkt_typed_name = input(f"\033[91m\033[1m\033[4m\nYou are about to delete a bucket named\033[00m '\033[4m{s3_bucket}\033[0m'. \033[91m\033[1m\033[4mPlease type\033[00m '\033[4m{s3_bucket}\033[0m' \033[91m\033[1m\033[4mto continue the deletion process\033[00m: ")

        if bkt_typed_name != s3_bucket:
            print("\nTermination of deletion process initiated due to bucket name does not match.")
            print("\nTermination successfull.")
            return
        
        chc = input("\033[91m\033[1m\033[4m\nAre you sure? Do you still want to continue?\033[00m (yes/no): ")

        if chc.lower() == "yes" or chc.lower() =="y":

            _, _, objects_path, _ = util.get_total_download_objects(s3_bucket, '', [], size_list=False)

            if len(objects_path) > 0:
                s3.delete_objects(Bucket=s3_bucket, Delete={"Objects": [{"Key": i} for i in objects_path]})

            s3.delete_bucket(Bucket=s3_bucket)

            print("\nBucket Deleted Successfully.")
        
        else:
            print("\nTerminating the deletion Process..........")
            print("\nTermination Successfull.")

    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()






def create_s3_bucket(bucket_name:list|tuple, profile:str) -> None:
    '''Create a S3 bucket for all given names in S3.

    Args:
        bucket_name (list|tuple): The list of bucket names to create in S3.
        profile (str): The profile to load the AWS config.
    
    Returns:
        None
    '''

    try:
        assert isinstance(bucket_name, (list, tuple)), "bucket_name must be a string or list or tuple."
        assert isinstance(profile, str), "profile must be a string."

        util.load_environ(profile)

        print("\nInitiating Bucket creation process.........")

        s3 = boto3.client('s3',
                            aws_access_key_id = os.environ["AWS_ACCESS_KEY"],
                            aws_secret_access_key = os.environ["AWS_SECRET_KEY"],
                            endpoint_url = os.environ["ENDPOINT_URL"]
                            )
        
        s3_buckt = [i["Name"] for i in s3.list_buckets()["Buckets"]]
        bukt_crt = 0

        for bkt in bucket_name:
            if bkt in s3_buckt:
                print(f"\nBucket named '\033[4m{bkt}\033[0m' was already existed.")
                print("Contnuing the creation Process.")
                continue

            else:
                s3.create_bucket(Bucket=bkt)
                bukt_crt += 1
        
        if bukt_crt > 0:
            print("\nS3 Buckets were created successfully.")
        else:
            print("\nNo Buckets were created as all the given buckets are already existed.")

    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()