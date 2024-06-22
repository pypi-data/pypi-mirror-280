## 插件配置 部分
import nonebot
from .config import Config, plugin_name, plugin_version, plugin_config
from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

## 机器人 部分
import json
import httpx
import locale
import datetime
from loguru import logger
from nonebot.params import CommandArg
from nonebot import require, on_command
from nonebot.adapters import Bot, Event, MessageSegment, Message

## 回复 & 发图 部分
require("nonebot_plugin_alconna")
from arclet.alconna import Alconna, Args
from nonebot_plugin_alconna import Target, UniMessage, SupportScope, on_alconna, Match

## 定时任务 部分
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

## 数据存储 部分
require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as store

# 插件初始化
__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_obastatus",
    description="获取 OpenBMCLAPI 相关数据",
    usage="""帮助: 返回帮助信息
总览: 返回 OpenBMCLAPI 当前状态
节点 <搜索条件>: 返回搜索到的节点信息
排名 <节点名次>: 返回指定名次的节点的详细信息
93HUB <(可选)图片搜索条件>: 相信你一定知道""",

    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

    homepage="https://github.com/Zero-Octagon/nonebot-plugin-obastatus",
    # 发布必填。

    config=Config,
    # 插件配置项类，如无需配置可不填写。

    supported_adapters={"~onebot.v11"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
)

headers = {
    'Cookie': plugin_config.oba_cookie,
}

# 存储单位格式化
def hum_convert(value):
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = 1024.0
    for i in range(len(units)):
        if (value / size) < 1:
            return "%.2f%s" % (value, units[i])
        value = value / size

# 数字分隔
def format_number(num):
    # 设置区域设置，以便使用逗号作为千位分隔符
    # 注意：这里假设您使用的是英文环境，如果是中文环境，可能需要使用'gbk环境'
    locale.setlocale(locale.LC_ALL, 'gbk')
    # 使用locale的格式化功能
    formatted = locale._format("%d", num, grouping=True)
    return formatted

# 按照名字搜索
def search_by_name(data, search_str, condition):
    # 初始化一个空列表来保存匹配的结果和它们的索引
    results_with_index = []
    
    # 遍历数据中的每一个项目，同时跟踪索引
    for index, item in enumerate(data):
        # 检查'item'字典中的'name'字段是否包含'search_str'
        if search_str.lower() in item.get(condition, '').lower():
            # 如果包含，将整个字典和它的索引添加到结果列表中
            results_with_index.append((index+1, item))
    
    # 返回所有匹配的项目及其索引
    return results_with_index

# 获取索引和对应内容
def get_record_by_index(records, index):
    if index < len(records) and index >= 0:
        return records[index]
    else:
        return None

# 读缓存
def read_file_from_cache(filename: str):
    cache_file = store.get_cache_file(plugin_name, filename)
    with open(cache_file, "r") as f:
        filelist_content = f.read()
        filelist = json.loads(filelist_content)
    return filelist

# 写缓存
def write_file_to_cache(filename, filelist):
    cache_file = store.get_cache_file(plugin_name, filename)
    with open(cache_file, "w") as f:
        json.dump(filelist, f)
    logger.info(f"{filename} 的缓存保存成功")

# 刷新缓存
def reload_cache():
    version = httpx.get('https://bd.bangbang93.com/openbmclapi/metric/version', headers=headers).json()
    dashboard = httpx.get('https://bd.bangbang93.com/openbmclapi/metric/dashboard', headers=headers).json()
    rank = httpx.get('https://bd.bangbang93.com/openbmclapi/metric/rank', headers=headers).json()
    write_file_to_cache('version.json', version)
    write_file_to_cache('dashboard.json', dashboard)
    write_file_to_cache('rank.json', rank)

scheduler.add_job(
    reload_cache, "interval", minutes=1, id="timed_cache_refresh"
)

# 插件的帮助面板
help = on_alconna("帮助")
@help.handle()
async def handle_function(bot: Bot):
    await help.finish(f'''OpenBMCLAPI 面板数据 {plugin_version}
帮助: 返回此信息
总览: 返回 OpenBMCLAPI 当前状态
节点 <搜索条件>: 返回搜索到的节点信息
排名 <节点名次>: 返回指定名次的节点的详细信息
93HUB <(可选)图片搜索条件>: 相信你一定知道
Tips: 结果 >3 条显示部分信息，结果 > 10条不显示任何信息（搜索可爱除外）
特别鸣谢: 盐木、甜木、米露、听风、天秀 和 bangbang93 的不杀之恩
''')
    
# OpenBMCLAPI 总览
status = on_alconna("总览")
@status.handle()
async def handle_function(bot: Bot, event: Event):
    version = read_file_from_cache('version.json')
    dashboard = read_file_from_cache('dashboard.json')
    await status.finish(f'''OpenBMCLAPI 面板数据 {plugin_version}
官方版本: {version.get('version')} | 提交ID: {version.get('_resolved').split('#')[1][:7]}
在线节点数: {dashboard.get('currentNodes')} 个 | 负载: {round(dashboard.get('load')*100, 2)}%
总带宽: {dashboard.get('bandwidth')} Mbps | 出网带宽: {round(dashboard.get('currentBandwidth'), 2)} Mbps
当日请求: {format_number(dashboard.get('hits'))} 次 | 数据量: {hum_convert(dashboard.get('bytes'))}
请求时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
数据源: https://bd.bangbang93.com/pages/dashboard''')

