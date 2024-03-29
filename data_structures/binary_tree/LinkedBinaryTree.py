import ArrayQueue

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return 1 + left_count + right_count


    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return subtree_root.data + left_sum + right_sum


    def height(self):
        if(self.is_empty()):
            raise Exception("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    def subtree_height(self, subtree_root):
        if ((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif ((subtree_root.left is not None) and (subtree_root.right is None)):
            return 1 + self.subtree_height(subtree_root.left)
        elif ((subtree_root.left is None) and (subtree_root.right is not None)):
            return 1 + self.subtree_height(subtree_root.right)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue.ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)


    def __iter__(self):
        for node in self.postorder():
            yield node.data


def min_and_max(bin_tree):
    if bin_tree.is_empty():
        raise EmptyTree("Tree is Empty.")
    else:
        node = bin_tree.root
        min_and_max = min_and_max_helper(node)
        return (min_and_max[0], min_and_max[1])

def min_and_max_helper(node):
    if node == None:
        pass
    elif node.left == None and node.right == None:
        if node.data > max:
            max = node.data
        if node.data < min:
            min = node.data
        return (min, max)
    else:
        if node.left != None:
            min_and_max = min_and_max_helper(node.left)
        if node.data > min_and_max[1]:
            max = node.data
        if node.data < min_and_max[0]:
            min = node.data


        if node.right != None:
            min_and_max = min_and_max_helper(node.right)
        if node.data > min_and_max[1]:
            max = node.data
        if node.data < min_and_max[0]:
            min = node.data

        return (min, max)


def main():
    tree = LinkedBinaryTree()
    tree.root = LinkedBinaryTree.Node(3)
    tree.root.right = LinkedBinaryTree.Node(7)
    tree.root.right.right = LinkedBinaryTree.Node(4)
    tree.root.right.left = LinkedBinaryTree.Node(8)
    tree.root.left = LinkedBinaryTree.Node(2)
    tree.root.left.left = LinkedBinaryTree.Node(9)
    tree.root.left.left.left = LinkedBinaryTree.Node(5)
    tree.root.left.left.right = LinkedBinaryTree.Node(1)
    tree.size = 9
    print(min_and_max(tree))