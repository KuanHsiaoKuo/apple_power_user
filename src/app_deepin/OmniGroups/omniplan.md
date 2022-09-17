# OmniPlan介绍

![img](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/plan-card.png)

<!--ts-->
* [OmniPlan介绍](#omniplan介绍)
   * [基础流程](#基础流程)
   * [完善/维护流程](#完善维护流程)
      * [复查](#复查)
      * [增加注释](#增加注释)
   * [常用快捷键](#常用快捷键)
   * [小技巧](#小技巧)
      * [导出选择](#导出选择)
         * [任务安排](#任务安排)
         * [资源使用](#资源使用)
         * [大纲视图](#大纲视图)
         * [网络视图](#网络视图)
      * [容忍期](#容忍期)
   * [报告选择](#报告选择)
   * [参考资源](#参考资源)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sat Sep 17 13:43:48 UTC 2022 -->

<!--te-->

<video src="https://www.omnigroup.com/assets/img/2020/plan-video-18.mp4" controls="controls"></video>

## 基础流程

1. 确定项目的基本信息和控制项
2. 编写任务分解
3. 为每一个任务确定他的投人
4. 添加资源,把资源分配到任务中去
5. 确定每一项工作任务的先后顺序和关系
6. 自动排程后检查每一项资源的使用倩况

## 完善/维护流程

### 复查

1. 检查任务间的关联是否符合预期一一网络视图
2. 使用“显示安排影响因素”和“检查器"确认调整后的任务关联
3. 计划是否有优化空间一一甘特图直接调整任务

### 增加注释

1. 补充说明任务是什么
2. 多方合作时，标明需要其他方的何种资源的支持

## 常用快捷键

- 切换检查视图：cmd+shift+i(info)

## 小技巧

### 导出选择

> 主要还是按照任务、资源、项目大纲、网络图这四块分别导出后再合并

#### 任务安排

![image-20220626155900015](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220626155900015.png)

#### 资源使用

![image-20220626155615091](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220626155615091.png)

#### 大纲视图

#### 网络视图

### 容忍期

```admonish tip title='容忍期'
有时候可能某些任务需要间接交替完成，这时候就需要设置容忍期
```

## 报告选择

## 参考资源

- [Omniplan](https://support.omnigroup.com/documentation/omniplan/mac/4.3/en/)

- [【OmniPlan系列】2_创建新的项目计划（1）_: 任务分解](https://www.bilibili.com/video/BV1zV41187Vx)
    - 项目大纲介绍
- [【OmniPlan系列】2_创建新的项目计划（2）](https://www.bilibili.com/video/BV1ty4y1S7Tj)
    - 任务(甘特)视图介绍: [gantt-view](https://support.omnigroup.com/documentation/omniplan/mac/4.3/en/gantt-view/#gantt-view)
    - 设置任务时间, 任务时间显示，资源分配，任务关联关系
    - 任务类型：任务、里程碑（确定两个任务的先后关系）、吊床、群组
    - 自动排程
    - 检查任务关系：顺序是否错乱、每个资源的任务是否线性安排、资源视图查看是否有重合(两个资源做同一件事)
    - 基础流程
    - 导出方式
- [【OmniPlan系列】3_设置有效工作时间](https://www.bilibili.com/video/BV1WV411h78U)
    - 资源视图使用
    - 考虑国家假期、节假日安排等
    - 调整工作时间、工作日
    - 添加加班时间，比如周末
    - 去掉休息日：在资源界面按住shift拖拽
    - 可以针对项目、单个资源设置
- [【OmniPlan教程】4 完善项目进度计划(https://www.bilibili.com/video/BV1bV411h7oE)
    - 复查工作任务：网络视图, 可以直接拖拽连接快速安排任务关联
    - 显示安排影响因素：暂未找到，只能在右侧任务检查器菜单看到
    - 任务优化：鼠标拖拽+任务锁定
    - 为工作任务添加注释
    - 如何完善项目计划
- [【OmniPlan教程】5_资源视图与资源使用方法-1_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Yi4y1c7dH)
    - 资源视图的组成：人员、设备、素材、群组
    - 任务检查器 > 更改资源分配时: 任务持续时间、任务工作量、已分配额度(可多人协作完成任务)
- [【OmniPlan教程】6_跟踪项目执行_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1JK411G7VF)
    - 尽量不要让一个任务多人参与，如果确实需要，可以考虑拆解为更细的任务
    - 关键路径：显示甘特 > 重要路径
    - 自定义工具栏可以设置重要路径
    - 跟踪项目执行：对应设置基线，一般在确认之后建立，创建基线之后就可以将实际完成情况与计划进行对比
    - 设置任务完成进度
    - 任务进度有变化之后，可以选择重新排程
    - 拆分任务：当投入资源中途被调用，比如出差，紧急处理其他任务
    - 过滤任务：可以指定查看某些状态下的任务
- [【OmniPlan教程】7_调整项目显示样式_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1wy4y1D7RZ)
    - 项目字体、项目颜色等
    - 自定义特殊任务样式
- [【OmniPlan教程】8_资源分级及其影响因素_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1U5411H75r)

    - 介绍自动排程的作用
    - 影响资源分级的因素(可以☑️自动资源分级)
        - 资源
        - 任务间的关联关系
        - 安排：尽早安排/尽晚安排
        - 优先级：数值越高越优先
        - 时限(容忍期)：在某个时间段内完成，按住shift键拖动任务两端即可
- [【OmniPlan系列】9 OmniPlan最后一课_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1P5411p7EE)
    - 回顾前面8集内容
    - 如何输出当前项目进度：可以自定义输出模版
    - 文件 》新建仪表盘：可以拖入多个项目的计划统一查看
- [【公开课】清华大学：项目管理的逻辑（全6讲）_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1tr4y1s74S)