# 根据 节点名称 搜索节点详细信息   
node = on_alconna(
    Alconna(
        "节点",
        Args["name?", str]
    ),
)

@node.handle()
async def handle_function(name: Match[str]):
    if name.available:
        node.set_path_arg("name", name.result)

@node.got_path("name", prompt="缺参数啦！记得补上喵喵～")
async def got_name(name: str):
    args = str(name).replace('\n', '')
    send_text = f'OpenBMCLAPI 面板数据 {plugin_version}'
    if len(str(args)) > 16:
        send_text += f'''\n要求: 节点名称 最多 16 个字符
搜索条件不符合要求，请调整参数后重新尝试'''
    else:
        send_text = f'OpenBMCLAPI 面板数据 {plugin_version}'
        rank = read_file_from_cache('rank.json')
        version = read_file_from_cache('version.json')
        matches_with_index = search_by_name(rank, str(args), 'name')
        if len(matches_with_index) > 0 and len(matches_with_index) <= 3:
            for index, match in matches_with_index:
                enabled_status = '❔'
                fullSize_status = '❔'
                version_status = '❔'
                # 节点状态检测
                if match.get('isEnabled') == True:
                    enabled_status = '✅'
                else:
                    enabled_status = '❌'
                # 节点类型检测
                if match.get('fullSize') == True:
                    fullSize_status = '🌕'
                else:
                    fullSize_status = '🌗'
                # 节点版本检测
                if match.get('version') != None:
                    if match.get('version') == version.get('version'):
                        version_status = '🟢'
                    else:
                        version_status = '🟠'

                send_text += f'''\n{enabled_status}{fullSize_status} | {index} | {match.get('name')} | {match.get('version', '未知')}{version_status}
所有者: {match.get('user', {}).get('name', '未知')} | 赞助商: {match.get('sponsor', {}).get('name', '未知')}
当日流量: {hum_convert(match.get('metric', {}).get('bytes', 0))} | 当日请求数: {format_number(match.get('metric', {}).get('hits', 0))} 次'''
                send_text += f'\n请求时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        elif (len(matches_with_index) > 3 and len(matches_with_index) <= 10) or str(args) == '可爱':
            for index, match in matches_with_index:
                # 节点状态检测
                if match.get('isEnabled') == True:
                    enabled_status = '✅'
                else:
                    enabled_status = '❌'
                send_text += f'''\n{enabled_status} | {index} | {match.get('name')} | {hum_convert(match.get('metric', {}).get('bytes', 0))} | {format_number(match.get('metric', {}).get('hits', 0))}'''
            send_text += f'\n请求时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        elif len(matches_with_index) > 10 and str(args) != '可爱':
            send_text += f'''\n搜索到{len(matches_with_index)}个节点，请改用更精确的名字
请求时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'''
        else:
            send_text += f'''未找到有关 {args} 的相关节点信息，请调整参数后重新尝试
请求时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'''
        r = await UniMessage.text(send_text).send(reply_to=True)
        await r.recall(delay=60, index=0)

# 根据 节点ID 搜索拥有者
node_id = on_alconna(
    Alconna(
        "ID",
        Args["id?", str]
    ),
)

@node_id.handle()
async def handle_function(id: Match[str]):
    if id.available:
        node_id.set_path_arg("id", id.result)

