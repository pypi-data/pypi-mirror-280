from setuptools import setup, find_packages

setup(
    name='pjsk_name_index',
    version='1.1.0',
    author='YuxiangWang0525',
    author_email='yuxiangwang0525@gmail.com',
    description='A library for indexing names from the game Project Sekai.',
    long_description=open('README.md',encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_package_name',
    packages=find_packages(),
    install_requires=[
        # 依赖列表
    ],
    classifiers=[
        # 开发状态
        'Development Status :: 5 - Production/Stable',
        # 目标用户
        'Intended Audience :: Developers',
        # 许可证（比如MIT）
        'License :: OSI Approved :: MIT License',
        # 兼容的Python版本
        'Programming Language :: Python :: 3',
    ],
)
