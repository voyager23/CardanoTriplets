#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  adev.py
#  
#  Copyright 2022 mike <mike@pop-os>
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

def is_cardano(a,b,c):
	return (8*a*a*a + 15*a*a +6*a - 27*b*b*c == 1)

def main(args):
	count = 0
	k = 0
	while True:
		
		# positive k
		a = 3*k + 2
		b = k + 1
		c = 8*k + 5
		if is_cardano(a,b,c):
			if a+b+c <= 1000:
				count += 1
				print(a,b,c, is_cardano(a,b,c))
			else:
				break
				
		# negative k
		a = -3*k + 2
		b = -k + 1
		c = -8*k + 5
		if is_cardano(a,b,c):
			if a+b+c <= 1000:
				count += 1
				print(a,b,c, is_cardano(a,b,c))
			else:
				break
		k += 1
	print(count)	
	return 0
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
