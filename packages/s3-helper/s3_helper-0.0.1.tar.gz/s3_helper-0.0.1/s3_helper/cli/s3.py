import argparse
import os

from s3_helper.__init__ import __version__
from s3_helper.process import s3_process, initializer
from s3_helper.process import upload, download


    


def s3_cli():
    parser = argparse.ArgumentParser(description="Upload and download directories/files from Amazon S3")
    parser.add_argument('--version', action='version', version=f's3_manager - v{__version__}')
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand', metavar="", description="Available subcommands for managing S3:")

    config_parser = subparsers.add_parser(
        'config',
        help='Manage the S3 configuration',
        description='Configure various settings such as access credentials, default storage locations, and synchronization options. This command serves as the foundation for tailoring S3Sync to your specific needs, ensuring seamless integration with your workflow.'
    )

    directory = os.getcwd()

    upload_parser = subparsers.add_parser(
        'upload',
        help='Upload directories/files to S3',
        description='Seamlessly upload directories and files to Amazon S3. Whether you\'re backing up important data or distributing assets, this command streamlines the process by securely transferring your content to the cloud. You can define upload options, such as storage classes and encryption, to align with your data management strategies.'
    )

    upload_parser.add_argument("--config", metavar="", help="Local path to the config file", default=directory)
    upload_parser.add_argument("--directory", metavar="", help="Local directory to upload", default=directory)
    upload_parser.add_argument("--s3-bucket", metavar="", help="S3 bucket to upload to", default="")
    upload_parser.add_argument("--s3-prefix", metavar="", help="Prefix to use for S3 object keys", default="")
    upload_parser.add_argument("--exclude", metavar="", nargs='*', help="Exclude files or directories from upload", default=[])
    upload_parser.add_argument("--include", metavar="", nargs="*", help="Include files that startswith '.', '_' from upload.", default=[])
    upload_parser.add_argument("--profile",  metavar="", help="Name of the profile used for AWS S3.", default="default")



    download_parser = subparsers.add_parser(
        'download',
        help='Download directories/files from S3',
        description='Effortlessly retrieve directories and files from Amazon S3 to your local environment. Whether you\'re restoring backups or accessing shared resources, this command simplifies the retrieval process. Customize download preferences such as overwriting rules and filtering to ensure you have the right files where you need them.'
    )

    download_parser.add_argument("--config", metavar="", help="Local path to the config file", default=directory)
    download_parser.add_argument("--s3-bucket", metavar="", help="S3 bucket to download from", default="")
    download_parser.add_argument("--s3-prefix", metavar="", help="Prefix to use for S3 object keys", default="")
    download_parser.add_argument("--directory", metavar="", help="Local directory to save downloaded files", default=directory)
    download_parser.add_argument("--exclude", metavar="", nargs='*', help="Exclude files or directories from download", default=[])
    download_parser.add_argument("--profile", metavar="", help="Name of the profile used for AWS S3.", default="default")


    list_parser = subparsers.add_parser(
        'list',
        help='Handles all list function from Amazon S3 bucket in a structured format.',
        description='Seamlessly hnadle all list functions from Amazon S3 bucket and print it in a pretty structured format, this command streamlines the process by securely handling your content from the cloud.'
    )

    lst_sub = list_parser.add_subparsers(title="List_commands", dest="list_command", metavar="", description="Available subcommands for list:")

    objects_parser = lst_sub.add_parser("objects", help="Print all directories and files from Amazon S3 bucket in a structured format.")

    objects_parser.add_argument("--config", metavar="", help="Local directory to the config file", default=directory)
    objects_parser.add_argument("--s3-bucket", metavar="", help="S3 bucket to download from", default="")
    objects_parser.add_argument("--s3-prefix", metavar="", help="Prefix to use for S3 object keys", default="")
    objects_parser.add_argument("--profile",  metavar="", help="Name of the profile used for AWS S3.", default="default")
    objects_parser.add_argument("--exclude", nargs='*', metavar="", help="Exclude files or directories from download", default=[])


    buckets_parser = lst_sub.add_parser('buckets', help='Print all available buckets from Amazon S3 bucket.')

    buckets_parser.add_argument("--profile",  metavar="", help="Name of the profile used for AWS S3.", default="default")


    delete_parser = subparsers.add_parser(
        'delete',
        help='Handle all deletion process in Amazon S3 bucket.',
        description='Seamlessly handle all deletion function from Amazon S3 bucket, this command streamlines the process by securely deleting your content from the cloud.'
    )

    del_sub = delete_parser.add_subparsers(title="Delete_commands", dest="delete_command", metavar="", description="Available subcommands for delete:")

    del_object_parser = del_sub.add_parser("objects", help="Print all directories and files from Amazon S3 bucket.")

    del_object_parser.add_argument("--config", metavar="", help="Local directory to the config file", default=directory)
    del_object_parser.add_argument("--s3-bucket", metavar="", help="S3 bucket to download from", default="")
    del_object_parser.add_argument("--s3-prefix", metavar="", help="Prefix to use for S3 object keys", default="")
    del_object_parser.add_argument("--profile",  metavar="", help="Name of the profile used for AWS S3.", default="default")
    del_object_parser.add_argument("--exclude", nargs='*', metavar="", help="Exclude files or directories from download", default=[])

    
    del_bucket_parser = del_sub.add_parser('bucket', help='Delete a bucket from Amazon S3.')

    del_bucket_parser.add_argument("--config", metavar="", help="Local directory to the config file", default=directory)
    del_bucket_parser.add_argument("--s3-bucket", metavar="", help="S3 bucket to download from", default="")
    del_bucket_parser.add_argument("--profile",  metavar="", help="Name of the profile used for AWS S3.", default="default")
 

    create_bucket_parser = subparsers.add_parser(
        'create-buckets',
        help='Create all given buckets in Amazon S3.',
        description='Seamlessly create buckets in Amazon S3, this command streamlines the process by securely creating bucket in the cloud. You can define create-buckets options, such as bucket_name and profile, to align with your requirements.'
    )

    create_bucket_parser.add_argument("buckets", nargs="*", metavar="Bucket Names", help="Bucket names with white space seperator.")
    create_bucket_parser.add_argument("--profile",  metavar="", help="Name of the profile used for AWS S3.", default="default")


    sub1 = config_parser.add_subparsers(title="config_commands", dest= "config_command", metavar="", description="Available subcommands for config:")

    sub1.add_parser("init", help="Interactively create config file for S3.")
    conf_list_parser = sub1.add_parser("list", help="List the contents of the AWS S3 config file.")
    set_parser = sub1.add_parser("set", help="Register the key-value in AWS S3 config file.")
    
    set_parser.add_argument("key_value", nargs=2, help="Set or update the config file based on key-value.")
    set_parser.add_argument("--config", metavar="", help="Local path to the S3 config file.", default=directory)
    conf_list_parser.add_argument("--config", metavar="", help="Local path to the S3 config file.", default=directory)
    



    args = parser.parse_args()

    if args.subcommand == "upload":
        upload.s3_upload(args.config, args.directory, args.s3_bucket, args.s3_prefix, args.exclude, args.include,
                         args.profile)
    
    elif args.subcommand == "download":
        download.s3_download(args.config, args.s3_bucket, args.s3_prefix, args.directory, args.exclude,
                             args.profile)


    elif args.subcommand == "list":
        
        if args.list_command == "objects":
            s3_process.list_s3_bucket_objects(args.s3_bucket, args.s3_prefix, args.exclude, args.profile, args.config)
        elif args.list_command == "buckets":
            s3_process.list_s3_buckets(args.profile)


    elif args.subcommand == "delete":

        if args.delete_command == "objects":
            s3_process.delete_s3_bucket_objects(args.s3_bucket, args.s3_prefix, args.exclude, args.profile, args.config)
        elif args.delete_command == "bucket":
            s3_process.delete_s3_bucket(args.s3_bucket, args.profile, args.config)
    

    elif args.subcommand == "create-buckets":
        s3_process.create_s3_bucket(args.buckets, args.profile)

    elif args.subcommand == "config":
        if args.config_command == "init":
            initializer.s3_config()
        
        elif args.config_command == "set":
            s3_process.set_s3_config(args.config, args.key_value[0], args.key_value[1])
        
        elif args.config_command == "list":
            s3_process.list_s3_config(args.config)