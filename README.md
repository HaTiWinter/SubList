# SubList

迅雷不及掩耳之势以辞分曲之。

## 功能

1. [根据 srt 字幕切分 wav 音频](#split)，生成 list 映射。
2. [根据 list 映射合并 wav 音频](#merge)，生成新的 list 映射。
3. [根据 list 映射和 wav 音频打包](#pack)，生成适用于 [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) 的数据集。
4. [直接根据 srt 字幕和 wav 音频打包](#integrator)，生成适用于 [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) 的数据集。

## 安装

### 依赖

* [Python 3.x](https://www.python.org/downloads/)
* [FFmpeg](https://ffmpeg.org/download.html)

### 整合包

#### Windows

* [Github](https://github.com/HaTiWinter/SubList/releases/download/20240601/SubList.exe)
* [阿里云盘（63qk）](https://www.alipan.com/s/FrG7hRxQsmf)
* [天翼云盘（q5g2）](https://cloud.189.cn/t/i2yEjeV7vaEv)

### 手动安装

``` bash
pip install -r requirements.txt
```

## 使用

### 根据 srt 字幕切分 wav 音频 {#split}

``` bash
# split.py
# 根据 srt 字幕切分 wav 音频，生成 list 映射
# 需把字幕和音频放在同一目录下
python split.py <input_file> <output_dir>
```

### 根据 list 映射合并 wav 音频 {#merge}

``` bash
# merge.py
# 根据 list 映射合并 wav 音频，生成新的 list 映射
# 需把映射和音频放在同一目录下
python merge.py <input_dir> <output_dir>
```

### 根据 list 映射和 wav 音频打包 {#pack}

``` bash
# pack.py
# 根据 list 映射和 wav 音频打包，生成适用于 GPT-SoVITS 的数据集
# 需把映射和音频放在同一目录下
python pack.py <input_dir> <output_dir>
```

### 直接根据 srt 字幕和 wav 音频打包 {#integrator}

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
