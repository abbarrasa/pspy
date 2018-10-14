#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2018 Alberto Buitrago Barrasa <albertusko@northumbria>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from pspy import Database


def main(args):
    Database.connect('store.db')
    Database.createTables()
    
    title = StringCol(length=255, unique=True)
	description = StringCol(length=511)
	comment = StringCol(default=None)
	format = EnumCol(['ISO', 'CSO', 'Eboot'])
	path = StringCol()
    
    
	g = Game(title='Grand Thief Auto Liberty City',
	description='GTA Liberty City',
	format='ISO',
	path='ISOS/GTA')
    Database.close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
