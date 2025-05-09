﻿**浙江师范大学课题任务分工及推进计划**

## **1. 任务清单及内容说明**
### **1.1 基于公路GIS数据的网络拓扑快速建模。**
#### **1.1.1具体内容**
以公路养护电子地图数据和国家公路网矢量数据为基础，研发面向规划研究的网络拓扑快速生成技术，建立典型路网拓扑模型。

注意规划路网与实际路网的区别，规划路网以县市、重要经济节点、重要交通枢纽等为节点，实际路网以互通及收费站为节点，需根据应用场景区别处理。（**浙江师范大学**、江苏智澄）。

注：公路养护电子地图是100米为间隔的，类似养护桩号一样来标注；国家公路网矢量数据提供比较齐全的节点数据，包括收费站、重要交通枢纽站等交通节点，和县市中心、重要经济中心等构成的经济节点；

2. #### **网络拓扑构建**
**1） 高速公路网络拓扑快速生成**

1) 将节点放入到高速公路网络中。选取可能构成为节点的交通基础设施（包括但是不限于以下内容：收费站、龙门架、高速服务站（包括停车区））、互通枢纽），找到距离最近的路段端点作为交通基础设施在高速公路网络中的节点（需要设置节点的不同属性，后续可以区分开来）；
1) 确定相邻节点间距离、平均车道数、平均限速、道路等级等信息；
1) 对构造的高速网络图信息进行检查；
1) 对于给定节点类型，快速网络拓扑建模的算法构建。

**2） 以城市和重要经济中心为节点的高速公路网络拓扑快速构建**

1) 城市中心为节点，构造城市之间的高速公路网络（以高速公路网络线路来构造）；
1) 给定一对城市，形成给定对城市之间的若干条高速联通路径。

### **1.2 <a name="_hlk153301851"></a>构建高速公路网空间结构评价指标体系**
#### **1.2.1 具体内容**
在分析传统路网评价指标实用性的基础上（路网密度、节点连接率、通道数量、通道间距、路网连通度、平均车道数、路网等级结构），引入或改进复杂网络指标，构建公路网空间结构评价指标体系。（**浙江师范大学**、部规划院、江苏智澄）。

注：公路体系的基本概念包括：路网密度、节点连接率、通道数量、通道间距、路网连通度、平均车道数、路网等级结构等，先去规划文本里面将概念理清。增加相关公路体系里面的概念，特别是去看看高速公路相关新闻里面对于高速公路网络的概念。但是上面这些概念，其实本质上并没有涉及网络的概念内容，还是局限于局部和线路的概念，因而构建高速公路网空间结构评价指标体系，其本质上是研究高速公路网络的网络全局拓扑结构特征的构建。

#### **1.2.2 构建高速公路网空间结构评价指标体系**
**1） 构建高速公路网空间结构指标**

1) 分析传统的规划体系结构指标，分析与网络结构指标之间的异同；
1) 查找交通运输网络分析文章中相关空间结构指标，找到适用于高速网络的进行引入；
1) 针对b中存在交通网络结构指标中存在的问题，引入网络科学中的相关结构指标，构建更加适用于高速公路网络的空间结构指标。
2. ` `**建立高速公路网空间结构评价体系**
1) 理清各类网络结构指标之间的关联，例如主成分分析等方法进行梳理；
1) 应用比较成熟和公认的指标评价方法（例如灰色评价等）进行高速公路网空间结构评价
1) 应用b的方法，对实际的网络体系进行评价，分析现有网络存在的问题，提出对应的提升方案和解决办法。

### **1.3 高速公路网空间结构指标分析。**
#### **1.3.1 具体内容**
测算四川省、重庆市不同时期高速公路网的空间结构指标，通过指标前后对比揭示路网空间结构变动趋势。（**浙江师范大学**）。

注：高速公路网空间结构指标主要用于描述和分析高速公路网络的空间布局和组织结构，便于理解和评估高速公路网络的现状，为未来的规划和决策提供依据。
#### **1.3.2 分析高速公路网空间结构**
**1）选定分析方法**

1) 应用各类分析方法，分析各种方法之间的异同；
1) 针对高速公路网空间结构，选择适宜的分析方法。

**2）进行具体分析**

1) 根据选定的方法及建立的高速公路网空间结构评价体系对具体数据进行分析；
1) 对a中结果进行拟合，揭示路网空间结构变动趋势。

### **1.4 公路网络空间稳定性研究。**
#### **1.4.1** **具体内容**
研发基于鲁棒性分析的公路网络韧性分析技术，通过计算路网在受到攻击后指标的下降程度，评估典型高速公路网络的稳定性，识别关键路段和节点。（**浙江师范大学**）

注：公路网络的稳定性是指公路网络对来自于外界的各种影响的阻抗性能，一般用网络中部分节点或路段陷入瘫痪后的连通性来表达。公路网络的稳定性是指公路网络对来自于外界的各种影响的阻抗性能，一般用网络中部分节点或路段陷入瘫痪后的连通性来表达。
#### **1.4.2 研究公路网络空间稳定性**
**1） 构建基于鲁棒性的公路网络空间韧性评价指标**

1) 分析传统评估鲁棒性与韧性的指标，分析与公路网络空间韧性指标之间的异同；
1) 查找交通运输网络分析文章中相关指标，找到适用于公路网络的进行引入；
1) 针对b中公路网络稳定性指标中存在的问题，引入网络科学中的相关指标，构建更加适用于高速公路网络的稳定性指标。

