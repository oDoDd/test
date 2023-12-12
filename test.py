import os

def create_folder(folder_path):
    try:
        # 使用exist_ok=True参数，如果目录已存在不会抛出异常
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder '{folder_path}' created successfully.")
    except OSError as error:
        print(f"Creation of the directory {folder_path} failed: {error}")

# 在main函数中调用create_folder函数
def main():
    # ... 省略其他代码 ...

    # 设置要创建的文件夹路径
    folder_path = 'path/to/your/directory'

    # 创建文件夹
    create_folder(folder_path)

    # ... 省略其他代码 ...

# 确保是直接运行此脚本时才执行main函数
if __name__ == '__main__':
    main()