@node_id.got_path("id", prompt="缺参数啦！记得补上喵喵～")
async def got_id(id: str):
    send_text = f'OpenBMCLAPI 面板数据 {plugin_version}'
    if len(id) > 24:
        send_text = f'''OpenBMCLAPI 面板数据 {plugin_version}
要求: 节点ID 最多 24 个字符
搜索条件不符合要求，请调整参数后重新尝试'''
    else:
        rank = read_file_from_cache('rank.json')
        version = read_file_from_cache('dashboard.json')
        matches_with_index = search_by_name(rank, id, '_id')
        if len(matches_with_index) > 0 and len(matches_with_index) <= 3:
            for index, match in matches_with_index:
                enabled_status = '❔'
                fullSize_status = '❔'
                version_status = '❔'
                # 节点状态检测
                if match.get('isEnabled') == True:
                    enabled_status = '✅'
                else:
                    enabled_status = '❌'
                # 节点类型检测
                if match.get('fullSize') == True:
                    fullSize_status = '🌕'
                else:
                    fullSize_status = '🌗'
                # 节点版本检测
                if match.get('version') != None:
                    if match.get('version') == version.get('version'):
                        version_status = '🟢'
                    else:
                        version_status = '🟠'

                send_text += f'''\n{enabled_status}{fullSize_status} | {index} | {match.get('name')} | {match.get('version', '未知')}{version_status}
所有者: {match.get('user', {}).get('name', '未知')} | 赞助商: {match.get('sponsor', {}).get('name', '未知')}
当日流量: {hum_convert(match.get('metric', {}).get('bytes', 0))}
当日请求数: {format_number(match.get('metric', {}).get('hits', 0))} 次
ID: {match.get('_id')}'''
                send_text += f'\n请求时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        elif len(matches_with_index) > 3 and len(matches_with_index) <= 10:
            for index, match in matches_with_index:
                # 节点状态检测
                enabled_status = '❔'
                fullSize_status = '❔'
                version_status = '❔'
                if match.get('isEnabled') == True:
                    enabled_status = '✅'
                else:
                    enabled_status = '❌'
                # 节点类型检测
                if match.get('fullSize') == True:
                    fullSize_status = '🌕'
                else:
                    fullSize_status = '🌗'
                # 节点版本检测
                if match.get('version') != None:
                    if match.get('version') == version.get('version'):
                        version_status = '🟢'
                    else:
                        version_status = '🟠'
                send_text += f'''\n{enabled_status}{fullSize_status}{version_status} | {index} | {match.get('name')} | {hum_convert(match.get('metric', {}).get('bytes', 0))} | {format_number(match.get('metric', {}).get('hits', 0))}'''
            send_text += f'\n请求时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        elif len(matches_with_index) > 10:
            send_text += f'''\n搜索到{len(matches_with_index)}个节点，请改用更精确的ID
请求时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'''
        else:
            send_text += f'''未找到有关 {id} 的相关节点信息，请调整参数后重新尝试
请求时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'''
        r = await UniMessage.text(send_text).send(reply_to=True)
        await r.recall(delay=60, index=0)
            
# 根据 节点名称 搜索节点详细信息   
node_rank = on_alconna(
    Alconna(
        "排名",
        Args["position?", str]
    ),
)

@node_rank.handle()
async def handle_function(position: Match[str]):
    if position.available:
        node_rank.set_path_arg("position", position.result)

@node_rank.got_path("position", prompt="缺参数啦！记得补上喵喵～")
async def got_position(position: int):
    send_text = f'OpenBMCLAPI 面板数据 {plugin_version}'
    rank = read_file_from_cache('rank.json')
    version = read_file_from_cache('version.json')
    try:
        index = position-1
        match = get_record_by_index(rank, index)
        if match is not None:  # 正常情况
            enabled_status = '❔'
            fullSize_status = '❔'
            version_status = '❔'
            # 节点状态检测
            if match.get('isEnabled') == True:
                enabled_status = '✅'
            else:
                enabled_status = '❌'
            # 节点类型检测
            if match.get('fullSize') == True:
                fullSize_status = '🌕'
            else:
                fullSize_status = '🌗'
            # 节点版本检测
            if match.get('version') != None:
                if match.get('version') == version.get('version'):
                    version_status = '🟢'
                else:
                    version_status = '🟠'
            send_text += f'''\n{enabled_status}{fullSize_status} | {index+1} | {match.get('name')} | {match.get('version', '未知')}{version_status}
所有者: {match.get('user', {}).get('name', '未知')} | 赞助商: {match.get('sponsor', {}).get('name', '未知')}
当日流量: {hum_convert(match.get('metric', {}).get('bytes', 0))}
当日请求数: {format_number(match.get('metric', {}).get('hits', 0))} 次'''
            send_text += f'\n请求时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        else:   # 超了
            send_text += f'\n索引超出范围，请输入一个有效的数字。'
            send_text += f'\n请求时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    except ValueError:
        send_text = f'''OpenBMCLAPI 面板数据 {plugin_version}
要求: 节点名次 必须为一个整数
搜索条件不符合要求，请调整参数后重新尝试'''
    r = await UniMessage.text(send_text).send(reply_to=True)
    await r.recall(delay=60, index=0)
            
# 随机获取 Mxmilu666/bangbang93HUB 中精华图片
bangbang93HUB = on_alconna(
    Alconna(
        "93HUB",
        Args["name?", str]
    ),
)

@bangbang93HUB.handle()
async def handle_function(name: Match[str]):
    if name.available:
        bangbang93HUB.set_path_arg("name", name.result)

@bangbang93HUB.got_path("name", prompt=UniMessage.image('https://apis.bmclapi.online/api/93/random').send(reply_to=True))
async def handle_function(name: str):
    send_text = ''
    name = name.replace('\n', '')
    matchList = []
    imageList = httpx.get('https://ttb-network.top:8800/mirrors/bangbang93hub/filelist', headers=headers).json()

    for i in imageList:
        if name.lower() in i:
            matchList.append(i)

    if len(matchList) < 1:
        send_text = UniMessage.text('找不到哦，请重新尝试~')
    elif len(matchList) == 1:
        send_text =  UniMessage.image(f"https://apis.bmclapi.online/api/93/file?name={matchList[0]}")
    else:
        send_text = UniMessage.text(f'搜索结果包含 {len(matchList)} 条，请改用更加精确的参数搜索')
    r = await send_text.send(reply_to=True)
    await r.recall(delay=60, index=0)

# 开机后先运行一遍重载缓存
reload_cache()