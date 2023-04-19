import sys
sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, key, x):
        self.key = key
        self.x = x
        self.right, self.left = None, None


class Tree:
    def __init__(self, head, x):
        self.head = Node(head, x)

    def make_tree(self, key, x):
        cur_node = self.head

        while True:
            if cur_node.x > x:
                if cur_node.left is None:
                    cur_node.left = Node(key, x)
                    break
                else:
                    cur_node = cur_node.left

            elif cur_node.x < x:
                if cur_node.right is None:
                    cur_node.right = Node(key, x)
                    break
                else:
                    cur_node = cur_node.right

    def preorder(self):
        res = []

        def order(node):
            nonlocal res
            res.append(node.key)
            if node.left is not None:
                order(node.left)
            if node.right is not None:
                order(node.right)
        order(self.head)
        return res

    def postorder(self):
        res = []

        def order(node):
            nonlocal res
            if node.left is not None:
                order(node.left)
            if node.right is not None:
                order(node.right)
            res.append(node.key)
        order(self.head)
        return res


def solution(nodeinfo):
    answer = []
    for i in range(len(nodeinfo)):
        nodeinfo[i] = [i + 1] + nodeinfo[i]

    nodeinfo.sort(key=lambda x: x[2], reverse=True)

    tree = Tree(nodeinfo[0][0], nodeinfo[0][1])

    for i in nodeinfo[1:]:
        tree.make_tree(i[0], i[1])

    answer.append(tree.preorder())
    answer.append(tree.postorder())

    return answer


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
