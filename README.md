# SubList

迅雷不及掩耳之势以辞成章。

## 功能

1. **根据 srt 字幕切分 wav 音频，生成 list 映射。**
2. **根据 list 映射合并 wav 音频，生成新的 list 映射。**
3. **根据 list 映射和 wav 音频打包，生成适用于** [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) **的数据集：** 默认支持中文、英文。若要实现支持多语言，请手动修改 ` pack.py ` 的 ` set_languages `，具体 ` langs ` 支持详见 [pylangid3](https://github.com/adbar/py3langid)。**注意**：请勿将 ` zh ` 与 ` ja ` 同时用作 ` langs ` 的参数。经测试，这种行为可能会导致语言识别错误。
4. **直接根据 srt 字幕和 wav 音频打包，生成适用于** [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) **的数据集：** 默认支持中文、英文。若要实现支持多语言，请手动修改 ` pack.py ` 的 ` set_languages `，具体 ` langs ` 支持详见 [pylangid3](https://github.com/adbar/py3langid)。**注意**：请勿将 ` zh ` 与 ` ja ` 同时用作 ` langs ` 的参数。经测试，这种行为可能会导致语言识别错误。

## 安装

### 依赖

* [Python 3.x](https://www.python.org/downloads/)
* [FFmpeg](https://ffmpeg.org/download.html)

### 整合包

#### Windows

* [Github](https://github.com/HaTiWinter/SubList/releases/download/20240602/SubList.exe)

### 手动安装

``` bash
pip install -r requirements.txt
```

## 使用

### 根据 srt 字幕切分 wav 音频

``` bash
# split.py
# 根据 srt 字幕切分 wav 音频，生成 list 映射
# 需把字幕和音频放在同一目录下
python split.py <input_file> <output_dir>
```

### 根据 list 映射合并 wav 音频

``` bash
# merge.py
# 根据 list 映射合并 wav 音频，生成新的 list 映射
# 需把映射和音频放在同一目录下
python merge.py <input_dir> <output_dir>
```

### 根据 list 映射和 wav 音频打包

``` bash
# pack.py
# 根据 list 映射和 wav 音频打包，生成适用于 GPT-SoVITS 的数据集
# 需把映射和音频放在同一目录下
python pack.py <input_dir> <output_dir>
```

### 直接根据 srt 字幕和 wav 音频打包

``` bash
# integrator.py
# 直接根据 srt 字幕和 wav 音频打包，生成适用于 GPT-SoVITS 的数据集
# 需把字幕和音频放在同一目录下
python integrator.py <input_dir> <output_dir> <speaker>
```

## 鸣谢

### 相关项目

* [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 提供了数据集的格式
* [Alice_split_toolset](https://github.com/AliceNavigator/Alice_split_toolset) | 提供了程序基础流程的灵感
