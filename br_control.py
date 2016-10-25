#!/usr/bin/env python
# --*-- coding:utf-8 --*--
#
# Copyright 2016.
#
# Authors: JhonRoun <jhonroun@yandex.ru>
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of either or both of the following licenses:
#
# 1) the GNU Lesser General Public License version 3, as published by the 
# Free Software Foundation; and/or
# 2) the GNU Lesser General Public License version 2.1, as published by 
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the applicable version of the GNU Lesser General Public 
# License for more details.
#

import pygtk
pygtk.require('2.0')
import gtk
import subprocess


# Удобные функции


class RangeWidgets:
    
    def getCurrentBrightness(self):
        return int(float(subprocess.check_output("xrandr --verbose | grep -i brightness | cut -f2 -d ' '", shell=True).split('\n')[0])* 100)
 
    def scale_moved(self, event):
        cmd = "xrandr --output DSI1 --brightness %.2f" % (float(self.hscale.get_value())/100)
        cmdStatus = subprocess.check_output(cmd, shell=True)

   
    # Создаём окно

    def __init__(self):
        # Стандартное создание окна
        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", lambda w: gtk.main_quit())
        self.window.set_title("Управление яркостью")
        currB = self.getCurrentBrightness()		
		
     #   box1 = gtk.VBox(False, 0)
      #  self.window.add(box1)
      #  box1.show()

        box2 = gtk.HBox(False, 10)
        box2.set_border_width(10)
     #   box1.pack_start(box2, True, True, 0)
        box2.show()
        adj1 = gtk.Adjustment(currB, 0, 100, 1, 10, 0)
      

        box3 = gtk.VBox(False, 10)
        box2.pack_start(box3, True, True, 0)
        box3.show()

        # Повторно используем этот же регулятор
        self.hscale = gtk.HScale(adj1)
        self.hscale.set_size_request(200, 30)
        self.hscale.connect("value-changed", self.scale_moved)
        box3.pack_start(self.hscale, True, True, 0)
        self.hscale.show()
        self.window.add(box2)
        box2 = gtk.HBox(False, 10)
        box2.set_border_width(10)
     #   box1.pack_start(box2, True, True, 0)
        box2.show()


        self.window.show()

def main():
    gtk.main()
    return 0            

if __name__ == "__main__":
    RangeWidgets()
    main()
