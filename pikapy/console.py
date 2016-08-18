import argparse
import sys

import pikapy
from pikapy.ptcexceptions import *

from pgoapi import PGoApi
from pgoapi.utilities import f2i
from pgoapi import utilities as util
from pgoapi.exceptions import AuthException, ServerSideRequestThrottlingException
import pprint
import time
import threading
import getopt
import user


def parse_arguments(args):
    """Parse the command line arguments for the console commands.
    Args:
      args (List[str]): List of string arguments to be parsed.
    Returns:
      Namespace: Namespace with the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description='Pokemon Trainer Club Account Creator'
    )
    parser.add_argument(
        '-u', '--username', type=str, default=None,
        help='Username for the new account (defaults to random string).'
    )
    parser.add_argument(
        '-p', '--password', type=str, default=None,
        help='Password for the new account (defaults to random string).'
    )
    parser.add_argument(
        '-e', '--email', type=str, default=None,
        help='Email for the new account (defaults to random email-like string).'
    )
    parser.add_argument(
        '-b', '--birthday', type=str, default=None,
        help='Birthday for the new account. Must be YYYY-MM-DD. (defaults to a random birthday).'
    )
    parser.add_argument(
        '-s','--start', type=int,default=1,
        help='Start of the Username Range.'
    )
    parser.add_argument(
        '-c','--count', type=int,default=1,
        help='Count Users to be created.'
    )
    parser.add_argument(
        '-a','--api', type=str,default=None,
        help='Insert 2Captcha API Key here.'
    )
    parser.add_argument(
        '-hl','--headless', type=int,default=0,
        help='Needed when on a headless Linux server!.'
    )

    return parser.parse_args(args)


def entry():
    """Main entry point for the package console commands"""
    args = parse_arguments(sys.argv[1:])
    for x in range(args.start,args.start+args.count):
        try:
            user = args.username + str(x)
            plusmail = args.email.split("@")[0]+"+"+user+"@"+args.email.split("@")[1]
            account_info = pikapy.random_account(user, args.password, plusmail, args.birthday, args.api, args.headless)
            
            print('  Username:  {}'.format(account_info["username"]))
            print('  Password:  {}'.format(account_info["password"]))
            print('  Email   :  {}'.format(account_info["email"]))
            print('\n')
            
            # Accept Terms Service
            
            accept_tos(account_info["username"], account_info["password"])
            # Append usernames 
            with open("usernames.txt", "a") as ulist:
                ulist.write(account_info["username"]+":"+account_info["password"]+"\n")
                ulist.close()
        # Handle account creation failure exceptions
        except PTCInvalidPasswordException as err:
            print('Invalid password: {}'.format(err))
        except (PTCInvalidEmailException, PTCInvalidNameException) as err:
            print('Failed to create account! {}'.format(err))
        except PTCException as err:
            print('Failed to create account! General error:  {}'.format(err))

def accept_tos(username, password):
    flag = False
    while not flag:
        try:
            api = PGoApi()
            #Set spawn to NYC
            api.set_position(49.4536783, 11.077678699999979, 299.0)
            api.login('ptc', username, password)
            time.sleep(0.5)
            req = api.create_request()
            req.mark_tutorial_complete(tutorials_completed = 0, send_marketing_emails = False, send_push_notifications = False)
            response = req.call()
            print('Accepted Terms of Service for {}'.format(username))
            flag = True
        except ServerSideRequestThrottlingException:
            print('This happens, just restart')
