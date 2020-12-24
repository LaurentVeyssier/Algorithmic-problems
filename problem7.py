# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 18:38:21 2020

@author: lveys
"""
# A RouteTrieNode with a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, extension, handler):
        # Insert the node
        if extension not in self.children:
            self.children[extension] = RouteTrieNode(handler)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        # input: parts of the path(list)
        node = self.root
        for extension in path_list:
            node.insert(extension, None)
            node = node.children[extension]
        # assign the handler to the leaf corresponding to the path end node
        node.handler = handler

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        if path_list ==['']:
            return self.root.handler
        for extension in path_list:
            if extension in node.children:
                node = node.children[extension]
            else:
                return None
        return node.handler
    
    
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, route):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(route)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # split the path and pass the pass parts as a list to the RouteTrie
        node = self.root
        node.insert(self.split_path(path), handler)
        
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # input path(str) with parts separated by slashes ("/")
        # return None if it's not found or return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        node = self.root
        output = node.find(self.split_path(path))
        if output is None:
            return 'not found handler'
        return output
    
    def split_path(self, path):
        # split the path into parts for the add_handler and loopup functions
        # input path(str) with parts separated by slashes ("/")
        # Return [''] for root inquiry '' or '/'
        # Produce same output with and without trailing slash
        route = path.split('/')
        route = ' '.join(route)
        route=route.strip().split(' ')
        return route




# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # , "not found handler" remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("")) # should print 'root handler'