**2） 研究公路网络空间稳定性**

1) 通过移除节点的策略对公路网络进行攻击；
1) 依据评价指标，基于攻击后公路网络空间的连通性以及恢复程度等结果研究路网空间的稳定性。

### **1.5 典型路网形态拓扑结构类型抽象。**
#### **1.5.1具体内容**
依托全国及区域路网规划建设数据，借鉴路网几何形态的分类方法，抽象提炼高速公路网的主要拓扑结构类型，如星型、树型、环线、鱼刺型、网络型、放射+环线型等，归纳总结不同类型路网的空间结构特点。（**浙江师范大学**、部规划研究院）。

**注：网络的拓扑结构即网络的形状表示，是将网络中各事物按一定方式连接起来，形成一个有固定结构的物理布局，能够反映实际事物间显性、隐性的关系。**
#### **1.5.2 典型路网形态拓扑结构类型抽象**
**1）提炼各类型路网空间结构特点**

分析全国及区域路网规划建设数据，将数据进行特点提炼。

**2）分类归纳路网拓扑结构**

根据数据特点对数据进行分类，并归纳为各种类型的拓扑结构。

### **1.6 形成公路网空间结构评价技术指南（远期任务）。**
依托上述研究成果，形成公路网空间结构评价标准规范类技术文件，为行业发展提供参考和依据（部规划研究院、**浙江师范大学**、江苏智澄）。

**高速公路网交通运行特征分析（江苏智澄牵头）**

1） 交通拥堵评价及识别研究。

建立公路拥堵评价指数，包括服务水平、行驶速度、拥堵时长、拥堵里程、拥堵频次等指标，科学回答“全路网” “全路段”“全天候”等问题。研发基于多源数据的拥堵快速识别技术，提取四川、重庆高速公路网拥堵路段及节点。探索高速公路拥堵形成和消散机制。（江苏智澄、**浙江师范大学**）

**2） 典型区域的宏观基本图绘制（选择性研究）。**

验证宏观基本图存在性和路网通行能力的指标。（**浙江师范大学**）

**3） 形成面向规划场景的公路网交通运行评价技术指南（远期任务）。**

以支撑规划研究和决策为目标，形成三维三类公路交通运行评价的标准规范类技术文件。三维：收费运营、路网运行、交通出行；三类：路网、通道、节点。（部规划研究院、江苏智澄、**浙江师范大学**）
## **2. 团队分工**
主要承担路网拓扑方向研究；承担有关模型方法的研发；负责或参与研究报告有关章节的撰写；负责相关论文、专著、专利、标准、奖项的具体撰写和申报。

## **3. 时间安排**
具体时间安排请见“浙江师范大学高速公路项目拟定计划.XLSX”文件

## **4. 项目信息及项目组成员情况**

<table><tr><th colspan="2">项目名称</th><th colspan="7">重庆市高速公路网综合技术分析</th></tr>
<tr><td colspan="2" rowspan="2">项目归属</td><td colspan="3">所属单位</td><td colspan="2">所属机构</td><td colspan="2">所属学科</td></tr>
<tr><td colspan="3">浙江师范大学</td><td colspan="2">工学院</td><td colspan="2">交通运输工程</td></tr>
<tr><td colspan="9">项目组成员</td></tr>
<tr><td>序号</td><td colspan="2">姓名</td><td>职称</td><td colspan="2">学历</td><td colspan="2">所在单位</td><td>任务分工</td></tr>
<tr><td>1</td><td colspan="2">余森彬</td><td>讲师</td><td colspan="2">博士</td><td colspan="2">浙江师范大学</td><td>项目负责人</td></tr>
<tr><td>2</td><td colspan="2">李莉莉</td><td>工程师</td><td colspan="2">硕士</td><td colspan="2">金华市轨道交通集团运营有限公司</td><td>技术指导</td></tr>
<tr><td>3</td><td colspan="2">邱  欣</td><td>教授</td><td colspan="2">博士</td><td colspan="2">浙江师范大学</td><td>技术指导</td></tr>
<tr><td>4</td><td colspan="2">杨  青</td><td>副教授</td><td colspan="2">博士</td><td colspan="2">浙江师范大学</td><td>理论指导</td></tr>
<tr><td>5</td><td colspan="2">王运恒</td><td>学生</td><td colspan="2">在读本科</td><td colspan="2">浙江师范大学</td><td>理论指导</td></tr>
<tr><td>6</td><td colspan="2">陈海辰</td><td>学生</td><td colspan="2">在读硕士</td><td colspan="2">浙江师范大学</td><td>现场指导</td></tr>
<tr><td>7</td><td colspan="2">王文婕</td><td>学生</td><td colspan="2">在读本科</td><td colspan="2">浙江师范大学</td><td>文本撰写</td></tr>
<tr><td>8</td><td colspan="2">谭雅文</td><td>学生</td><td colspan="2">在读本科</td><td colspan="2">浙江师范大学</td><td>数据挖掘</td></tr>
<tr><td>9</td><td colspan="2">黄耀毅</td><td>学生</td><td colspan="2">在读本科</td><td colspan="2">浙江师范大学</td><td>文本撰写</td></tr>
</table>

