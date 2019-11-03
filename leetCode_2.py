# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x=0
        y=0
        i=0
        times=1
        while l1 is not None:
            x+=l1.val*times
            l1=l1.next
            times*=10
        times=1
        while l2 is not None:
            y+=l2.val*times
            l2=l2.next
            times*=10
        z=x+y
        print(x,y,z)
        result = []
        while z:
            result.append(z % 10)
            z = z // 10
        l3=[0 for i in range(len(result))]
        for i in range(0,len(result)):
            l3[i]=ListNode(result[i])
        for i in range(0,len(result)-1):
            l3[i].next=l3[i+1]
        while (l3[0]):
            print (l3[0].val)
            l3[0]=l3[0].next
        return l3[0]




if __name__=='__main__':
    L11=ListNode(2)
    L12=ListNode(4)
    L13=ListNode(3)
    L21=ListNode(5)
    L22=ListNode(6)
    L23=ListNode(4)
    L11.next=L12
    L12.next=L13
    L21.next=L22
    L22.next=L23
    lisT=Solution()
    l3=ListNode(lisT.addTwoNumbers(L11,L21))
    while (l3):
        print (l3.val)
        l3=l3.next