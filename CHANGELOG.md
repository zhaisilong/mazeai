# MAZE.AI Changelog

所有重要的版本更改都将在此处记录。

## [0.0.7] - 2024-04-23

### Added

- 引入 [MolVS](https://molvs.readthedocs.io/en/latest)

## [0.0.6] - 2024-04-20

### Added

- 在 Python 中编写一个支持 pip extra 选项的包
- chem: 标志符转 smiles 两种方式

### Fixed

- Readthedocs 左下角打不开: 去掉 `conf.py` 中的 pdf 注释（消除了首页乱码），然后将 `python` 版本从 `3.12` 改为 `3.7`  即可

## [0.0.5] - 2024-04-19

- 加入 Read The Docs，参考[博文](https://zhaisilong.com/index.php/archives/readthedocs.html)

## [0.0.4] - 2024-04-19

### Added - Failed

- 构建 [Anaconda](https://docs.anaconda.com/free/anacondaorg/user-guide/packages/conda-packages/) 包自动上传的 workflows
- <https://www.pyopensci.org/python-package-guide/tutorials/publish-conda-forge.html>

```bash
mamba install anaconda-client
anaconda login

# 这种方式上传到 anaconda cloud 
python setup.py sdist
version="0.0.3"
anaconda upload dist/mazeai-"${version}".tar.gz

mamba install grayskull
grayskull pypi dist/mazeai-"${version}".tar.gz
```

## [0.0.2] - 2024-04-19

### Added

- 初始化库
- 构建 PyPi 自动上传的 workflows
