#!/usr/bin/env python3

# NAME: target_sender_module.py
# PURPOSE: randomly generating and sending Target commands upon keypress
# AUTHOR: Emma Bethel

import os
import random
import robomodules as rm
from messages import MsgType, message_buffers, Target

# retrieving address and port of robomodules server (from env vars)
ADDRESS = os.environ.get("LOCAL_ADDRESS","localhost")
PORT = os.environ.get("LOCAL_PORT", 11295)

FREQUENCY = 1

TARGET_PAIRS = [ # color, shape
    (3, 3), (0, 0), (1, 2), (3, 1), (3, 0), (0, 2), (0, 3), (2, 1), (1, 1), (3, 2)
]


class TargetSenderModule(rm.ProtoModule):
    # sets up the module (subscriptions, connection to server, etc)
    def __init__(self, addr, port):
        self.subscriptions = []
        super().__init__(addr, port, message_buffers, MsgType, FREQUENCY, self.subscriptions)

    # runs every time one of the subscribed-to message types is received
    def msg_received(self, msg, msg_type):
        pass

    # runs every 1 / FREQUENCY seconds
    def tick(self):
        input().lower()
        
        target = random.choice(TARGET_PAIRS)
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
