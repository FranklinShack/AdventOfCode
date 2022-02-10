import sys, getopt
import re, functools
from readFile import readFile
from aocd import submit

def main(argv):
    L=[]
    usage=("Usage: "+sys.argv[0]+' {-p -s}')
    try:
        opts, args = getopt.getopt(argv, "hps")
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            return 0
        elif opt == '-p':
            L = readFile("puzzleInput.txt")
        elif opt == '-s':
            L = readFile("sampleInput.txt")
    solut=sol(L)
    print(solut)
    #submit(solut)

    return 0

class Tree_structure:
   def __init__(self, data=None):
      self.key = data
      self.children = []

   def set_root_node(self, data):
      self.key = data

   def add_vals(self, node):
      self.children.append(node)

   def search_val(self, key):
      if self.key == key:
         return self
      for child in self.children:
         temp = child.search(key)
         if temp is not None:
            return temp
      return None

   def count_leaf_node(self):
      leaf_nodes = []
      self.count_leaf_node_helper_fun(leaf_nodes)
      return len(leaf_nodes)

   def count_leaf_node_helper_fun(self, leaf_nodes):
    if self.children == []:
        leaf_nodes.append(self)
    else:
        print(len(self.children))
        for child in range(len(self.children)):
            self.children[child].count_leaf_node_helper_fun(leaf_nodes)





def findPaths(L, start, paths, visited):

    visited=[start] if (ord(start)>96 and ord(start)<123) else []

    for i in L:
        if i[0] == start and start not in visited:
            if i[1] == "end":
                return Tree_structure("end")

            if ord(i[1])>96 and ord(i[1])<123:
                visited.append(i[1])
            child = Tree_structure(i[1])
            child.children = findPaths(L, i[1], [], visited)
            paths.append(child)
                
    return paths


def sol(L):
    paths=Tree_structure("start")
    for i in range(len(L)):
        if L[i][0]=="start":
            child = Tree_structure(L[i][1])
            child.children = findPaths(L, L[i][1], [], [])
            paths.children.append(child)

    return paths.count_leaf_node()

if __name__ == "__main__":
   main(sys.argv[1:])