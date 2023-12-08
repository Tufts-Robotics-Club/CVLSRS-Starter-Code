#!/usr/bin/env python3

# NAME: target_sender_module.py
# PURPOSE: randomly generating and sending Target commands upon keypress
# AUTHOR: Emma Bethel

import os
import random
from copy import deepcopy
import robomodules as rm
from messages import MsgType, message_buffers, Target

# retrieving address and port of robomodules server (from env vars)
ADDRESS = os.environ.get("LOCAL_ADDRESS","localhost")
PORT = os.environ.get("LOCAL_PORT", 11295)

FREQUENCY = 1

TARGET_PAIRS = [  # color, shape
    (0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)
]


class TargetSenderModule(rm.ProtoModule):
    # sets up the module (subscriptions, connection to server, etc)
    def __init__(self, addr, port):
        self.subscriptions = []
        super().__init__(addr, port, message_buffers, MsgType, FREQUENCY, self.subscriptions)

        self.target_pairs = []

    # runs every time one of the subscribed-to message types is received
    def msg_received(self, msg, msg_type):
        pass

    # runs every 1 / FREQUENCY seconds
    def tick(self):
        input().lower()

        if len(self.target_pairs) == 0:
            self.target_pairs = deepcopy(TARGET_PAIRS)
        
        target = random.choice(self.target_pairs)
        self.target_pairs.remove(target)

        msg = Target()
        msg.shape = target[1]
        msg.color = target[0]


        self.write(msg.SerializeToString(), MsgType.TARGET)
        print('sent', msg)
        

def main():
    print('press enter to send a target message!')
    module = TargetSenderModule(ADDRESS, PORT)
    module.run()


if __name__ == "__main__":
    main()
