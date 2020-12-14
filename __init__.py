import os
from hoshino import Service


sv = Service("原神帮助")


help_txt = '''这是一个HoshinoBot的原神相关插件，包含原神抽卡，丘丘语翻译，找神瞳,找资源点等功能
插件仓库在 https://github.com/H-K-Y/Genshin_Impact_bot.git
 
'''

root = os.getcwd()
@sv.on_fullmatch("原神帮助")
async def help(bot, ev):
    await bot.send(ev, help_txt + f"[CQ:image,file=file:///{root}//hoshino//modules//Genshin_Impact_bot//command.png]")


