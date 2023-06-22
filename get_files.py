import os

# def get_files(dir,suffix):
#     res=[]
#     for root,dir,files in os.walk(dir):
#         for filename in files:
#             name,suf=os.path.splitext(filename)
#             if suf == suffix:
#                 res.append(os.path.join(root,filename))
    
#     print(res)

# get_files("./",'.py')


# Solution2
# def pick(obj):
#     if obj.endswith(".py"):
#         print(obj)

# def scan_path(ph):
#     file_list = os.listdir(ph)
#     for obj in file_list:
#         if os.path.isfile(obj):
#             pick(obj)
#         elif os.path.isdir(obj):
#             scan_path(obj)

# if __name__=='__main__':
#     path = input("input your direction:")
#     scan_path(path)

# Solution3  #failed
from glob import iglob

def func(fp,postfix):
    for i in iglob(f"{fp}/**/*{postfix}, recursive=true"):
        print(i)

if __name__ == "__main__":
    postfix = ".py"
    func("c:\Users\Administrator\Documents\My Coding\PyCoding",postfix)