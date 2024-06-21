import time

import oss2
from loguru import logger


class OssControler:
    def __init__(self, key_id: str, key_secret: str, endpoint: str, bucket: str):
        """
        Args:
            key_id: ID
            key_secret: SECRET
            endpoint: 端点区域，比如杭州：oss-cn-hangzhou.aliyuncs.com
            bucket: 桶名
        """
        self.auth = oss2.Auth(key_id, key_secret)
        self.bucket = oss2.Bucket(self.auth, endpoint, bucket)
        self.prefix_url = 'https://{}.{}'.format(bucket, endpoint)
        self.bucket_name = bucket

    def delete_one(self, path: str):
        """删除一个文件"""
        self.bucket.delete_object(path)
        logger.info('OSS已删除 ==> {}'.format(path))

    def list_dir(self, dir: str):
        """列出所有文件（包含子孙目录下的文件）"""
        for object in oss2.ObjectIteratorV2(self.bucket, prefix=dir):
            oss_path = object.key
            if not oss_path.endswith('/'):
                yield oss_path

    def get_size(self, key: str, tomb=True):
        """获取文件大小（默认MB）"""
        result = self.bucket.list_objects(key)
        if not result.object_list:
            logger.warning('OSS上没有此文件 ==> {}'.format(key))
            return
        b = result.object_list[0].size
        return round(b / 1024 ** 2, 4) if tomb else b

    def get_url(self, key: str):
        """获取文件地址，路径不存在则抛出异常"""
        self.check(key)
        url = '{}/{}'.format(self.prefix_url, key)
        return url

    def check(self, key: str):
        """检查路径，路径不存在则抛出异常"""
        if self.is_exists(key) is False:
            raise Exception('路径不存在 ==> {}'.format(key))

    def is_exists(self, key: str):
        """判断路径是否存在"""
        return self.bucket.object_exists(key)

    def move(self, src_key: str, dst_key: str):
        """移动oss路径"""
        self.bucket.copy_object(self.bucket_name, source_key=src_key, target_key=dst_key)
        self.bucket.delete_object(src_key)

    def upload(self, bdata: bytes, key: str, retry=2, rest=0.5, replace=None):
        """
        上传文件到OSS，上传成功返回地址，上传失败返回None
        Args:
            bdata: 上传的二进制数据
            key: OSS路径
            retry: 重试次数
            rest: 重试间隔
            replace: 路径重复时，是否替换

        Returns:
            URL / None
        """
        if self.is_exists(key) is True:
            logger.warning('OSS路径已存在 ==> {}'.format(key))
            if replace is None:
                return
            if replace is False:
                return self.get_url(key)

        for _ in range(1 + retry):
            try:
                result = self.bucket.put_object(key, bdata)
                if result.status == 200:
                    return self.get_url(key)
            except Exception as e:
                logger.error('上传文件到OSS ==> {}'.format(e))
                time.sleep(rest)

    def download(self, key: str, file: str, retry=2, rest=0.5) -> bool:
        """
        从OSS下载文件到本地，上传成功返回True，否则返回False
        Args:
            key: OSS路径
            file: 本地文件
            retry: 重试次数
            rest: 重试间隔

        Returns:
            True / False
        """
        for _ in range(1 + retry):
            try:
                resp = self.bucket.get_object_to_file(key, file)
                return True if resp.status == 200 else False
            except Exception as e:
                logger.warning('从OSS下载文件 ==> {}'.format(e))
                time.sleep(rest)
        return False
