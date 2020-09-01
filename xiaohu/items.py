# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinadrugtrialsInfoItem(scrapy.Item):
    # define the fields for your item here like:

    _id = scrapy.Field()  # _id 即使是mongodb默认添加，也需要在这里定义

    curr_page = scrapy.Field()

    reg_no = scrapy.Field()  # 登记号

    # 详情信息
    public_inf = scrapy.Field()

    # 机构信息
    inst_inf = scrapy.Field()

    # curr_page = scrapy.Field()  # 页面编码
    # base_inf = scrapy.Field()  # 基本信息
    # researcher_inf = scrapy.Field()  # 研究者信息
    # insts_inf = scrapy.Field()  # 机构信息
    # back_inf = scrapy.Field()  # 背景信息
    # status_inf = scrapy.Field()  # 状态信息

    # pass


# class BaseItem(scrapy.Item):
#     _id = scrapy.Field()  # _id 即使是mongodb默认添加，也需要在这里定义
#     curr_page = scrapy.Field()
#     登记号 = scrapy.Field()
#     试验状态 = scrapy.Field()
#     申请人联系人 = scrapy.Field()
#     首次公示信息日期 = scrapy.Field()
#     申请人名称 = scrapy.Field()


# class ResearcherItem(scrapy.Item):
#     _id = scrapy.Field()  # _id 即使是mongodb默认添加，也需要在这里定义
#     curr_page = scrapy.Field()
#     姓名 = scrapy.Field()
#     学位 = scrapy.Field()
#     职称 = scrapy.Field()
#     电话 = scrapy.Field()
#     Email = scrapy.Field()
#     邮政地址 = scrapy.Field()
#     邮编 = scrapy.Field()
#     单位名称 = scrapy.Field()


# class InstsItem(scrapy.Item):
#     _id = scrapy.Field()  # _id 即使是mongodb默认添加，也需要在这里定义
#     curr_page = scrapy.Field()
#     机构名称 = scrapy.Field()
#     主要研究者 = scrapy.Field()
#     国家 = scrapy.Field()
#     省_州 = scrapy.Field()
#     城市 = scrapy.Field()


# class BackItem(scrapy.Item):
#     _id = scrapy.Field()  # _id 即使是mongodb默认添加，也需要在这里定义
#     curr_page = scrapy.Field()
#     登记号 = scrapy.Field()
#     相关登记号 = scrapy.Field()
#     药物名称 = scrapy.Field()
#     药物类型 = scrapy.Field()
#     临床申请受理号 = scrapy.Field()
#     适应症 = scrapy.Field()
#     试验专业题目 = scrapy.Field()
#     试验通俗题目 = scrapy.Field()
#     试验方案编号 = scrapy.Field()
#     版本日期 = scrapy.Field()
#     方案最新版本号 = scrapy.Field()
#     方案是否为联合用药 = scrapy.Field()


# class StatusItem(scrapy.Item):
#     _id = scrapy.Field()  # _id 即使是mongodb默认添加，也需要在这里定义
#     curr_page = scrapy.Field()
#     试验状态 = scrapy.Field()
#     目标入组人数 = scrapy.Field()
#     已入组人数 = scrapy.Field()
#     实际入组总人数 = scrapy.Field()

class InstItem(scrapy.Item):
    _id = scrapy.Field()  # _id 即使是mongodb默认添加，也需要在这里定义
    curr_page = scrapy.Field()
    登记号 = scrapy.Field()
    机构名称 = scrapy.Field()
    主要研究者 = scrapy.Field()
    国家 = scrapy.Field()
    省_州 = scrapy.Field()
    城市 = scrapy.Field()


