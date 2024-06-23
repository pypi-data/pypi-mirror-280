"""
pjsk-name-index
2022-present Moedigital,YuxiangWang_0525 and pjsk-name-index contributors
"""

full_name = ['Hatsune Miku', 'Kagamine Rin', 'Kagamine Len', 'Megurine Luka', 'MEIKO', 'KAITO', 'Hoshino Ichika', 'Tenma Saki', 'Mochizuki Honami', 'Hinomori Shiho', 'Hanasato Minori', 'Kiritani Haruka', 'Momoi Airi', 'Hinomori Shizuku', 'Azusawa Kohane', 'Shiraishi An', 'Shinonome Akito', 'Aoyagi Toya', 'Tenma Tsukasa', 'Otori Emu', 'Kusanagi Nene', 'Kamishiro Rui', 'Yoisaki Kanade', 'Asahina Mafuyu', 'Shinonome Ena', 'Akiyama Mizuki']
full_name_cn = ['初音未来', '镜音铃', '镜音连', '巡音流歌', 'MEIKO', 'KAITO', '星乃一歌', '天马咲希', '望月穗波', '日野森志步', '花里实乃理', '桐谷��', '桃井爱莉', '日野森雫', '小豆泽心羽', '白石杏', '东云彰人', '青柳冬弥', '天马司', '凤笑梦', '草薙宁宁', '神代类', '宵崎奏', '朝比奈真冬', '东云绘名', '晓山瑞希']

team_name = ['VIRTUAL SINGER', 'Leo/need', 'MORE MORE JUMP!', 'Vivid BAD SQUAD', 'Wonderlands x Showtime', 'Nightcord at 25:00']
team_name_cn = ['虚拟歌手', 'Leo/need', 'MORE MORE JUMP!', 'Vivid BAD SQUAD', 'Wonderlands x Showtime', '25时，在Nightcord。']
team_name_cn_official = ['虚拟歌手', '狮雨星绊', '萌萌飞跃少女团！', '炫狂小队', '奇幻仙境演出秀', '25点,夜音见']

simple_name = ['miku', 'rin', 'len', 'luka', 'meiko', 'kaito', 'ick', 'saki', 'hnm', 'shiho', 'mnr', 'hrk', 'airi', 'szk', 'khn', 'an', 'akt', 'toya', 'tks', 'emu', 'nene', 'rui', 'knd', 'mfy', 'ena', 'mzk']
simple_team_name = ['vs', 'ln', 'mmj', 'vbs', 'ws', '25时']

# 待补全,所有戏称/别名必须在字典的嵌套列表中
joke_name_cn = {
    'Hatsune Miku': ['葱', '猫葱', '白葱'],
    'Kagamine Rin': [],
    'Kagamine Len': [],
    'Megurine Luka': [],
    'MEIKO': [],
    'KAITO': [],
    'Hoshino Ichika': [],
    'Tenma Saki': ['马晓希'],
    'Mochizuki Honami': ['穗波妈妈'],
    'Hinomori Shiho': [],
    'Hanasato Minori': [],
    'Kiritani Haruka': [],
    'Momoi Airi': [],
    'Hinomori Shizuku': [],
    'Azusawa Kohane': [],
    'Shiraishi An': [],
    'Shinonome Akito': [],
    'Aoyagi Toya': [],
    'Tenma Tsukasa': [],
    'Otori Emu': ['汪大吼'],
    'Kusanagi Nene': [],
    'Kamishiro Rui': [],
    'Yoisaki Kanade': ['小气走'],
    'Asahina Mafuyu': ['马福友'],
    'Shinonome Ena': ['董慧敏'],
    'Akiyama Mizuki': []
}

# 生成索引
character_index = {name: full_name_cn[index] for index, name in enumerate(simple_name)}

team_index = {name: team_name_cn[index] for index, name in enumerate(simple_team_name)}

team_cn_official_index = {name: team_name_cn[index] for index, name in enumerate(team_name_cn_official)}

team_cn_index = {name: team_name_cn_official[index] for index, name in enumerate(team_name_cn)}

def sekai_index(name, type):
    def create_index(data):
        grouped_data = {
            'teams': [],
            'individual': []
        }

        # 遍历团队数据并添加到grouped_data中
        for index, team in enumerate(data['team_name']):
            grouped_data['teams'].append({
                'full_name': team,
                'full_name_cn': data['team_name_cn'][index],
                'full_name_cn_official': data['team_name_cn_official'][index],
                'simple_name': data['simple_team_name'][index]
            })

        # 遍历个人数据并添加到grouped_data中
        for index, name in enumerate(data['full_name']):
            member = {
                'full_name': name,
                'full_name_cn': data['full_name_cn'][index],
                'simple_name': data['simple_name'][index],
                'joke_name_cn': ','.join(data['joke_name_cn'][name]) if data['joke_name_cn'][name] else ''
            }
            grouped_data['individual'].append(member)

        return grouped_data

    data = {
        'full_name': full_name,
        'full_name_cn': full_name_cn,
        'simple_name': simple_name,
        'joke_name_cn': joke_name_cn,
        'team_name': team_name,
        'team_name_cn': team_name_cn,
        'team_name_cn_official': team_name_cn_official,
        'simple_team_name': simple_team_name
    }
    index = create_index(data)

    result = None
    if type == 'team':
        result = next((team for team in index['teams'] if any(name.lower() in str(value).lower() for value in team.values())), None)
    elif type == 'individual':
        result = next((member for member in index['individual'] if any(name.lower() in str(value).lower() for value in member.values())), None)

    return result

# Exporting variables and functions
__all__ = [
    'full_name',
    'full_name_cn',
    'team_name',
    'team_name_cn',
    'team_name_cn_official',
    'simple_name',
    'simple_team_name',
    'character_index',
    'team_index',
    'joke_name_cn',
    'team_cn_official_index',
    'team_cn_index',
    'sekai_index'
]
