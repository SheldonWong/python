'''
#面向对象

class TreeNode():
    
    def __init__(self,data):
        
        self.left = None
        self.data = data
        self.right = None   

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
print(root.data,root.left.data,root.right.data)
'''

# 嵌套字典
myTree = {'no surfacing':           #root
                        {'1':       #left subtree
                                {'flippers': 
                                    {'1': 'yes', 
                                    '0': 'no'}
                                }, 

                        '0': 'no'   #right subtree
                        }
            }
#print(myTree)
import json 

print(json.dumps(myTree, indent=4))

'''
def list_all_dict(dict_a):
    if isinstance(dict_a,dict) : #使用isinstance检测数据类型
        for x in range(len(dict_a)):
            temp_key = list(dict_a.keys())[x]
            temp_value = dict_a[temp_key]
            print(' '*x*4+"%s=>%s" %(temp_key,temp_value))
            list_all_dict(temp_value) #自我调用实现无限遍历

def myprint(d):
  for k, v in d.items():
    if isinstance(v, dict):
        print(k,"==>",v)
        myprint(v)
    else:
        print("{0} : {1}".format(k, v))
myprint(myTree)
#list_all_dict(myTree)
'''


'''
请注意，我们可以使用索引来访问列表的子树。
树的根是myTree[0]，根的左子树是myTree[1]，右子树是myTree[2]。
下面的代码说明了如何用列表创建简单树。一旦树被构建，我们可以访问根和左、右子树。
嵌套列表法一个非常好的特性就是子树的结构与树相同，本身是递归的。
子树具有根节点和两个表示叶节点的空列表。列表的另一个优点是它容易扩展到多叉树。
在树不仅仅是一个二叉树的情况下，另一个子树只是另一个列表。
'''

#嵌套列表
'''
myTree = ['a',   #root
                ['b',  #left subtree
                    ['d' [], []],
                    ['e' [], []] 
                ],

                ['c',  #right subtree
                    ['f' [], []],
                    [] 
                ]
        ]
'''