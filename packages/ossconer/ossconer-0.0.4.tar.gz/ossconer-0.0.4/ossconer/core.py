import os
import time
from typing import Generator

import oss2
from loguru import logger

from ossconer.exceptions import KeyExists, KeyNotExists


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

    def exists(self, key: str) -> bool:
        """判断路径是否存在"""
        has = self.bucket.object_exists(key)
        return has

    def hope(self, key: str, exists=True) -> None:
        """
        期望key存在/不存在，失望则抛出异常

        Args:
            key: OSS文件
            exists: 是否存在

        Returns: 
            None
        """
        has = self.exists(key)
        if exists and not has:
            raise KeyNotExists(key)
        if not exists and has:
            raise KeyExists(key)

    def delete(self, key: str, log=True) -> None:
        """删除一个OSS文件"""
        self.bucket.delete_object(key)
        if log is True:
            logger.info('OSS文件已被删除 ==> {}'.format(key))

    def list_keys(self, dir: str) -> Generator:
        """列出目录下所有的OSS文件（包括子孙目录下的OSS文件）"""
        for object in oss2.ObjectIteratorV2(self.bucket, prefix=dir):
            key = object.key
            if not key.endswith('/'):
                yield key

    def get_size(self, key: str) -> int:
        """获取OSS文件大小（字节）"""
        result = self.bucket.list_objects(key)
        if not result.object_list:
            raise KeyNotExists(key)
        b: int = result.object_list[0].size
        return b

    def move(self, src_key: str, dst_key: str) -> None:
        """移动OSS文件"""
        self.bucket.copy_object(self.bucket_name, source_key=src_key, target_key=dst_key)
        self.bucket.delete_object(src_key)

    def get_url(self, key: str) -> str:
        """获取OSS文件地址"""
        self.hope(key)
        url = '{}/{}'.format(self.prefix_url, key)
        return url

    def push(self, key: str, src: bytes | str, force=False) -> bool:
        """
        上传文件到OSS

        Args:
            key: OSS文件
            src: 上传的二进制数据 / 本地文件路径
            force: 若key存在，是否上传

        Returns:
            True / False
        """
        if force is False:
            self.hope(key, exists=False)

        if isinstance(src, bytes):
            data = src
        else:
            with open(src, 'rb') as f:
                data = f.read()

        result = self.bucket.put_object(key, data)
        return result.status == 200

    def pull(self, key: str, dst: str) -> bool:
        """
        从OSS下载文件

        Args:
            key: OSS文件
            dst: 本地路径（父目录不存在则自动创建）

        Returns:
            True / False
        """
        pdir = os.path.dirname(os.path.abspath(dst))
        if not os.path.exists(pdir):
            os.makedirs(pdir)
        result = self.bucket.get_object_to_file(key, dst)
        return result.status == 200

    def upload(self, src: bytes | str, key: str, retry=2, rest=0.5, replace: bool = None, log=True):
        """
        上传文件到OSS，然后返回地址，默认重试2次

        Args:
            src: 上传的二进制数据 / 本地文件路径
            key: OSS文件
            retry: 重试次数
            rest: 重试间隔
            replace: key重复时，是否替换

        Returns:
            URL / None
        """
        # 如果key已存在，则返回 None / 已有地址
        if self.exists(key):
            if log:
                logger.warning('OSS文件已存在 ==> {}'.format(key))
            if replace is None:
                return
            if replace is False:
                return self.get_url(key)

        # 强制上传，如果key已存在则覆盖
        for _ in range(1 + retry):
            try:
                if self.push(key, src, force=True):
                    return self.get_url(key)
            except Exception as e:
                logger.error('上传失败 ==> {}'.format(e))
                time.sleep(rest)

    def download(self, key: str, dst: str, retry=2, rest=0.5) -> bool:
        """
        从OSS下载文件到本地，默认重试2次

        Args:
            key: OSS文件
            dst: 本地文件
            retry: 重试次数
            rest: 重试间隔

        Returns:
            True / False
        """
        for _ in range(1 + retry):
            try:
                return self.pull(key, dst)
            except Exception as e:
                logger.error('下载失败 ==> {}'.format(e))
                time.sleep(rest)
        return False
