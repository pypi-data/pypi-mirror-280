import os
import argparse

from s3_helper.__init__ import __version__
from s3_helper.process import aws_process, initializer




def aws_s3_cli():
    parser = argparse.ArgumentParser(description="Configure your Amazon S3.")
    parser.add_argument('--version', action='version', version=f's3_manager - v{__version__}')
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand', metavar="", description="Available subcommands for managing AWS S3:")

    config_parser = subparsers.add_parser(
        'config',
        help='Manage the AWS S3 configuration',
        description='Configure various settings such as access credentials, default storage locations, and synchronization options. This command serves as the foundation for tailoring AWS S3 to your specific needs, ensuring seamless integration with your workflow.'
    )
    
    sub1 = config_parser.add_subparsers(title="config_subcommands", dest= "config_command", metavar="", description="Available subcommands for config:")

    sub1.add_parser("init", help="Interactively create config file for AWS S3.")
    remove_parser = sub1.add_parser("remove", help="Removes the specified profile from AWS S3 config.")
    list_parser = sub1.add_parser("list", help="List the contents of the AWS S3 config file.")
    set_parser = sub1.add_parser("set", help="Register the key-value in AWS S3 config file.")
    save_parser = sub1.add_parser("save", help="Save the AWS S3 config file.")

    sub2 = list_parser.add_subparsers(title="list_subcommands", dest="list_command", metavar="", description="Available subcommands for list:")

    sub2.add_parser("profile", help="List all available Profile.")

    set_parser.add_argument("key_value", nargs=2, help="Set or update the config file based on key-value.")
    set_parser.add_argument("--profile",  metavar="", help="Name of the profile used for AWS S3.", default="default")
    save_parser.add_argument("--profile",  metavar="", help="Name of the profile used for AWS S3.", default="default")
    list_parser.add_argument("--profile",  metavar="", help="Name of the profile used for AWS S3.", default="default")
    remove_parser.add_argument("profile_name", nargs="*", metavar="profile_name", help="Name of the AWS S3 profiles.")



    args = parser.parse_args()

    if args.config_command == "init":
        initializer.aws_config()
    
    elif args.config_command == "set":
        aws_process.set_config(args.profile, args.key_value[0], args.key_value[1])
    
    elif args.config_command == "list":

        if args.list_command == "profile":
            aws_process.list_profile()
        else: 
            aws_process.list_config(args.profile, True, False)
    
    elif args.config_command == "save":
        aws_process.list_config(args.profile, False, True)

    elif args.config_command == "remove":
        for i in args.profile_name:
            aws_process.remove_profile(i)