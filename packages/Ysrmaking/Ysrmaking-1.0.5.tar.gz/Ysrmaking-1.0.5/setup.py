from setuptools import setup, find_packages


setup(
    name="Ysrmaking",
    version="1.0.5",
    packages=['Ysrmaking'],
    install_requires=[
        'cyaron','importlib'
        # 在这里列出你的库所需的其他Python包
    ],

    author="Cloud_Ann",
    author_email="383067040@qq.com",
    description="this is for making the sample test on openjudge to testing coding probelm",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/cloudann/YSRmaking",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.11"
    ]
)