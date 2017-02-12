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
from utilities import Utilities


class AStar(object):
    def __init__(self):
        pass

    def search(self, root):

        frontier = []
        visited = []
        paths = []

        frontier.append(root)
        while len(frontier) > 0:
            current_node = frontier.pop()
            if current_node.is_goal():
                return current_node
            if not self.is_node_in_list(current_node, visited):
                for node, path_cost in current_node.get_neighbours():
                    if not self.is_node_in_list(node, visited):
                        cost = self.path_cost(node, paths)
                        paths.append({"current_node": current_node, "node": node, "cost": cost, "status": 'open'})
                min_cost = 9999
                min_node = None
                index = 0
                min_index = 0
                print(paths)
                for item in paths:
                    print("current_node: %s, node: %s, cost: %s, status: %s" % (
                        item['current_node'].get_name(), item['node'].get_name(), item['cost'], item['status']))
                    if min_cost > cost and item['status'] == "open":
                        min_cost = cost
                        min_index = index
                        min_node = item['node']
                    index += 1

                print("min_node: %s, min_cost: %s, min_index: %s" % (min_node.get_name(), min_cost, min_index))

                '''
                if not self.is_node_in_list(min_node, frontier):
                    paths[min_index]['status'] = 'visited'
                    frontier.append(min_node)
                visited.append(current_node)
                '''

    def path_cost(self, node, path):
        print("node: " + node.get_name())
        total_cost = 0
        for item in path:
            # if item['status'] == 'visited':
            for n, cost_path in item['node'].get_neighbours():
                print("cost_path: " + cost_path)
                # print(n.get_name())
                if n.get_name() == node.get_name():
                    print("node:" + n.get_name())
                    total_cost = total_cost + cost_path

        total_cost = total_cost + node.get_heuristic()
        print(total_cost)
        return total_cost

    def total_cost_so_far(self, current_node, path):
        if len(path) == 0:
            return 0
        elif len(path) == 1:
            cost = 0
            for n, path_cost in path[0].get_neighbours():
                if n.get_name() == current_node.get_name():
                    cost = cost + path_cost
            return cost
        else:
            i = 0
            cost = 0
            for n in path:
                if i < len(path) - 1:
                    for node, path_cost in path[i].get_neighbours():
                        if node.get_name() == path[i + 1].get_name():
                            cost = cost + path_cost
                i = i + 1
            return cost
