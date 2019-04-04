#!/usr/bin/env python

import logging, os
logging.getLogger().setLevel(level=os.environ.get("LOGLEVEL", "INFO"))
logging.getLogger().addHandler(logging.StreamHandler())

from i4t.core.instancing import InstancingToken, InstancingWarrant
from i4t.core.provisioning import ProvisioningToken, ProvisioningWarrant

from i4t.cli.config import Config

import argparse

def main(args):
  config = Config()
  if args.application:
    # make application
    application = args.application
    iwarrant, pwarrant = config.load_project_application(application)
    # TODO merge contents
    iwarrant = InstancingWarrant.generate(application)
    pwarrant = ProvisioningWarrant()
    pwarrant.add_token_generate_mqtt(args.host, args.port, args.channel)
    config.save_project_application(application, iwarrant, pwarrant)
  if args.client:
    # make client
    client = args.client
    application = args.application
    iwarrant, pwarrant = config.load_project_client(client)
    # TODO merge contents
    iwarrant = InstancingWarrant.generate(client)
    pwarrant = ProvisioningWarrant()
    pwarrant.add_token_generate_mqtt(args.host, args.port, args.channel)
    print(pwarrant)
    print(pwarrant.protobuf)
    config.save_project_client(client, iwarrant, pwarrant)

def parse_args():
  examples="""
Examples:
  provisioning_factory.py
"""
  # add args
  parser = argparse.ArgumentParser(epilog=examples, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('-a', dest='application', type=str, help='Name of application')
  parser.add_argument('--host', dest='host', type=str, help='Application host')
  parser.add_argument('--port', dest='port', type=int, help='Application port')
  parser.add_argument('--channel', dest='channel', type=str, help='Application channel')
  parser.add_argument('-c', dest='client', type=str, help='Name of client')

  # parse args
  args = parser.parse_args()
  return args

if __name__ == '__main__':
  main(parse_args())
