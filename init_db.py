import sqlite3

conn = sqlite3.connect('database.db')

with open('db.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()
cur.execute("INSERT INTO slogan (title, button, content, link) VALUES (?, ?, ?, ?)",
            ('管理团队与玩家共度艰难岁月，忆苦思甜', '了解我们', '444', 'HardTime')
            )
cur.execute("INSERT INTO slogan (title, button, content, link) VALUES (?, ?, ?, ?)",
            ('丰富的活动与浓厚的节日氛围', '加入服务器 参与活动', '333', 'Parties')
            )
cur.execute("INSERT INTO slogan (title, button, content, link) VALUES (?, ?, ?, ?)",
            ('原版与插件的深度融合使游戏内容更丰富', '加入我们 助力开发', '222', 'Plugins')
            )
cur.execute("INSERT INTO slogan (title, button, content, link) VALUES (?, ?, ?, ?)",
            ('以开放包容的姿态大步迈向新时代', '学习新思想', '111', 'NewEra')
            )



cur.execute("INSERT INTO introduce (title, button, content, link) VALUES (?, ?, ?, ?)",
            ('小熊酒吧度假村 远离城市的喧嚣 尽享海岛美景', '', '内容111', 'BearBar')
            )
cur.execute("INSERT INTO introduce (title, button, content, link) VALUES (?, ?, ?, ?)",
            ('即将上线：物料仓库 随时随地存取数据库中的物品', '', '内容222', 'LockoctThings')
            )
cur.execute("INSERT INTO introduce (title, button, content, link) VALUES (?, ?, ?, ?)",
            ('灵动特色反作弊 宁杀一千不放一个 宁枉勿纵', '', '内容111', 'AntiCheat')
            )
cur.execute("INSERT INTO introduce (title, button, content, link) VALUES (?, ?, ?, ?)",
            ('灵动摄影画廊 感受灵动MC的美丽风景与派对的热闹氛围', '', '内容222', 'Gallery')
            )
conn.commit()
conn.close()
