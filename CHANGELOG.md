# MAZE.AI Changelog

所有重要的版本更改都将在此处记录。

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
