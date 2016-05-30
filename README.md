# get-instances-by-tag
Python script to report instances by tag key.

### Usage
Run the script without any arguments and it will query for EC2 instances, and sort them by the _Owner_ tag.

`$ get-instances-by-tag.py`

Optionally, you can pass in `-k` or `--key` to sort by a different tag key.  And finally, you can use `-r` to reverse
the sort order.

### Configuration
This script uses boto3, and you can override the credentials using environment variables
([Boto3 Github Configuration](http://boto3.readthedocs.io/en/latest/guide/configuration.html))
