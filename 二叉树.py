class Node():
    '''节点'''
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree():
    '''二叉树'''
    def __init__(self):
        self.root = None

    def add(self, item):
        '''添加节点'''
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        quene = [self.root]
        '''
        从根节点开始找位置，如果根节点有左孩子就将它的左孩子添加到列表，右孩子一样，然后从它的
        孩子开始继续找，直到找到一个节点没有左孩子或者右孩子，就将node添加到此位置
        '''
        while quene:
            cur_node = quene.pop(0)
            # 如果节点没有左孩子，就将node添加为左孩子
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            # 否则，将节点的左孩子添加到列表中，以便下次遍历它的子节点
            else:
                quene.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                quene.append(cur_node.rchild)

    def breadth_travel(self):
        '''广度遍历(层次遍历)'''
        if self.root is None:
            return
        quene = [self.root]
        while quene:
            cur_node = quene.pop(0)
            print(cur_node.elem, end='->')
            if cur_node.lchild is not None:
                quene.append(cur_node.lchild)
            if cur_node.rchild is not None:
                quene.append(cur_node.rchild)

    def 

    def pre_travel(self, node):
        '''先序遍历'''
        if node is None:
            return
        print(node.elem, end='->')
        self.pre_travel(node.lchild)
        self.pre_travel(node.rchild)

    def mid_travel(self, node):
        '''中序遍历'''
        if node is None:
            return
        self.mid_travel(node.lchild)
        print(node.elem, end='->')
        self.mid_travel(node.rchild)

    def last_travel(self, node):
        '''后序遍历'''
        if node is None:
            return
        self.last_travel(node.lchild)
        self.last_travel(node.rchild)
        print(node.elem, end='->')


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3) 
    tree.add(4)
    tree.add(5)
    print('广度遍历：', end='')
    tree.breadth_travel()
    print('\n先序遍历：', end='')
    tree.pre_travel(tree.root)
    print('\n中序遍历：', end='')
    tree.mid_travel(tree.root)
    print('\n后序遍历：', end='')
    tree.last_travel(tree.root)
        
