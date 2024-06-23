import os

from configparser import ConfigParser
from collections import defaultdict

from s3_helper.utils import util





def aws_config() -> None:
    """Interactively creates the aws config file based on user input."""

    try:
        cred, conf = ConfigParser(), ConfigParser()
        home_path = os.path.expanduser("~")
        
        print("\nInitializing Interactive Console...........\n")

        profile = input("Enter the Profile Name : ")
        profile = profile if profile != "" else "default"
        prof = []

        if os.path.exists(os.path.join(home_path, ".aws/credential")):
            cred = util.load_config(os.path.join(home_path, ".aws/credential"))
        
        if os.path.exists(os.path.join(home_path, ".aws/config")):
            conf = util.load_config(os.path.join(home_path, ".aws/config"))
            prof = conf._sections.keys()

        if profile not in prof:
            cred[profile], conf[profile] = defaultdict(), defaultdict()

        
        region = input("Enter the Region Name : ")
        conf[profile]["region"] = region if region != "" else "us-west"

        url = input("Enter the endpoint-url (without port): ")

        if url != "" and url[-1] != "/":
            url = url+"/"
        conf[profile]["endpoint_url"] = url

        out_fmt = input("Enter the Output format : ")
        if out_fmt not in ["txt", "json", "toml"]:
            print("\nThe given output format does not support. Using default output format 'txt'.\n")
            out_fmt = "txt"
        conf[profile]["output"] = out_fmt
 
        while True:
            accesskey = input("Enter the Access Key : ")
            if util.validate_key(accesskey):
                cred[profile]["aws_access_key"] = accesskey
                break
            print("\n\033[4mAccess key must not be empty and contain no white-spaces between the key and length greater than 4\033[0m.\n")
        
        while True:
            secretkey = input("Enter the Secret Key : ")
            if util.validate_key(secretkey):
                cred[profile]["aws_secret_key"] = secretkey
                break
            print("\n\033[4mSecret key must not be empty and contain no white-spaces between the key and length greater than 4\033[0m.\n")
        
        os.makedirs(os.path.join(home_path, ".aws"),exist_ok=True)

        with open(os.path.join(home_path, ".aws/credential"), "w+") as f:
            cred.write(f)
        
        with open(os.path.join(home_path, ".aws/config"), "w+") as f:
            conf.write(f)
        
        util.hide(os.path.join(home_path, ".aws"))

        print("\n\033[4mAWS S3 config file created successfully!\033[0m")

    except KeyboardInterrupt:
        print("\n\033[91m\033[1m\033[4mError\033[00m: Operation canceled by user.")
    except Exception as e:
        print("An error occurred \033[91m\033[1m\033[4mError\033[00m:", e)




def s3_config() -> None:
    """Interactively creates the local .s3_config file for S3 based on user input."""

    try:
        config = ConfigParser()

        if os.path.exists(os.path.join(os.getcwd(), ".s3_config")) and os.path.isdir(os.path.join(os.getcwd(), ".s3_config")):
            print("\nS3 '\033[4mconfig\033[0m' already exists in the current directory.")
            return
        
        print("\nInitializing Interactive Console...........\n")

        bucket_name = input("Enter S3 bucket name: ")
        prefix = input("Enter S3 prefix: ")
        exclude = input("Enter excluded items (comma-separated): ")
        include = input("Enter included items startwith '.' (comma-seperated): ")

        config['S3_CONFIG'] = {'BUCKET_NAME': bucket_name,
                               'PREFIX': prefix,
                               'EXCLUDE': exclude,
                               'INCLUDE': include
                               }

        os.makedirs(os.path.join(os.getcwd(), ".s3_config"), exist_ok=True)
        config_file_path = os.path.join(os.getcwd(), '.s3_config/.config')
        
        with open(config_file_path, 'w') as config_file:
            config.write(config_file)
        
        util.hide(os.path.join(os.getcwd(), ".s3_config"))

        print("\nS3 '\033[4mconfig\033[0m' file created successfully at the current directory.")

    except KeyboardInterrupt:
        print("\n\033[91m\033[1m\033[4mError\033[00m: Operation canceled by user.")
    except Exception as e:
        print("\nAn error occurred \033[91m\033[1m\033[4mError\033[00m: ", e)