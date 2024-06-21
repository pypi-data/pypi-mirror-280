from setuptools import setup, find_packages

setup(
    # 如果上传时出现ERROR：The user '' isn't allowed to upload to project ''，换个名字，长一点无所谓，不能跟别人重复
    name="liuwangcs",
    version="0.0.2",
    author="Gardenia",
    author_email="1198481467@qq.com",
    description="This is a project template.",

    # 存放源码的地址，填入gitee的源码网址即可
    # url="https://gitee.com/UnderTurrets/",

    packages=find_packages(),

    # README.md文本的格式，如果希望使用markdown语言就需要下面这句话
    # long_description_content_type="text/markdown",

    # 安装过程中，需要安装的静态文件，如配置文件、service文件、图片等
    # data_files=[
    #      ("", ["conf/*.conf"]),
    #      ("/usr/lib/systemd/system", ["bin/*.service"]),
    #            ],

    # 希望被打包的文件
    # package_data={
    #     "":["*.txt"],
    #     "bandwidth_reporter":["*.txt"]
    #            },

    # 不打包某些文件
    # exclude_package_data={
    #     "bandwidth_reporter":["*.txt"]
    #            },

    # 表明当前模块依赖哪些包，若环境中没有，则会从pypi中下载安装
    # install_requires=["requests",],

    # setup.py 本身要依赖的包，这通常是为一些setuptools的插件准备的配置
    # 这里列出的包，不会自动安装。
    # setup_requires=["",],

    # 仅在测试时需要使用的依赖，在正常发布的代码中是没有用的。
    # 在执行python setup.py test时，可以自动安装这三个库，确保测试的正常运行。
    # tests_require=[
    #     "",
    # ],

    # install_requires 在安装模块时会自动安装依赖包
    # 而 extras_require 不会，这里仅表示该模块会依赖这些包
    # 但是这些包通常不会使用到，只有当你深度使用模块时，才会用到，这里需要你手动安装
    # extras_require={
    #     "":  [""],
    # },
)
