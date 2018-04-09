#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html
#  
#  Copyright 2018  <pi@raspbari19>
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


import gi								# import PyGObject module
gi.require_version('Gtk', '3.0')		# ensure the correct (viz. 3.0) is available for use
from gi.repository import Gtk			# import the Gtk module

myWindow = Gtk.Window()					# create an empty window
myWindow.connect("destroy", Gtk.main_quit) # attach to delete event queue for window dismissal
myWindow.show_all()						# display window
Gtk.main()								# start Gtk processing loop which is terminated when window is dismissed
