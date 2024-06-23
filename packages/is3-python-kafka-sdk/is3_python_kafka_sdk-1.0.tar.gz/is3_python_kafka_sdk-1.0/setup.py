import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="is3-python-kafka-sdk",
    version="1.0",
    author="chaser",
    author_email="sxing.liu@foxmail.com",
    description="is3 python kafka server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/ZhihengNing/Python-server",
    packages=setuptools.find_packages(),
    install_requires=['flask==3.0.3',
                      'flasgger==0.9.7.1',
                      'gunicorn',
                      'requests==2.32.3',
                      'confluent-kafka==2.3.0'],
    entry_points={
        'console_scripts': [
            'is3_run_app=app:main'
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
