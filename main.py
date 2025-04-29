import os
import time
from 查找新字典索引对应的旧字典的索引 import 排序RS
def 提取数字并修改(filename, dictionary, output_filename):
    # 存储提取的数字
    extracted_numbers = []

    # 打开文件并读取
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # 先读取所有行

    # 新建一个列表，用于存储处理后的行
    new_lines = []

    for line in lines:
        # 将行拆分为单独的部分
        parts = line.split()
        if parts:
            # 获取行首的数字
            first_number = int(parts[0])

            # 如果字典中有对应的值，则替换为字典中的值
            if first_number in dictionary:
                parts[0] = str(dictionary[first_number])  # 替换为字典中的值
                new_lines.append(' '.join(parts) + '\n')  # 将修改后的行加入新列表
            else:
                # 如果字典中没有对应的值，跳过该行，不加入新列表
                continue

    # 将修改后的内容保存到新的文件
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.writelines(new_lines)
def 修改文件夹下所有txt文件(folder_path, dictionary):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):  # 只处理txt文件
            try:
                input_filepath = os.path.join(folder_path, filename)
                output_filename = os.path.join(folder_path, f"{filename}")  # 为修改后的文件命名
                提取数字并修改(input_filepath, dictionary, output_filename)
                print(f"修改后的文件已保存为 {output_filename}")
            except Exception as e:
                print(f'发生错误：{input_filepath}错误：{e}//2s后继续运行')
                time.sleep(2)
if __name__ == '__main__':
    '''
    filename:旧的classes文件（请修改为自己的文件路径）
    filename2：删除掉无用的标签后的新的classes文件（请修改为自己的文件路径）
    folder_path:修改为你存储yolo生成的数据的txt文件夹
    '''
    filename = rf'C:\Users\67167\Desktop\YOLU\YOLOXUNLIAN\ultralytics-8.3.55\datasets\icon\labels\classes.txt'  # 替换为你的文件路径
    filename2 = rf'C:\Users\67167\Desktop\YOLU\YOLOXUNLIAN\ultralytics-8.3.55\datasets\icon\labels\clasxin.txt'  # 替换为你的文件路径
    folder_path = r'C:\Users\67167\Desktop\YOLU\YOLOXUNLIAN\ultralytics-8.3.55\datasets\icon\labels\train2'  # 你的文件夹路径
    dictionary = 排序RS(filename, filename2)
    for key, value in dictionary.items():
        print(f"原索引: {key}, 新索引: {value}")
    print(f'排序完毕5s后将自动执行请确认无误和原文件已备份')
    time.sleep(5)
    # 示例使用
    '''
    dictionary:{原索引：修改后的新索引,原索引：修改后的新索引,原索引：修改后的新索引......}
    '''
    # 调用函数修改文件夹中的所有txt文件
    修改文件夹下所有txt文件(folder_path, dictionary)
    print(f'运行完毕，数据修改完成')

