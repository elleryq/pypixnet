#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pixnetlib import PixnetOAuth

def main( arg ):
    pixnet=PixnetOAuth()
    print( pixnet.get_users( "elleryq", {} ) )
    print( pixnet.get_album_sets( parameters={'user': 'elleryq' }) )

if __name__ == "__main__":
    main(sys.argv[1:])

