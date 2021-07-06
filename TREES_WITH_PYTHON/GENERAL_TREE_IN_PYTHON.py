class Treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def print(self):
        spaces=" "*self.get_level()
        prefix=spaces+"|__"if self.parent else ""
        print(prefix+self.data)
        for child in self.children:
            child.print()

def build_ds_tree():
    root=Treenode("DS")
    primitive=Treenode("PRIMITIVE")
    nonprimitive=Treenode("NON-PRIMITIVE")
    root.add_child(primitive)
    root.add_child(nonprimitive)
    root.print()

build_ds_tree()



# class Treenode:
#     def __init__(self,data):
#         self.data=data
#         self.children=[]
#         self.parent=None

#     def add_child(self,child):
#         child.parent=self
#         self.children.append(child)

#     def print(self):
#         # space=' '*self.get_level()*5 
#         space=' '*self.get_level()*5 
#         prefix=space+"|__"if self.parent else ""
#         print(prefix,self.data,self.get_level())
#         for child in self.children:
#             # print(child.data)
#             child.print()
    
#     def get_level(self):
#         level=0   
#         p=self.parent
#         while p:
#             level+=1
#             p=p.parent
#         return level  

# def build_ds_tree():
#     root=Treenode("DS")
    
#     primitive=Treenode("Primitive")          
#     nonprimitive=Treenode("Non-Primitive") 

#     inttype=Treenode("intger")
#     floattype=Treenode("float")
#     chartype=Treenode("character")

#     primitive.add_child(inttype)
#     primitive.add_child(floattype)
#     primitive.add_child(chartype)

#     root.add_child(primitive)        
#     root.add_child(nonprimitive)     
#     root.print() 
# build_ds_tree()  