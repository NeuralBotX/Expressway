![Expressway Project](./images/首页图像展示.png)

### 🚀 Expressway network planning 🚦 project in Chongqing🛤️, Sichuan Province🐼.

[![GitHub license](https://img.shields.io/github/license/microsoft/Generative-AI-For-Beginners.svg)](https://github.com/Yunheng-Wang/Expressway/blob/master/LICENSE.txt)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Yunheng-Wang/Expressway)



# 🌟 项目背景

高速公路作为专供汽车分方向、分车道行驶，全部控制出入的多车道公路，高速公路在综合交通运输体系中发挥着骨干作用，是交通运输现代化的重要标志。自1995年成渝高速公路建成通车以来，四川省先后编制了六版高速公路网规划（1996版、2009版、2011版、2014版、2019版、2022版）；在其指导下，四川省高速公路经历了由局部连通、通道贯通，再到加密成网的发展历程，通达深度由“地市通”向“县县通”逐步拓展，覆盖广度由平原经济区向盆周山区、高原山区不断延伸，空间形态由省会放射线为主向“射、横、纵、联、环”相互交错演变。截至2022年底，四川省高速公路网已建成9179公里、位居全国第三，进出川通道数量达28条，覆盖县城比例达78%（已通143个县）、六车道及以上占比达16.8%（1545公里）。高速公路网的快速发展，显著提升了四川交通的发展能级，为加快建设交通强省、推动新时代治蜀兴川再上新台阶奠定了坚实基础。

党的二十大擘画了以中国式现代化全面推进中华民族伟大复兴的宏伟蓝图，中央财经委要求交通把“联网、补网、强链”作为建设重点，全面提升网络效益。展望未来，四川省高速公路网仍有巨大的建设空间，但建设的难度和挑战明显增大。根据《四川省高速公路网布局规划（2022-2035年）》，到2035年四川省高速公路网里程将达约2.0万公里（含扩容复线600公里、远期展望线1700公里），形成由20条成都放射线、13条纵线以及4条环线、44条联络线组成的路网格局。截至2022年底，规划2.0万公路的高速公路中，已建规模仅占45%，在建3593公里、占20%，待建 7000 公里、占35%。

如何锚定治蜀兴川再上新台阶的新要求，把握好适度超前的度，科学实施剩余高速公路项目，推动高速公路高质量发展，是当前四川交通运输行业的重要任务。长期以来，公路网规划实施管理主要通过五年规划项目库、年度投资计划、规划执行评估等环节进行调控。受到理论方法制约，规划决策以定性分析和经验判断为主，缺乏路网效益评估方面的量化支撑，具体表现为：一是缺乏项目实施对路网可达性、均衡性、脆弱性等空间结构影响的量化评测；二是缺乏全路网交通流量、时空分布、运行效率、经营效益等运行状态的量化分析；三是缺乏高速公路与区域经济之间协调关系的量化评价。



# 🗃️ 项目基本简介

建立面向路网层面的公路网络特征分析方法，以之为工具辨明四川高速公路网发展的规律特征，并提出优化完善网络的对策建议，对提高规划实施决策水平具有重要作用，其成果的价值主要体现在三个方面：一是形成基于复杂网络理论和多源数据融合算法的公路网络特征分析成套技术，填补国内在该研究领域的技术空白。二是形成公路网络效益综合评价体系，为规划决策过程中项目遴选和评估提供量化分析工具。三是形成四川高速公路网发展历史演变、空间结构、运行状态等方面的主要结论，为今后编制五年发展年规划、开展路网中长期规划等提供参考。


# ⚡️ 如何快速配置该项目的环境

1. 首先你需要在某个文件根目录下执行以下程序从而创建一个虚拟环境
```fish
python -m venv venv
```

2. 激活该虚拟环境
```fish
.\myenv\Scripts\activate
```

3. 执行以下命令来执行 set.up 文件 （这里为了快速安装第三方库 我们配置了阿里的镜像源）
```fish
pip install . -i https://mirrors.aliyun.com/pypi/simple/
```
至此你的虚拟环境配置完成，你可以通过，pycharm来打开 \venv\Scripts\python.exe 的环境源


# 📂 项目介绍目录
|    |                  链接                  |                 概述                 | 备注信息   |                             
|:--:|:------------------------------------:|:----------------------------------:|--------|
| 00 | [四川省路基础数据集说明](src/DataSet/Readme.md) | 描述四川省的数据集，需要涵盖节点信息、路网信息以及相关基础数据的解释 | ###### | 
| 01 |  [构建基础路网代码解释](src/Graph/Readme.md)   | 描述路网的构建方式，并对如何构建基础路网的代码类进行详细的解释说明  | ###### | 




