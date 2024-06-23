import os
import rich
import json
import toml

import rich.box
from rich.table import Table
from rich.console import Console

from s3_helper.utils import util





def list_profile() -> None:
    '''Lists All profiles present in the AWS configure.

    Args:
        None
    
    Returns:
        None
    
    '''

    try:
        home_path = os.path.expanduser("~")
        cons = Console()

        cred = util.load_config(os.path.join(home_path, ".aws/credential"))
        conf = util.load_config(os.path.join(home_path, ".aws/config"))

        cred_keys = list(cred._sections.keys())
        conf_keys = list(conf._sections.keys())

        if cred_keys != conf_keys:
            corrupted_profile = list(set(cred_keys).difference(set(conf_keys)))
            raise AssertionError(f"There are {len(corrupted_profile)} corrupted profiles named '{' ,'.join(corrupted_profile)}'. Please use 's3 config remove <profile-name>'.")

        else:
            print("")
            
            tab = Table(title="AWS S3 Profiles", box=rich.box.MARKDOWN, leading=1)
            tab.add_column("Profile", justify="center", vertical="middle")

            for i in conf_keys:
                tab.add_row(i)
            
            cons.print(tab)

    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()





def list_config(profile:str, table:bool, save:bool) -> None:
    '''Shows or saves the config file of AWS configure.

    Args:
        profile (str): The Profile to use in the AWS configure.
        tabel (bool): Shows the config file in table format.
        save (bool): Save the config file in specified format as in AWS configure.
    
    Returns:
        None
    '''

    try:
        assert isinstance(profile, str), "profile must be a string."
        assert isinstance(table, bool), "table must be either True or False."
        assert isinstance(save, bool), "save must be either True or False."
        assert (not table and save) or (not save and table), "Either table or save must be True."

        dir = os.path.expanduser("~")
        cons = Console()

        cred = util.load_config(os.path.join(dir, ".aws/credential"))
        conf = util.load_config(os.path.join(dir, ".aws/config"))

        if profile not in conf._sections.keys():
            print(f"\nProfile name '\033[4m{profile}\033[0m' was not found in AWS S3 config.")
            print("\n\033[91m\033[1mInitiating Termination process...........\033[00m")
            print("Termination completed.")
            exit()

        if not util.is_admin():
            for i in cred._sections[profile].keys():
                cred._sections[profile][i] = "*" * (len(cred._sections[profile][i])-4) + cred._sections[profile][i][-4:]

        cred._sections[profile].update(conf._sections[profile])

        data = {"profile": profile}
        data.update(cred._sections[profile])

        if table:
            print("\n")

            tab = Table(title = "AWS S3 config", box=rich.box.MARKDOWN, padding=(0,3), leading=1)

            tab.add_column("Name", justify="right", vertical="middle")
            tab.add_column("value", justify="right", vertical="middle")

            for i, j in data.items():
                tab.add_row(i,j)
            
            cons.print(tab)
        
        elif save:
            with open(os.path.join(os.getcwd(), f"config.{data['output']}"), "w+") as f:
                
                if data["output"] == "txt":
                    f.writelines("\n".join([f"{i} = {j}" for i,j in data.items()]))
                
                elif data["output"] == "json":
                    json.dump(data, f, indent=1)
                
                elif data["output"] == "toml":
                    toml.dump(cred._sections[profile], f)

            print("\nConfig file saved successfully.")
            print(f"\nIt is saved in '{os.getcwd()}' as 'config.{data['output']}'")
    
    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()





def set_config(profile:str, key:str, value) -> None:
    '''Updates data of AWS configure.

    Args:
        profile (str): The Profile to use in the AWS configure.
        key (bool): The key in the config file.
        value (Any): Value to be set to key in the AWS configure.
    
    Returns:
        None
    '''

    try:
        assert isinstance(profile, str), "profile must be a string."
        assert isinstance(key, str), "Key must be a string."

        home_path = os.path.expanduser("~")

        cred = util.load_config(os.path.join(home_path, ".aws/credential"))
        conf = util.load_config(os.path.join(home_path, ".aws/config"))

        if profile not in conf._sections.keys():
            print(f"\nProfile name '\033[4m{profile}\033[0m' was not found in AWS S3 config.")
            print("\n\033[91m\033[1mInitiating Termination process...........\033[00m")
            print("Termination completed.")
            exit()

        if key in ["aws_access_key", "aws_secret_key"]:
   
            assert util.validate_key(value), "Secret or Access key must not be empty and contain no white-spaces between the key and length greater than 4."
            
            cred._sections[profile][key] = value
            with open(os.path.join(home_path, ".aws/credential"), "w+") as f:
                cred.write(f)
        
        else:
            conf._sections[profile][key] = value
            with open(os.path.join(home_path, ".aws/config"), "w+") as f:
                conf.write(f)

        print("\nSuccessfully updated AWS S3 config.")

    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()





def remove_profile(profile:str) -> None:
    '''Removes a profile from AWS configure.

    Args:
        profile (str): The Profile to remove in the AWS configure.
    
    Returns:
        None
    '''

    try:
        assert isinstance(profile, str), "profile must be a string."

        home_path = os.path.expanduser("~")

        cred = util.load_config(os.path.join(home_path, ".aws/credential"))
        conf = util.load_config(os.path.join(home_path, ".aws/config"))

        if profile not in conf._sections.keys():
            print(f"\nProfile name '\033[4m{profile}\033[0m' was not found in AWS S3 config.")
            print("\n\033[91m\033[1mInitiating Termination process...........\033[00m")
            print("Termination completed.")
            exit()


        if profile in cred._sections.keys():
            
            del cred._sections[profile]

            with open(os.path.join(home_path, ".aws/credential"), "w+") as f:
                cred.write(f)
        
        if profile in conf._sections.keys():

            del conf._sections[profile]

            with open(os.path.join(home_path, ".aws/config"), "w+") as f:
                conf.write(f)
    
        print(f"\nProfile name '\033[4m{profile}\033[0m' was successfully removed from the AWS S3 config.")

    except Exception as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()