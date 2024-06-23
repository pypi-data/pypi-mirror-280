import os
import boto3
import platform
from datetime import datetime

import rich.box
from rich.live import Live
from rich.table import Table
from rich.console import Console

from s3_helper.utils import util, progress



def s3_download(path: str, s3_bucket: str, s3_prefix: str, directory: str, exclude_list: list,
                     profile: str) -> None:
    """Download files(s) from an S3 bucket to a local directory.

    Args:
        path (str): The path to the '.s3_config' folder.
        s3_bucket (str): The name of the S3 bucket.
        s3_prefix (str): The prefix to filter S3 objects.
        directory (str): The local directory to save downloaded file(s).
        exclude_list (list): List of items to exclude from download.
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
        assert isinstance(profile, str), "profile must be a string."

        if platform.uname().system == "Windows":
            splitter = "\\"
        else:
            splitter = "/"

        util.load_environ(profile)

        cons = Console()

        ld_bucket, ld_prefix, ld_exclude, _ = util.get_s3_config(os.path.join(path, ".s3_config/.config"))

        s3_bucket = ld_bucket if s3_bucket == "" else s3_bucket
        s3_prefix = ld_prefix if s3_prefix == "" else s3_prefix
        exclude_list = ld_exclude if exclude_list == [] else exclude_list

        assert s3_bucket, "s3_bucket must not be empty. Please provide --s3-bucket and --s3-prefix in upload command."

        print("\nInitiating Download process............")

        s3 = boto3.client('s3',
                            aws_access_key_id = os.environ["AWS_ACCESS_KEY"],
                            aws_secret_access_key = os.environ["AWS_SECRET_KEY"],
                            endpoint_url = os.environ["ENDPOINT_URL"]
                            )
        
        ld_buckt = [i["Name"] for i in s3.list_buckets()["Buckets"]]

        assert s3_bucket in ld_buckt, f"Bucket named '\033[1m\033[4m{s3_bucket}\033[00m' does not exists."

        obj_count, total_size, objects_path, checksum_lst = util.get_total_download_objects(s3_bucket, s3_prefix, exclude_list, size_list=True)

        downloadable_index, redownloadable_index = util.get_downloadable_objects(directory, checksum_lst, objects_path)

        down_size = []
        down_obj = []
        local_path = []
        for i in downloadable_index:
            down_size.append(total_size[i])
            down_obj.append(objects_path[i])
            local_path.append(objects_path[i])

        if obj_count <= 0:
            print("\nNo objects were found in the given bucket with prefix.")
            print("\n\033[91m\033[1mInitiating Termination process...........\033[00m")
            print("\nTermination successfully completed.")
            exit()

        print("\n")

        tab = Table(title = "Download Stats", box=rich.box.MARKDOWN, padding=(0,3), leading=1)

        tab.add_column("Parameters", justify="center", vertical="middle")
        tab.add_column("Value", justify="center", vertical="middle")
        
        tab.add_row("Bucket Name", s3_bucket)
        tab.add_row("Bucket Prefix", s3_prefix)
        tab.add_row("Download Directory", directory)
        tab.add_row("Total Objects", str(len(objects_path)))
        tab.add_row("Total Downloadable Objects", str(len(downloadable_index)))
        tab.add_row("Total Re-Downloadable Objects", str(len(redownloadable_index)))
        tab.add_row("Total Objects Size", util.format_size(sum(total_size)))
        tab.add_row("Total Downloadable size", util.format_size(sum(down_size)))
        tab.add_row("Total Re-Downloadable size", util.format_size(sum([total_size[i] for i in redownloadable_index])))
        tab.add_row("Download Date and Time", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        cons.print(tab)

        exp_redown = input("\033[94m\033[1m\033[4m\nDo you want to add the re-downloadable files?\033[00m (yes/no): ")

        if exp_redown.lower() == "yes" or exp_redown.lower() == "y":
            fol_cnfrm = input("\033[94m\033[1m\033[4m\nDo you want to downlad the re-downloadable files to a different folder?\033[00m (yes/no): ")
            
            if fol_cnfrm.lower() == "yes" or fol_cnfrm.lower() == "y":
                while True:
                    fold = input("\033[90m\033[1m\033[4m\nSpecify the folder path to download\033[00m (give relative path): ")
                    
                    if not os.path.exists(os.path.join(directory,fold.replace("/", splitter))) or len(os.listdir(os.path.join(directory,fold.replace("/", splitter)))) <= 0 or fold == "":
                        fold = "copy_of_redownloaded_objects"
                        break

                    print("\033[93m\033[4m\nPlease Specify another folder path to download as such given folder path already exists.\033[00m")
                
                for k in redownloadable_index:
                    down_obj.append(objects_path[k])
                    down_size.append(total_size[k])
                    local_path.append(objects_path[k].replace(s3_prefix, os.path.join(directory, fold.replace("/", splitter))).replace("/", splitter))
                
            else:
                for k in redownloadable_index:
                    down_obj.append(objects_path[k])
                    down_size.append(total_size[k])
                    local_path.append(objects_path[k].replace(s3_prefix, directory).replace("/", splitter))
        

        if len(down_obj) <= 0:
            print(f"\nNo Files to Download as all files in the \033[1m\033[4m{s3_bucket}\033[00m bucket are already present in the directory.")
            print("\n\033[91m\033[1mInitiating Upload Termination process...........\033[00m")
            print("\nTermination successfully completed.")
            exit()



        desisn = input("\033[94m\033[1m\033[4m\nDo you want to Proceed with Download?\033[00m (yes/no): ")

        if desisn.lower() == "yes" or desisn.lower() =="y":

            print("\nInitiate Downloading.........\n")

            overall_task_id = progress.overall_progress.add_task("Downloading", total=len(down_obj))

            with Live(progress.progress_group):

                for obj_path, obj_size, loc_path in zip(down_obj, down_size, local_path):

                    os.makedirs(os.path.split(loc_path)[0], exist_ok=True)

                    progress.overall_progress.update(overall_task_id)
                    
                    if obj_size > 26214400:
                        current_prog_id = progress.current_progress.add_task("download", filename=os.path.split(obj_path)[-1], total=obj_size)

                        s3.download_file(s3_bucket, obj_path, loc_path, Config=util.down_large_trans_config,
                                    Callback=progress.ProgressPercentage(current_prog_id))

                        progress.overall_progress.update(overall_task_id, advance=1)
                        progress.current_progress.update(current_prog_id, visible=False)
                    
                    else:
                        s3.download_file(s3_bucket, obj_path, loc_path, Config=util.small_trans_config)
                    
                        progress.overall_progress.update(overall_task_id, advance=1)

                progress.overall_progress.update(overall_task_id, description="Download Completed")
            
            print("\nDownload Successfully Completed.")
        
        else:
            print("\n\033[91m\033[1mInitiating Download Termination process...........\033[00m")
            print("\nTermination successfully completed.")
            exit()

    except KeyboardInterrupt:
        print("\n\n\033[91m\033[1mInitiating Download Termination process...........\033[00m")
        print("\nTermination successfully completed.")
        exit()

    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()