## ***四川省可用的路网基础数据集概述***
- Road_Y : 乡道 
- Road_X : 县道 
- Road_S : 省道
- Road_G : 国道
- Road_C : 村道
- Road_D : 空数据
- Road_Z : 空数据
- Road_V : 仅有一条数据


## ***数据集中存在 MultiLineString 类型的有哪些文件?***
- Road_Y;Road_W;Road_C


## ***四川省数据可用的离散点基础数据集概述***
- CBJZCP : 村子
- YHGQP : 管理站、养护站、道班
- YXFWSS : 客运站、车站、加油站、服务站、停车区
- ZCJCZP : 检测站
- ZRCP : 村委
- CBJZCP : 村子、村委会
- XZP : 镇、乡、少数民族
- WZKP : 鞭炮仓库、机养中心
- WHLYLJDP : 景区、公园、科技园
- ***SFZP : 收费站***
- SDP : 隧道
- QXZP : 机场气象台
- QLP : 桥
- LCZP : 疑似高速网络节点
- JZCP : 委员会、村子
- JTLJDP : 车站服务区、养护站、渡口、出入口
- CRKP : 道路出入口
- DKP : 渡口、码头
- GSGXFWSSP : 服务区、加水区、停车区
- GYJGP : 养护区
- HDP : 涵洞
- JCZP : 大坝
- JJLJDP : 产业园、公司
- JKSBP : 车辆检测器、监控设施
- JTLGCP : 观测站
- ***GANTRY : 门架***


# ***数据属性解释***
- https://data.ms.gov.cn/portal/service_detail?id=0000000078f27166017946a42383359a&type=opendata#tabLink8


## ***四川省数据在路网中如何判断某路线是否是高速公路?***
- 目前为止，主要有三列属性依据可以来判断路线是高速公路：
  - 'LXBH' : 路线的编号
  - 'LDJSDJ' : 道路等级标识。值包括：1，2，3，4，5，None(空)
  - 'LXMC' : 路线的名称

- 由于LDJSDJ属性中部分值缺失（None空值） 以及 LXMC 中部分中文名称存在误差等问题
- 该项目使用 LXBH 属性作为识别是否为高速公路的关键因素
  - 主要原因：数据无缺失
  - 核心思想：
    1. LXBH 中 G/Y/H/C ... + 三位数字 : 一般公路,如国道省道等
    2. LXBH 中 G/Y/H/C ... + 两位数字/一位数字/四位数字 (上述1的差集) : 高速公路
    3. LXMC 中 含有高速两个字的
    4. LDJSDJ 中 为1的

- 注意：Road_C 文件中不存在高速公路线路（其他文件的待完善...）


# ***代码可执行对输入的文件有什么要求？***
- 文件格式为 .shp 
- 离散点 文件内 存在 两个属性 CROWID 、geometry 且这些属性值不能为空
- 路网数据 文件内 存在 CROWID 、geometry、LXBH、LDJSDJ、LXMC 或 CROWID 、geometry、LXBH、LXMC 且这些属性值不能为空



