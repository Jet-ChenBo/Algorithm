# 单向循环链表

class Node():
    '''节点'''
    def __init__(self,item):
        self.elem = item
        self.next = None
        
class SingleLinkList():
    '''单向循环链表'''
    def __init__(self, node=None):
        # 头指针
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head is None

    def length(self):
        '''链表长度'''
        if self.is_empty():
            return 0
        # now用来移动遍历节点
        now = self.__head
        # count记录节点个数
        count = 1
        while now.next != self.__head:
            count += 1
            now = now.next
        return count

    def travel(self):
        '''遍历链表'''
        if self.is_empty():
            return
        now = self.__head
        while now.next != self.__head:
            print(now.elem, end='->')
            now = now.next
        # 退出循环时，now指向尾节点
        print(now.elem)
        print('尾节点的下一个：',now.next.elem)

    def add(self, item):
        '''从头部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
            return
        # 找到尾节点
        now = self.__head
        while now.next is not self.__head:
            now = now.next
        # 插入新节点
        node.next = self.__head
        self.__head = node
        # 将尾节点指向node
        now.next = node

    def append(self, item):
        '''从尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            now = self.__head
            while now.next != self.__head:
                now = now.next
            now.next = node
            node.next = self.__head

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
        now.next = node

    def remove(self, item):
        '''删除节点'''
        now = self.__head
        # 如果删除的元素是头
        if now.elem == item:
            # 找到尾节点
            end = self.__head
            while end.next is not self.__head:
                end = end.next
            # 更换新的头节点
            self.__head = self.__head.next
            # 尾节点指向新的头节点
            end.next = self.__head
            return
        # 找到要删除的节点的前一个节点
        while now.next != self.__head and now.next.elem != item:
            now = now.next
        if now.next == self.__head:
            print("没有此节点")
        else:
            now.next = now.next.next
            

    def search(self, item):
        '''查找节点是否存在'''
        if self.is_empty():
            return False 
        now = self.__head
        while now.next is not self.__head:
            if now.elem == item:
                return True
            now = now.next
        # 退出循环时now指向尾节点，仍然需要判断
        return True if now.elem == item else False

single = SingleLinkList()
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
print('删除值为50的节点')
single.remove(50)
single.travel()
