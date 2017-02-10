'''
    Copyright (C) 2017  Mustafa Neguib. This project is an Open Source Artificial Intelligence
    Library.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    {project}  Copyright (C) {year}  {fullname}
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
'''

class Node(object):
    '''
    This class is the description of a node in a
    network.
    '''


    def __init__(self,id,name,neighbours,heuristic,goal):
        '''

        :param id: this is the identifying number, usually a number
        :param name: this is the name given to the node, usually a string
        :param neighbours: this is a list of neighbours the node
        :param heuristic: this is usually a numeric value such as the straight line distance to goal node
        :param goal: this is a boolean variable, and tells whether the node is a goal node or not
        '''
        self.id=id
        self.name=name
        self.neighbours=neighbours
        self.heuristic=heuristic
        self.goal=goal

    def set_id(self,id):
        self.id=id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name=name

    def get_name(self):
        return self.name

    def set_neighbours(self, neighbours):
        self.neighbours=neighbours

    def get_neighbours(self):
        return self.neighbours

    def set_heuristic(self,heuristic):
        self.heuristic=heuristic

    def get_heuristic(self):
        return self.heuristic

    def set_is_goal(self,is_goal):
        self.is_goal=is_goal

    def is_goal(self):
        return self.goal