import os
import boto3
from datetime import datetime

import rich.box
from rich.live import Live
from rich.table import Table
from rich.console import Console

from s3_helper.utils import util, tree, progress





def s3_upload(path:str, directory:str, s3_bucket:str, s3_prefix:str, exclude_list:list, include_list:list, profile:str) -> None:
    """Upload file(s) from a directory to an S3 bucket.

    Args:
        path (str): The path to the '.s3_config' folder.
        directory (str): The directory containing file(s) to upload.
        s3_bucket (str): The name of the S3 bucket.
        s3_prefix (str): The prefix to use for S3 object keys.
        exclude_list (list): List of items to exclude from upload.
        include_list (list): List of items startswith '.' to include in upload.
        profile (str): The Profile to use in the AWS configure.

    Return:
        None  
    """
    try:
        assert isinstance(path, str) and os.path.exists(path), "path must be a string and exists."
        assert isinstance(directory, str) and os.path.exists(directory), "directory must be a string and exists."
        assert isinstance(s3_bucket, str), "s3_bucket must be a string."
        assert isinstance(s3_prefix, str), "s3_prfix must be a string."
        assert isinstance(exclude_list, (list,tuple)), "exclude_list must be a list or tuple of strings."
        assert isinstance(include_list, (list,tuple)), "include_list must be a list or tuple of strings."
        assert isinstance(profile, str), "profile must be a string."

        util.load_environ(profile)

        cons = Console()

        ld_bucket, ld_prefix, ld_exclude, ld_include = util.get_s3_config(os.path.join(path, ".s3_config/.config"))

        s3_bucket = ld_bucket if s3_bucket == "" else s3_bucket
        s3_prefix = ld_prefix if s3_prefix == "" else s3_prefix
        exclude_list = ld_exclude if exclude_list == [] else exclude_list
        include_list = ld_include if include_list == [] else include_list
        
        assert s3_bucket, "s3_bucket must not be empty. Please provide --s3-bucket and --s3-prefix in upload command."

        print("\nInitiating Upload process............")

        s3 = boto3.client('s3',
                            aws_access_key_id = os.environ["AWS_ACCESS_KEY"],
                            aws_secret_access_key = os.environ["AWS_SECRET_KEY"],
                            endpoint_url = os.environ["ENDPOINT_URL"]
                            )
        
        ld_buckt = [i["Name"] for i in s3.list_buckets()["Buckets"]]

        assert s3_bucket in ld_buckt, f"Bucket named '\033[1m\033[4m{s3_bucket}\033[00m' does not exists."

        obj_count, total_size, objects_path, checksum_lst = util.get_total_upload_objects(directory, s3_prefix, exclude_list, include_list, size_list=True)

        uploadable_index, reuploadable_index = util.get_uploadable_objects(s3, checksum_lst, objects_path,  s3_bucket, s3_prefix)

        up_size = []
        up_obj = []
        for i in uploadable_index:
            up_size.append(total_size[i])
            up_obj.append(objects_path[i])


        if obj_count <= 0:
            print("\nNo objects were found in the given directory.")
            print("\n\033[91m\033[1mInitiating Termination process...........\033[00m")
            print("\nTermination successfully completed.")
            exit()

        print("\n")

        tab = Table(title = "Upload Stats", box=rich.box.MARKDOWN, padding=(0,3), leading=1)

        tab.add_column("Parameters", justify="center", vertical="middle")
        tab.add_column("Value", justify="center", vertical="middle")
        
        tab.add_row("Bucket Name", s3_bucket)
        tab.add_row("Bucket Prefix", s3_prefix)
        tab.add_row("Upload Directory", directory)
        tab.add_row("Total Objects", str(len(objects_path)))
        tab.add_row("Total Uploadable Objects", str(len(uploadable_index)))
        tab.add_row("Total Re-Uploadable Objects", str(len(reuploadable_index)))
        tab.add_row("Total Objects Size", util.format_size(sum(total_size)))
        tab.add_row("Total Uploadable size", util.format_size(sum(up_size)))
        tab.add_row("Total Re-Uploadable size", util.format_size(sum([total_size[i] for i in reuploadable_index])))
        tab.add_row("Upload Date and Time", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        cons.print(tab)

        if len(reuploadable_index) > 0:
            exp_reup = input("\033[94m\033[1m\033[4m\nDo you want to add the re-uploadable files?\033[00m (yes/no): ")

            if exp_reup.lower() == "yes" or exp_reup.lower() =="y":
                
                print("\n")
                tab = Table(title = "Re-Upload Files", box=rich.box.MARKDOWN, padding=(0,3))

                tab.add_column("S.No", justify="center", vertical="middle")
                tab.add_column("File Name", justify="center", vertical="middle")
                tab.add_column("Size", justify="center", vertical="middle")

                for idx,j in enumerate(reuploadable_index):
                    tab.add_row(str(idx), os.path.split(objects_path[j])[-1], util.format_size(total_size[j]))
                
                cons.print(tab)
            
                upconfrm = input("\033[94m\033[1m\033[4m\nPlease Confirm the files you want to Re-Upload?\033[00m (use 'S.No' with space or 'a'/'all' to select all files): ")
                
                if upconfrm.lower() == "a" or upconfrm.lower() == "all":
                    for k in reuploadable_index:
                        up_size.append(total_size[k])
                        up_obj.append(objects_path[k])
                
                elif upconfrm.replace(" ", "").isdigit():
                    for k in upconfrm.strip().split():
                        up_size.append(total_size[reuploadable_index[int(k)]])
                        up_obj.append(objects_path[reuploadable_index[int(k)]])


        if len(up_obj) <= 0:
            print(f"\nNo Files to Upload as all files in the directory are already present in the \033[1m\033[4m{s3_bucket}\033[00m bucket and Unchanged.")
            print("\n\033[91m\033[1mInitiating Upload Termination process...........\033[00m")
            print("\nTermination successfully completed.")
            exit()


        dyrn = input("\033[94m\033[1m\033[4m\nAre you interested in exploring the folder structure of the uploadable files?\033[00m (yes/no): ")

        if dyrn.lower() == "yes" or dyrn.lower() =="y":

            tree.draw_tree(up_obj, up_size, is_s3=False)
        
        else:
            print("\n\033[91m\033[1mInitiating Explorer Termination process...........\033[00m")
            print("\nTermination successfully completed.")



        desisn = input("\033[94m\033[1m\033[4m\n\nDo you want to Proceed with Upload?\033[00m (yes/no): ")

        if desisn.lower() == "yes" or desisn.lower() =="y":

            print("\nInitiate Uploading.........\n")

            overall_task_id = progress.overall_progress.add_task("Uploading", total=len(up_obj))

            with Live(progress.progress_group):

                for obj_path, obj_size in zip(up_obj, up_size):
                    local_path = obj_path.replace(s3_prefix, directory)
                    
                    progress.overall_progress.update(overall_task_id)
                    
                    if obj_size > 52428800:
                        current_prog_id = progress.current_progress.add_task("upload", filename=os.path.split(obj_path)[-1], total=obj_size)

                        s3.upload_file(local_path, s3_bucket, obj_path.replace("\\","/"), Config=util.large_trans_config,
                                    Callback=progress.ProgressPercentage(current_prog_id))

                        progress.overall_progress.update(overall_task_id, advance=1)
                        progress.current_progress.update(current_prog_id, visible=False)

                    else:
                        s3.upload_file(local_path, s3_bucket, obj_path.replace("\\","/"), Config=util.small_trans_config)
                    
                        progress.overall_progress.update(overall_task_id, advance=1)

                progress.overall_progress.update(overall_task_id, description="Upload Completed")
        
            print("\nUpload Successfully Completed.")

        else:
            print("\n\033[91m\033[1mInitiating Upload Termination process...........\033[00m")
            print("\nTermination successfully completed.")
            exit()

    except KeyboardInterrupt:
        print("\n\n\033[91m\033[1mInitiating Upload Termination process...........\033[00m")
        print("\nTermination successfully completed.")
        exit()

    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()