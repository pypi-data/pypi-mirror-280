from distutils.core import setup
from setuptools import find_packages

setup(name='Ship-bai',    # 包名
      version='1.0.0',        # 版本号
      description='Ship Class',
      long_description='Ship Class',
      author='Shaojie',
      author_email='otnw_bsj@163.com',
      url='',
      install_requires=[
          'pygame'
      ],	# 依赖包会同时被安装
      license='MIT',
      packages=find_packages())
