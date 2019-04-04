#!/usr/bin/env python

import logging, os
logging.getLogger().setLevel(level=os.environ.get("LOGLEVEL", "INFO"))
logging.getLogger().addHandler(logging.StreamHandler())

from i4t.core.instancing import InstancingToken, InstancingWarrant
from i4t.core.provisioning import ProvisioningToken, ProvisioningWarrant

from i4t.cli.config import Config

import fire

class Pipeline(object):

  def __init__(self):
    self.itoken = InstancingToken()
    self.iwarrant = InstancingWarrant()
    self.ptoken = ProvisioningToken()
    self.pwarrant = ProvisioningWarrant()
    self.config = Config()

fire.Fire(Pipeline)
