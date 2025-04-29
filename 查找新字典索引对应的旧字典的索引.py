import time

from 读取class获取行 import 排序

# 存储字符及其行号的字典
char_line_mapping = {}
char_line_mapping2 = {}

def 排序RS(filename,filename2):
    列表 = {}
    列表2 = {}
    print(f'------------------------------------------filename------------------------------------------')
    排序2 = 排序(filename=filename, char_line_mapping=列表)
    print(f'------------------------------------------filename2------------------------------------------')
    排序1 = 排序(filename=filename2, char_line_mapping=列表2)
    # 新字典，保存结果
    new_dict = {}
    for key in 排序2:
        print(f'2中查找的元素为{key}')
        if key in 排序1:
            print(f'值{key}对应的远索引为{排序2[key]}')
            print(f'值{key}对应的新索引为{排序1[key]}')
            new_dict[排序2[key]] = 排序1[key]
            print(' ')
            print(' ')
            print(' ')
    print(new_dict)
    return new_dict
def yanzheng(filename,char_line_mapping):
    char_line_mapping = {}
    char_line_mapping2 = {}
    排序2 = 排序(filename=filename, char_line_mapping=char_line_mapping)
    排序1 = 排序(filename=filename2, char_line_mapping=char_line_mapping2)
    bianliang = 'cz'
    if bianliang in 排序2:
        print(f'查找{bianliang}的值对应的的索引为{排序2[bianliang]}')
    if bianliang in 排序1:
        print(f'查找{bianliang}的值对应的1中的索引为{排序1[bianliang]}')
    time.sleep(1)
# 遍历第二个字典，提取共同的键
# 打印新字典

if __name__ == '__main__':
    filename = rf'C:\Users\67167\Desktop\YOLU\YOLOXUNLIAN\ultralytics-8.3.55\datasets\icon\labels\classes.txt'  # 替换为你的文件路径
    filename2 = rf'C:\Users\67167\Desktop\YOLU\YOLOXUNLIAN\ultralytics-8.3.55\datasets\icon\labels\clasxin.txt'  # 替换为你的文件路径
    排序RS(filename,filename2)