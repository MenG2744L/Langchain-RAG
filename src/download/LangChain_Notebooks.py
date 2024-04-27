import requests
import zipfile
import os

# 定义云端文件的 URL
url = 'https://cdn-oss-prod.unlimiai.com/jupyter/LangChain_Notebooks.zip'
# 定义本地文件保存路径
local_file_path = 'E:\\python-prj\\Langchain-RAG\\assets\\LangChain_Notebooks.zip'
# 定义解压缩目标文件夹路径
extract_folder_path = 'E:\\python-prj\\Langchain-RAG\\assets\\'

if not os.path.exists(local_file_path):
    # 发送 HTTP GET 请求下载文件
    response = requests.get(url)

    # 检查响应状态码是否为 200 (成功)
    if response.status_code == 200:
        # 以二进制写入模式打开本地文件
        with open(local_file_path, 'wb') as f:
            # 将响应内容写入本地文件
            f.write(response.content)
        print("文件下载成功！")
    else:
        print("文件下载失败。")
else:

    # 创建解压缩目标文件夹
    os.makedirs(extract_folder_path, exist_ok=True)

    # 打开 ZIP 文件
    with zipfile.ZipFile(local_file_path, 'r') as zip_ref:
        # 解压缩 ZIP 文件到指定目录
        zip_ref.extractall(extract_folder_path)

    print("ZIP 文件解压缩完成。")
