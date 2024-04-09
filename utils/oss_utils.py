import oss2
import os


auth=''
# 填写Bucket名称。
bucket = oss2.Bucket(auth, 'https://oss-ap-southeast-5.aliyuncs.com', 'fuse-prod')


def put_file(dir_name,file_name,file_path):
    """

    :param dir_name:oss 设置文件夹名称
    :param file_name: 文件名称
    :param file_path: 待上传文件的路径
    :return:
    """
    # 必须以二进制的方式打开文件。
    # 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
    with open(file_path, 'rb') as fileobj:
        # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。
        #fileobj.seek(1000, os.SEEK_SET)
        # Tell方法用于返回当前位置。
        #current = fileobj.tell()
        # 填写Object完整路径。Object完整路径中不能包含Bucket名称。
        object_name="%s/%s"%(dir_name,file_name)
        bucket.put_object(object_name, fileobj)


def set_file_sign(object_name,expire_time):
    """

    :param object_name:oss 上文件存放的位置 eg：object_name = "adakami/A_Policy_List_1-14_15-6-2022_2022-06-16.xlsx"
    :param expire_time: 过期时间，单位秒
    :return:
    """

    # 生成上传文件的签名URL，有效时间为60秒。
    # 生成签名URL时，OSS默认会对Object完整路径中的正斜线（/）进行转义，从而导致生成的签名URL无法直接使用。
    # 设置slash_safe为True，OSS不会对Object完整路径中的正斜线（/）进行转义，此时生成的签名URL可以直接使用。
    url = bucket.sign_url('GET', object_name, expire_time, slash_safe=True)
    print('签名url的地址为：', url)
    return url
    # 使用签名URL上传本地文件。
    # 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。
    # 如果未指定本地路径只设置了本地文件名称（例如examplefile.txt），则默认从示例程序所属项目对应本地路径中上传文件。
    #result = bucket.put_object_with_url_from_file(url, 'A_Policy_List_1-14_15-6-2022_2022-06-16.xlsx')
    #print(result.status)


def get_file_from_dir(dir_name,file_name):
    """

    :param dir_name: oss上目录的位置
    :param file_name: 文件的下载位置 eg：file_name = '/home/jms/fbi-api/report_forms/temp_need/ruizhong/%s' % (name2)
    :return:
    """
    for obj in oss2.ObjectIteratorV2(bucket, prefix=dir_name+'/', delimiter='/', fetch_owner=True):
        # 通过is_prefix方法判断obj是否为文件夹。
        if obj.is_prefix():  # 判断obj为文件夹。
            print('directory: ' + obj.key)
        else:  # 判断obj为文件。
            name=obj.key
            print(name)
            name2=name.split("/")[1]
            bucket.get_object_to_file(name, file_name)


def show_file_name(dir_name):
    """

    :param dir_name: oss上目录的位置
    :param file_name: 文件的下载位置 eg：file_name = '/home/jms/fbi-api/report_forms/temp_need/ruizhong/%s' % (name2)
    :return:
    """
    for obj in oss2.ObjectIteratorV2(bucket, prefix=dir_name+'/', delimiter='/', fetch_owner=True):
        # 通过is_prefix方法判断obj是否为文件夹。
        if obj.is_prefix():  # 判断obj为文件夹。
            print('directory: ' + obj.key)
        else:  # 判断obj为文件。
            name=obj.key
            print("file_name=",name)