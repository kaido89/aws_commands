#!/usr/bin/env python3
import boto3


def main():
    profile_name = input('*** Requirement **** AWS profile name: ')
    session=boto3.session.Session(profile_name=profile_name)
    print('*** SUCCESS *** The session '+profile_name+' was created')
    return session


main()
