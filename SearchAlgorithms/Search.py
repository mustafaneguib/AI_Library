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

from queue import *


class Search(object):
    def __init__(self):
        pass

    def astar(self):

        pass

    def bfs(self, root):
        '''
        Breadth First Search algorithm
        :param root: root node
        :return: the goal node
        '''
        visited = []
        q = Queue(maxsize=0)
        q.put(root)
        visited.append(root)
        while not q.empty():
            current_node = q.get()
            print("-->" + current_node.get_name())
            if current_node.is_goal():
                return current_node
            for node, heuristic in current_node.get_neighbours():
                if self.is_node_in_list(node, visited) == False:
                    visited.append(node)
                    q.put(node)

    def dfs(self):
        pass

    def is_node_in_list(self, node, list):
        '''
        This function checks if the given node is in the provided list
        :param node:
        :param list:
        :return: return True or False
        '''
        found_node = False
        for n in list:
            if n.get_name() == node.get_name():
                found_node = True
                break

        if found_node:
            return True
        else:
            return False

