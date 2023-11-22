from __future__ import absolute_import

from brainvisa.processes import *


name = 'Print Something'
userLevel = 0

signature = Signature(
    'message', String(),
)

def execution(self, context):
    print(self.message)
