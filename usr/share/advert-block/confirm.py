#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  confirm.py
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
			Gtk.Window.__init__(self, title="antiX Advert Blockers")
			self.grid=Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
			self.add(self.grid)

			self.label = Gtk.Label()
			self.label.set_markup("""
	The <b>antiX Advert Blocker</b> adds stuff to your <b>/etc/hosts</b> file, so
	that many advertising servers and websites will not be able to connect
	to this PC.

	You can choose one service, or combine multiple services for more advert protection.
	Blocking ad servers protects your pricacy, saves you bandwidth, greatly
	improves web-browsing speed, and makes the internet much less annoying in general.

	Do you want to proceed?
	""")
			self.label.set_justify(Gtk.Justification.LEFT)
			self.grid.attach(self.label, 1, 1, 8, 1)

			self.button1 = Gtk.Button.new_with_label("Next -->")
			self.button1.connect("clicked", self.onnextclicked)
			self.grid.attach(self.button1, 8, 2, 1, 1)

			self.button2 = Gtk.Button.new_with_label("Cancel")
			self.button2.connect("clicked", self.oncancelclicked)
			self.grid.attach(self.button2, 1, 2, 1, 1)

		def onnextclicked(self, widget):
			print("CONTINUE")
			exit(0)

		def oncancelclicked(self,widget):
			print("EXIT")
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


