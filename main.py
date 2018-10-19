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

from pspy import Settings, Database, Game


def main(args):
    settings = Settings()

    db_filename = settings.read().get('Database', 'file')
    print("El fichero es: " + db_filename)
    database = Database()
    database.connect(db_filename)
    database.createSchema()
    g = Game(
        title='Grand Thief Auto Liberty City10',
        description='GTA Liberty City',
        size=48306354,
        format='CSO',
        path='ISOS/GTA.zip'
    )
    size = g.humanReadableSize()
    print("El tamano es: " + size)
    a = id(g.id)
    print(a)
    print('The hash is: ')
    database.close()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
