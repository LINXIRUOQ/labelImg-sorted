import time
# 读取文件并处理每一行

# 存储字符及其行号的字典
char_line_mapping = {}
char_line_mapping2 = {}
def 排序(filename, char_line_mapping):
    # 打开文件并读取
    with open(filename, 'r', encoding='utf-8') as file:
        # 用于跟踪字符的索引
        index = 0
        # 按行处理文件中的每一行
        for line in file:
            line = line.strip()  # 去除行首尾的空白字符
            if line:  # 如果行非空
                print(f'行{index}内容：{line}')
                # 将整行内容及其索引位置存储到字典中
                char_line_mapping[line] = index
                index += 1  # 更新行索引
        return char_line_mapping
if __name__ == '__main__':
    filename = rf'C:\Users\67167\Desktop\YOLU\YOLOXUNLIAN\ultralytics-8.3.55\datasets\icon\labels\classes.txt'  # 替换为你的文件路径
    filename2 = rf'C:\Users\67167\Desktop\YOLU\YOLOXUNLIAN\ultralytics-8.3.55\datasets\icon\labels\clasxin.txt'  # 替换为你的文件路径
    排序1 = 排序(filename=filename,char_line_mapping=char_line_mapping)
    print(排序1)
    排序2 =排序(filename=filename2, char_line_mapping=char_line_mapping2)
    print(排序2)

# 输出结果

