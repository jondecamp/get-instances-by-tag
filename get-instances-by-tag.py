#!/usr/bin/env python
import boto3
import operator
import getopt
import sys

report = []
reverse = False
tag_key = 'Owner'
help_message = 'get-instances-by-tag.py [-k <tag key to sort by>]'

def main(argv):
    global reverse
    global tag_key
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.all()

    try:
        opts, args = getopt.getopt(argv,"rhk:", ["key="])
    except getopt.GetoptError:
        print help_message
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print help_message
            sys.exit()
        elif opt in ("-k", "--key"):
            tag_key = arg
        elif opt in ("-r"):
            reverse = True

    output(gen_report(instances))

def get_tag_value(instance_tags, key):
    value = 'unknown'
    for tag in instance_tags:
        if tag['Key'] == key:
            value = tag['Value']
    return value

def gen_report(instances):
    for instance in instances:
        instance_info = {
            "id": instance.id,
            "launch_time": instance.launch_time,
            "instance_type": instance.instance_type,
            tag_key: get_tag_value(instance.tags, tag_key)
        }
        report.append(instance_info)
    return report

def output(input):
    input.sort(key=operator.itemgetter(tag_key), reverse=reverse)
    for i in input:
        print("%-10s %-19s %-8s %s" % (i[tag_key], i['id'], i['instance_type'], i['launch_time']))
    return

main(sys.argv[1:])
