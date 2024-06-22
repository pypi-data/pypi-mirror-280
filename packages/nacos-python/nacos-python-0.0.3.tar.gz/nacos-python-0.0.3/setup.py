import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nacos-python",
    version="0.0.3",
    author="alan",
    author_email="al6nlee@gmail.com",
    description="适配nacos模块",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/al6nlee/nacos-python",
    packages=setuptools.find_packages(exclude=('tests', 'tests.*')),  # 指定最终发布的包中要包含的packages
    classifiers=[  # 其他信息，一般包括项目支持的Python版本，License，支持的操作系统
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development"
    ],
    install_requires=[],  # 项目依赖哪些库(内置库就可以不用写了)，这些库会在pip install的时候自动安装
    python_requires='>=3.9',
    license='MIT',
    package_data={  # 默认情况下只打包py文件，如果包含其它文件比如.so格式，增加以下配置
        "loggingA": [
            "*.py",
            "*.so",
        ]
    },
)
