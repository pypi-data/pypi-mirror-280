from setuptools import setup, find_packages

setup(
    name="locust_telc",
    version="1.5",
    author="galaxy",
    author_email="3340604072@qq.com",
    description="Add interface description information. If it causes infringement, please contact to delete it",

    # 项目主页
    url="http://iswbm.com/", 
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    python_requires='>=3.8',
    include_package_data=True,
    include_entry_points = True,
    zip_safe=True,
    install_requires=['locust>=1.2.3',],


    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages(),
    # 希望被打包的文件
    package_data={
        'locust_telc/webui':['dist/*.html','dist/assets/*.ico','dist/assets/*.js'],
               },
    entry_points={
        'console_scripts': [
            'locust = locust_telc.main:main',
        ],
    },
)