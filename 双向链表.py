# 双向链表

class Node():
    '''节点'''
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None

class DoubleLinkList():
    '''双向链表'''
    def __init__(self, node=None):
        # 头节点
        self.__head = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        # now用来移动遍历节点 
        now = self.__head
        # count记录节点个数
        count = 0
        while now != None:
            count += 1
            now = now.next
        return count

    def travel(self):
        '''遍历链表'''
        now = self.__head
        while now != None:
            if now.prev:   
                print(now.elem,'(前面是',now.prev.elem,')',end='->')
            else:
                print(now.elem,end='->')
            now = now.next

    def add(self, item):
        '''从头部添加元素'''
        node = Node(item)
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def append(self, item):
        '''从尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            now = self.__head
            while now.next != None:
                now = now.next
            now.next = node
            node.prev = now

    def insert(self, pos, item):
        '''在指定位置添加元素'''
        if pos <= 0:
            self.add(item)
            return
        elif pos > self.length()-1:
            self.append(item)
            return
        # 找到pos位置前面的节点
        node = Node(item)
        now = self.__head
        while pos>1:
            now = now.next
            pos -= 1
        node.next = now.next
        now.next.prev = node
        now.next = node
        node.prev = now

    def remove(self, item):
        '''删除节点'''
        now = self.__head
        # 如果删除的元素是头
        if now.elem == item:
            self.__head = self.__head.next
            self.__head.prev = None
            return
        # 找到要删除的节点
        while now != None and now.elem != item:
            now = now.next
        if now == None:
            print("没有此节点")
        else:
            if now.next is not None:
                now.next.prev = now.prev     
            now.prev.next = now.next
                
            

    def search(self, item):
        '''查找节点是否存在'''
        now = self.__head
        while now:
            if now.elem == item:
                return True
            now = now.next
        return False

single = DoubleLinkList()
single.append(20)  # 末尾添加节点
single.append(30)
single.add(40)  # 头部添加节点
single.add(50)
print('链表是否为空：', single.is_empty())
print('链表长度', single.length())
single.travel()
print('\n在第2个位置插入值为80的节点')
single.insert(2,80)
single.travel()
print('\n查找是否存在值为40的节点', single.search(40))
print('删除值为40的节点')
single.remove(40)
single.travel()
        

    
