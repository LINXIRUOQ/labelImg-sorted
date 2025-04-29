import os
from 查找新字典索引对应的旧字典的索引 import *
# 设置图片所在的文件夹路径
folder_path = r'C:\Users\67167\Desktop\YOLU\YOLOXUNLIAN\ultralytics-8.3.55\datasets\icon\images\train'

# 获取文件夹中所有文件的列表
file_list = os.listdir(folder_path)

# 过滤出图片文件（假设图片的扩展名为 .jpg, .jpeg, .png 等）
image_extensions = ['.jpg', '.jpeg', '.png']
image_files = [f for f in file_list if any(f.lower().endswith(ext) for ext in image_extensions)]

# 按文件名排序（如果需要按字母顺序排列）
image_files.sort()

# 遍历图片文件，重命名为 1.jpg, 2.jpg, 3.jpg 等（根据原始扩展名保持一致）
for index, image_file in enumerate(image_files, start=1):
    # 获取文件扩展名
    file_extension = os.path.splitext(image_file)[1]

    # 构建旧文件路径和新文件路径
    old_file_path = os.path.join(folder_path, image_file)
    new_file_name = f"{index}{file_extension}"  # 重新命名为 1.jpg, 2.jpg, 3.jpg 等，保持原始扩展名
    new_file_path = os.path.join(folder_path, new_file_name)

    # 检查新文件路径是否已存在，如果已存在则跳过
    if os.path.exists(new_file_path):
        print(f"文件 {new_file_path} 已存在，跳过重命名。")
        continue  # 跳过当前文件

    # 重命名文件
    os.rename(old_file_path, new_file_path)
    print(f"已将 {old_file_path} 重命名为 {new_file_path}")