class PublicInfoItem(scrapy.Item):
    _id = scrapy.Field()
    # 基本信息
    登记号 = scrapy.Field()
    试验状态 = scrapy.Field()
    申请人联系人 = scrapy.Field()
    首次公示信息日期 = scrapy.Field()
    申请人名称 = scrapy.Field()

    # 背景信息
    相关登记号 = scrapy.Field()
    药物名称 = scrapy.Field()
    药物类型 = scrapy.Field()
    临床申请受理号 = scrapy.Field()
    适应症 = scrapy.Field()
    试验专业题目 = scrapy.Field()
    试验通俗题目 = scrapy.Field()
    试验方案编号 = scrapy.Field()
    版本日期 = scrapy.Field()
    方案最新版本号 = scrapy.Field()
    方案是否为联合用药 = scrapy.Field()

    # 申请人信息
    联系人座机 = scrapy.Field()
    联系人手机号 = scrapy.Field()
    联系人邮箱 = scrapy.Field()
    联系人邮政地址 = scrapy.Field()
    联系人邮编 = scrapy.Field()

    # 实验设计
    试验分类 = scrapy.Field()
    试验分期 = scrapy.Field()
    设计类型 = scrapy.Field()
    随机化 = scrapy.Field()
    盲法 = scrapy.Field()
    试验范围 = scrapy.Field()

    # 主要研究者
    研究者姓名 = scrapy.Field()
    研究者学位 = scrapy.Field()
    研究者职称 = scrapy.Field()
    研究者电话 = scrapy.Field()
    研究者邮箱 = scrapy.Field()
    研究者邮政地址 = scrapy.Field()
    研究者邮编 = scrapy.Field()
    研究者单位名称 = scrapy.Field()

    # 状态信息
    试验状态2 = scrapy.Field()
    目标入组人数 = scrapy.Field()
    已入组人数 = scrapy.Field()
    实际入组总人数 = scrapy.Field()


