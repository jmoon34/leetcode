# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
# 
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
# 
# Example 1:
# 
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7



def merge_two_rec(t1, t2):
    def recurse(n1, n2):
        if not n1 and not n2:
            return None
        if n1 and not n2:
            return n1
        if not n1 and n2:
            return n2
        n1.val += n2.val
        n1.left = recurse(n1.left, n2.left)
        n1.right = recurse(n1.right, n2.right)
        return n1
    return recurse(t1, t2)


# dfs using stack.  We change everything in t1 and connect it to parts of t2 where t1 is missing
def merge_two_iter(t1, t2):
    if not t1 and not t2:
        return None
    if t1 and not t2:
        return t1
    if not t1 and t2:
        return t2
    s1, s2 = [t1], [t2]
    while s1 and s2:
        c1, c2 = s1.pop(), s2.pop()
        c1.val += c2.val
        if c1.left and c2.left:
            s1.append(c1.left)
            s2.append(c2.left)
        elif not c1.left and c2.left:
            c1.left = c2.left
        if c1.right and c2.right:
            s1.append(c1.right)
            s2.append(c2.right)
        elif not c1.right and c2.right:
            c1.right = c2.right
    return t1

# We can make the method above more concise by using 1 stack
def merge_two_iter_better(t1, t2):
    if not t1 and not t2:
        return None
    if t1 and not t2:
        return t1
    if not t1 and t2:
        return t2
    stack = [(t1, t2)]
    while stack:
        c = stack.pop()
        c[0].val += c[1].val
        if c[0].left and c[1].left:
            stack.append((c[0].left, c[1].left))
        elif not c[0].left and c[1].left:
            c[0].left = c[1].left
        if c[0].right and c[1].right:
            stack.append((c[0].right, c[1].right))
        elif not c[0].right and c[1].right:
            c[0].right= c[1].right
    return t1
