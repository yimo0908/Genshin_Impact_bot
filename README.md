# Genshin_Impact_bot

### This is a Genshin Impact plugin for [HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)
### 这是一个[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)原神~~抽卡~~插件
### 这个项目目前正在扩展，加入更多原神相关娱乐和信息查询功能，敬请期待

### 如果你是在项目名称为Genshin_Impact_gacha时安装的，请删除Genshin_Impact_gacha重新Git clone

# 安装方法

在 HoshinoBot\hoshino\modules 目录下使用git拉取本项目

然后在 HoshinoBot\\hoshino\\config\\\__bot__.py 文件的 MODULES_ON 加入 Genshin_Impact_bot

config.py文件有插件的常用配置，你可以根据自己的情况修改

重启 HoshinoBot

# 效果演示
### 原神抽卡
![原神抽卡](https://github.com/H-K-Y/Genshin_Impact_bot/blob/main/screenshot/qiu_qiu_translation.png) 
### 丘丘语翻译
![丘丘语翻译](https://github.com/H-K-Y/Genshin_Impact_bot/blob/main/screenshot/genshin_impact_gacha.png) 

# 指令

### 原神抽卡

@bot相遇之缘：10连抽卡

@bot纠缠之缘：90连抽卡

@bot原之井：180连抽卡

原神卡池：查看当前UP池，这个指令也可以用来重载卡池配置文件，config.json保存的是当前卡池信息

原神卡池切换：切换其他原神卡池


### 丘丘语翻译
丘丘一下 丘丘语句 ：翻译丘丘语

丘丘词典 丘丘语句 ：查询丘丘语句的单词含义


# 更新记录

### 2020-10-22
* 修复了4星概率写错了导致4星只能保底抽出的问题.............
* 加入了更多抽卡的统计结果，比如抽出最多的武器是啥，第一个4星和5星事多少抽出的

### 2020-10-21
* 在config.py加入了抽卡限制功能，限制每个人一天最多抽多少次，感谢[corvo007](https://github.com/corvo007)提出的粪pr (粪pr是他自己说的
* 修复了第一次切换卡池后不能再切换卡池的问题
* 修复了查看UP信息时报错的问题

### 2020-10-20
* 重构了项目代码，~~第二天就重写？~~，~~过几天怕是忘了写的啥了........~~
* 加入的武器UP池和常驻池
* 加入了切换卡池的功能

### 2020-10-19
* 加入10连抽，90连抽和180连抽
* 加入抽卡发送图片功能
* 修复了Windows系统发送图片时可能出现的路径问题，图片全部改为base64发送