ip_pool = [
    '58.218.200.223:4927',
    '58.218.200.228:3718',
    '58.218.200.227:3515',
    '58.218.200.228:3873',
    '58.218.200.228:5400',
    '58.218.200.226:6699',
    '58.218.200.226:2236',
    '58.218.200.228:5109',
    '58.218.200.225:7840',
    '58.218.200.226:6723',
    '58.218.200.249:8070',
    '58.218.200.227:7106',
    '58.218.200.226:8894',
    '58.218.200.249:5593',
    '58.218.200.228:4359',
    '58.218.200.225:4895',
    '58.218.200.226:2517',
    '58.218.200.223:5298',
    '58.218.200.225:3146',
    '58.218.200.225:5874',
    '58.218.200.225:8323',
    '58.218.200.228:7571',
    '58.218.200.223:3565',
    '58.218.200.249:5575',
    '58.218.200.227:7627',
    '58.218.200.225:5088',
    '58.218.200.226:6581',
    '58.218.200.225:4745',
    '58.218.200.223:3752',
    '58.218.200.228:8723',
    '58.218.200.227:8495',
    '58.218.200.225:3719',
    '58.218.200.228:6806',
    '58.218.200.227:4682',
    '58.218.200.225:8697',
    '58.218.200.226:2386',
    '58.218.200.228:4544',
    '58.218.200.249:7123',
    '58.218.200.225:6345',
    '58.218.200.227:4000',
    '58.218.200.223:3875',
    '58.218.200.223:2729',
    '58.218.200.226:4302',
    '58.218.200.225:8044',
    '58.218.200.249:7071',
    '58.218.200.227:6946',
    '58.218.200.225:3028',
    '58.218.200.225:8916',
    '58.218.200.249:7076',
    '58.218.200.227:5095',
    '58.218.200.225:4241',
    '58.218.200.223:5778',
    '58.218.200.226:7841',
    '58.218.200.226:8179',
    '58.218.200.223:5570',
    '58.218.200.226:3090',
    '58.218.200.227:6082',
    '58.218.200.227:6959',
    '58.218.200.228:5750',
    '58.218.200.226:3678',
    '58.218.200.227:5047',
    '58.218.200.226:4359',
    '58.218.200.225:7513',
    '58.218.200.228:8498',
    '58.218.200.227:5216',
    '58.218.200.226:6940',
    '58.218.200.228:7778',
    '58.218.200.226:3469',
    '58.218.200.226:6290',
    '58.218.200.249:8231',
    '58.218.200.228:4417',
    '58.218.200.225:8377',
    '58.218.200.225:3584',
    '58.218.200.226:6780',
    '58.218.200.227:3505',
    '58.218.200.227:2031',
    '58.218.200.226:5883',
    '58.218.200.228:4340',
    '58.218.200.226:8844',
    '58.218.200.228:2867',
    '58.218.200.223:7582',
    '58.218.200.249:8324',
    '58.218.200.223:5263',
    '58.218.200.228:2933',
    '58.218.200.225:8647',
    '58.218.200.227:4342',
    '58.218.200.226:8775',
    '58.218.200.227:4194',
    '58.218.200.226:3738',
    '58.218.200.249:2625',
    '58.218.200.227:6001',
    '58.218.200.223:2440',
    '58.218.200.228:7927',
    '58.218.200.225:8975',
    '58.218.200.249:7846',
    '58.218.200.225:3257',
    '58.218.200.226:2597',
    '58.218.200.225:3274',
    '58.218.200.249:4505',
    '58.218.200.226:8897',
    '58.218.200.227:5564',
    '58.218.200.223:4721',
    '58.218.200.227:2312',
    '58.218.200.226:7901',
    '58.218.200.226:3351',
    '58.218.200.226:4399',
    '58.218.200.226:2721',
    '58.218.200.226:3634',
    '58.218.200.249:5008',
    '58.218.200.227:3886',
    '58.218.200.226:6359',
    '58.218.200.223:7934',
    '58.218.200.226:8733',
    '58.218.200.223:3086',
    '58.218.200.226:2313',
    '58.218.200.228:4971',
    '58.218.200.249:8902',
    '58.218.200.249:7174',
    '58.218.200.227:4347',
    '58.218.200.228:6628',
    '58.218.200.226:4094',
    '58.218.200.225:6963',
    '58.218.200.223:3014',
    '58.218.200.249:7029',
    '58.218.200.223:2332',
    '58.218.200.227:5442',
    '58.218.200.223:6161',
    '58.218.200.227:2808',
    '58.218.200.227:8963',
    '58.218.200.225:6663',
    '58.218.200.225:7792',
    '58.218.200.227:4905',
    '58.218.200.228:3621',
    '58.218.200.223:8377',
    '58.218.200.249:5042',
    '58.218.200.225:5466',
    '58.218.200.226:2279',
    '58.218.200.225:7814',
    '58.218.200.226:5484',
    '58.218.200.225:3880',
    '58.218.200.223:6657',
    '58.218.200.227:7143',
    '58.218.200.225:4514',
    '58.218.200.227:4360',
    '58.218.200.227:2254',
    '58.218.200.249:4129',
    '58.218.200.227:7643',
    '58.218.200.226:7407',
    '58.218.200.226:2895',
    '58.218.200.223:3264',
    '58.218.200.228:9144',
    '58.218.200.249:4670',
    '58.218.200.225:2630',
    '58.218.200.249:6357',
    '58.218.200.225:8704',
    '58.218.200.226:2878',
    '58.218.200.226:9000',
    '58.218.200.225:3714',
    '58.218.200.225:6577',
    '58.218.200.225:3693',
    '58.218.200.225:5521',
    '58.218.200.223:2900',
    '58.218.200.226:3124',
    '58.218.200.228:3938',
    '58.218.200.227:6090',
    '58.218.200.249:4697',
    '58.218.200.226:8939',
    '58.218.200.228:8707',
    '58.218.200.227:5148',
    '58.218.200.228:8092',
    '58.218.200.226:7995',
    '58.218.200.225:9028',
    '58.218.200.226:4434',
    '58.218.200.249:7187',
    '58.218.200.228:2151',
    '58.218.200.223:6198',
    '58.218.200.249:4133',
    '58.218.200.223:2396',
    '58.218.200.223:8314',
    '58.218.200.226:7923',
    '58.218.200.228:2245',
    '58.218.200.226:5247',
    '58.218.200.249:8814',
    '58.218.200.223:9013',
    '58.218.200.227:3199',
    '58.218.200.226:5290',
    '58.218.200.249:5763',
    '58.218.200.227:7860',
    '58.218.200.227:2554',
    '58.218.200.225:6548',
    '58.218.200.226:5528',
    '58.218.200.228:3256',
    '58.218.200.226:8958',
    '58.218.200.249:4485',
    '58.218.200.226:5428',
    '58.218.200.223:4127',
    '58.218.200.249:4387',
    '58.218.200.227:4383',
    '58.218.200.223:2065',
    '58.218.200.223:4401',
    '58.218.200.226:3046',
    '58.218.200.226:5687',
    '58.218.200.225:3016',
    '58.218.200.223:7344',
    '58.218.200.223:6572',
    '58.218.200.228:3618',
    '58.218.200.226:7939',
    '58.218.200.226:6113',
    '58.218.200.227:4944',
    '58.218.200.227:4010',
    '58.218.200.226:8228',
    '58.218.200.226:3288',
    '58.218.200.227:4096',
    '58.218.200.223:2072',
    '58.218.200.228:4309',
    '58.218.200.227:5406',
    '58.218.200.226:2446',
    '58.218.200.225:4620',
    '58.218.200.225:3979',
    '58.218.200.228:4533',
    '58.218.200.249:4567',
    '58.218.200.223:8221',
    '58.218.200.228:2539',
    '58.218.200.228:7969',
    '58.218.200.227:8918',
    '58.218.200.227:2727',
    '58.218.200.225:8473',
    '58.218.200.249:5458',
    '58.218.200.223:9111',
    '58.218.200.227:2643',
    '58.218.200.249:3471',
    '58.218.200.228:7644',
    '58.218.200.227:8588',
    '58.218.200.226:7160',
    '58.218.200.225:7950',
    '58.218.200.225:4431',
    '58.218.200.227:3860',
    '58.218.200.228:5190',
    '58.218.200.223:3666',
    '58.218.200.228:7046',
    '58.218.200.227:3258',
    '58.218.200.223:4814',
    '58.218.200.223:7447',
    '58.218.200.227:2499',
    '58.218.200.225:8123',
    '58.218.200.227:2850',
    '58.218.200.228:4078',
    '58.218.200.228:4794',
    '58.218.200.225:3963',
    '58.218.200.223:6757',
    '58.218.200.225:3503',
    '58.218.200.223:7298',
    '58.218.200.249:7926',
    '58.218.200.249:6245',
    '58.218.200.225:8351',
    '58.218.200.226:5761',
    '58.218.200.225:3823',
    '58.218.200.225:3061',
    '58.218.200.228:4609',
    '58.218.200.227:8633',
    '58.218.200.228:3023',
    '58.218.200.223:3470',
    '58.218.200.223:3859',
    '58.218.200.249:2642',
    '58.218.200.223:4084',
    '58.218.200.227:8431',
    '58.218.200.226:7659',
    '58.218.200.226:2459',
    '58.218.200.228:4885',
    '58.218.200.227:4296',
    '58.218.200.225:5585',
    '58.218.200.249:7363',
    '58.218.200.227:5191',
    '58.218.200.225:5358',
    '58.218.200.227:3683',
    '58.218.200.226:2406',
    '58.218.200.223:5650',
    '58.218.200.225:2077',
    '58.218.200.228:7568',
    '58.218.200.226:3561',
    '58.218.200.223:3027',
    '58.218.200.228:4581',
    '58.218.200.227:8496',
    '58.218.200.227:2630',
    '58.218.200.249:4385',
    '58.218.200.225:5404',
    '58.218.200.249:2301',
    '58.218.200.225:8822',
    '58.218.200.228:7229',
    '58.218.200.228:3625',
    '58.218.200.228:8188',
    '58.218.200.228:6522',
    '58.218.200.223:6358',
    '58.218.200.228:8862',
    '58.218.200.227:7390',
    '58.218.200.228:2171',
    '58.218.200.228:7937',
    '58.218.200.228:5444',
    '58.218.200.249:3931',
    '58.218.200.227:6030',
    '58.218.200.228:7149',
    '58.218.200.226:3198',
    '58.218.200.226:3500',
    '58.218.200.249:8657',
    '58.218.200.227:2136',
    '58.218.200.249:6441',
    '58.218.200.249:7889',
    '58.218.200.225:4906',
    '58.218.200.249:3846',
    '58.218.200.228:5141',
    '58.218.200.226:2602',
    '58.218.200.223:8790',
    '58.218.200.223:4114',
    '58.218.200.225:7688',
    '58.218.200.223:3050',
    '58.218.200.223:8964',
    '58.218.200.226:5549',
    '58.218.200.225:3228',
    '58.218.200.226:2687',
    '58.218.200.226:7752',
    '58.218.200.225:7028',
    '58.218.200.228:2751',
    '58.218.200.226:2840',
    '58.218.200.226:4004',
    '58.218.200.227:2476',
    '58.218.200.226:9099',
    '58.218.200.225:4088',
    '58.218.200.226:2437',
    '58.218.200.249:8689',
    '58.218.200.228:5276',
    '58.218.200.226:5279',
    '58.218.200.223:8068',
    '58.218.200.249:8139',
    '58.218.200.225:7567',
    '58.218.200.227:7922',
    '58.218.200.226:4453',
    '58.218.200.225:6044',
    '58.218.200.225:7857',
    '58.218.200.227:8079',
    '58.218.200.223:7764',
    '58.218.200.225:3783',
    '58.218.200.225:6734',
    '58.218.200.228:3716',
    '58.218.200.227:4844',
    '58.218.200.225:3126',
    '58.218.200.249:6948',
    '58.218.200.228:6129',
    '58.218.200.223:3266',
    '58.218.200.249:3491',
    '58.218.200.228:7258',
    '58.218.200.228:2844',
    '58.218.200.228:6100',
    '58.218.200.249:2296',
    '58.218.200.223:4962',
    '58.218.200.249:3613',
    '58.218.200.227:9042',
    '58.218.200.249:8874',
    '58.218.200.226:9019',
    '58.218.200.225:8912',
    '58.218.200.249:3816',
    '58.218.200.249:9175',
    '58.218.200.249:5592',
    '58.218.200.228:8543',
    '58.218.200.226:8546',
    '58.218.200.227:2007',
    '58.218.200.228:4923',
    '58.218.200.225:3465',
    '58.218.200.227:2851',
    '58.218.200.225:3709',
    '58.218.200.223:7551',
    '58.218.200.226:7931',
    '58.218.200.226:7205',
    '58.218.200.228:5760',
    '58.218.200.227:8664',
    '58.218.200.226:6888',
    '58.218.200.228:4383',
    '58.218.200.225:4158',
    '58.218.200.225:8719',
    '58.218.200.249:2421',
    '58.218.200.227:4201',
    '58.218.200.228:8425',
    '58.218.200.228:7535',
    '58.218.200.225:2680',
    '58.218.200.225:8682',
    '58.218.200.225:8316',
    '58.218.200.249:6041',
    '58.218.200.227:3296',
    '58.218.200.223:5989',
    '58.218.200.249:8483',
    '58.218.200.225:5692',
    '58.218.200.227:5937',
    '58.218.200.223:5032',
    '58.218.200.223:2468',
    '58.218.200.225:5863',
    '58.218.200.226:4951',
    '58.218.200.225:3514',
    '58.218.200.249:2991',
    '58.218.200.225:8227',
    '58.218.200.249:8813',
    '58.218.200.228:6438'
]
