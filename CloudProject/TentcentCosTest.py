from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
# 配置信息
secret_id = ''  # 替换为你的SecretId
secret_key = ''  # 替换为你的SecretKey
region = 'ap-shanghai'  # 替换为你的存储桶所在地域
bucket_name = 'zj-1226-1333744868'  # 替换为你的存储桶名称

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

local_file_path = 'C:\\Users\\22124\\Desktop\\download.jpg'
cos_file_path = 'test/modi.jpg'

try:
    response = client.download_file(
        Bucket=bucket_name,
        Key=cos_file_path,
        DestFilePath=local_file_path
    )
    print("文件下载成功！")
except Exception as e:
    print("文件下载失败：", e)


# def list_all_objects(bucket_name):
#     marker = ""
#     while True:
#         response = client.list_objects(
#             Bucket=bucket_name,
#             Marker=marker
#         )
#         if 'Contents' in response:
#             for content in response['Contents']:
#                 print(content['Key'])
#         if response['IsTruncated'] == 'false':
#             break
#         marker = response['NextMarker']
#
# list_all_objects(bucket_name)
