#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pixnetlib import Pixnet

def main( arg ):
    pixnet=Pixnet()
    print( pixnet.get_users_elleryq() )
    print( pixnet.get_album_sets( {'user': 'elleryq' }) )

if __name__ == "__main__":
    main(sys.argv[1:])

