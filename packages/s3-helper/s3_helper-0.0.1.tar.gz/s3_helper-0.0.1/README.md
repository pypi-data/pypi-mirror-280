# S3-Manager

The S3-Manager helps developer to easily access file from S3 bucts or Minio buckets. This can handle multiple operation like 'upload', 'download', 'list_files in a bucket' and many other operation.

## Installation
```
pip install s3-manager
```

## Usage:
### Creating AWS config:
```
S3 config init
```

### Show all available Profiles in AWS config:
```
S3 config list profile
```

### Update AWS config:
```
S3 config set <config key> <value> --profile <your profile>
```
Example:
```
S3 config set region us-west-1 --profile default
```

### Locally Save the AWS config:
```
S3 config save --profile <your profile>
```

### Remove a Profile from AWS config:
```
S3 config remove --profile <your profile>
```

### Show the contents of AWS config:
```
S3 config list --profile <your profile>
```
## Local S3 Usage:
### Create local config for S3:
```
s3 config init
```
### Update local config of S3:
```
s3 set <config key> <value>
```

### Show the contents of local S3 config:
```
s3 config list
```

### Creating Buckets in S3:
```
s3 create-bucket --bucket <bucket name> --profile <your profile>
```

### Show All Buckets in S3:
```
s3 list buckets --profile <your profile>
```

### Remove Buckets in S3:
```
s3 delete bucket --bucket <bucket name> --profile <your profile>
```

### Show Bucket Objects in S3:
```
s3 list objects --bucket <bucket name> --prefix <prefix in s3> --exclude <exclude list>
```

### Remove objects in S3:
```
s3 delete objects --bucket <bucket name> --prefix <prefix in s3> --exclude <exclude list>
```

### Upload files to S3 Bucket:
```
s3 upload --bucket <bucket name> --prefix <prefix in s3> --exclude <exclude list> --include <include list>
```

### Downlad files from S3 Bucket:
```
s3 download --bucket <bucket name> --prefix <prefix in s3> --exclude <exclude list>
```

