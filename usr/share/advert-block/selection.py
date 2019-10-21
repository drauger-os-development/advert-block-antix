#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  selection.py
#
#  Copyright 2019 Thomas Castleman <contact@draugeros.org>
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
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class splash(Gtk.Window):
		def __init__(self):
			Gtk.Window.__init__(self, title="antiX Advert Blocker")
			self.grid=Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
			self.add(self.grid)

			self.label = Gtk.Label()
			self.label.set_markup("""Choose your preferred ad blocking service(s)
""")
			self.label.set_justify(Gtk.Justification.LEFT)
			self.grid.attach(self.label, 1, 1, 3, 1)

			self.button = Gtk.CheckButton.new_with_label("adservers.org")
			self.grid.attach(self.button, 1, 2, 3, 1)

			self.button2 = Gtk.CheckButton.new_with_label("mvps.org")
			self.grid.attach(self.button2, 1, 3, 3, 1)

			self.button3 = Gtk.CheckButton.new_with_label("someonewhocares.org")
			self.grid.attach(self.button3, 1, 4, 3, 1)

			self.button4 = Gtk.CheckButton.new_with_label("yoyo.org")
			self.grid.attach(self.button4, 1, 5, 3, 1)

			self.button5 = Gtk.Button.new_with_label("Next -->")
			self.button5.connect("clicked", self.onnextclicked)
			self.grid.attach(self.button5, 3, 8, 1, 1)

			self.button6 = Gtk.Button.new_with_label("Undo Blocking")
			self.button6.connect("clicked", self.onunblockclicked)
			self.grid.attach(self.button6, 2, 8, 1, 1)

			self.button7 = Gtk.Button.new_with_label("Cancel")
			self.button7.connect("clicked", self.oncancelclicked)
			self.grid.attach(self.button7, 1, 8, 1, 1)

		def oncancelclicked(self,widget):
			print("EXIT")
			exit(2)

		def onnextclicked(self,widget):
			print("%s:adservers.org: %s:mvps.org: %s:someonewhocares.org: %s:yoyo.org: " % ((str(self.button.get_active())).upper(),(str(self.button2.get_active())).upper(),(str(self.button3.get_active())).upper(),(str(self.button4.get_active())).upper()))
			exit(0)

		def onunblockclicked(self,widget):
			print("UNBLOCK")
			exit(1)

def show_splash():
	window = splash()
	window.set_decorated(True)
	window.set_resizable(False)
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main()
	window.connect("delete-event", Gtk.main_quit)

show_splash()

