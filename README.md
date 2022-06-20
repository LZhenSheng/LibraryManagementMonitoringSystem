# 基于树莓派和RFID技术的智能图书管理监控系统（嵌入式课设）
## 1.环境

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E7%A1%AC%E4%BB%B6%E6%88%90%E5%93%81%E5%9B%BE.jpg)

### 1.1软件环境

|  类型   | 名称  |
|  ----  | ----  |
| 云数据库  | Bmob |
| 本地数据库  | Sqlite |
| 界面框架  | wxPython |
| 开发语言  | Python |

### 1.2硬件环境

| 名称  |
| ----  |
| MF RC-522读卡器 |
| RFID射频 |
| IC卡感应模块 |
| 源蜂鸣器模块(低电平触发) |
| HC-SR501人体红外感应模块 |
| 500万像素广角CSI视频摄像头 |

## 2.软件架构

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E7%B3%BB%E7%BB%9F%E7%BB%93%E6%9E%84%E5%9B%BE.png)

## 3.界面

(1)修改密码界面

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E4%BF%AE%E6%94%B9%E5%AF%86%E7%A0%81%E7%95%8C%E9%9D%A2.png)

(2)借阅历史查询结果弹窗界面

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E5%80%9F%E9%98%85%E5%8E%86%E5%8F%B2%E6%9F%A5%E8%AF%A2%E7%BB%93%E6%9E%9C%E5%BC%B9%E7%AA%97%E7%95%8C%E9%9D%A2.png)

(3)借阅查询历史界面

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E5%80%9F%E9%98%85%E6%9F%A5%E8%AF%A2%E5%8E%86%E5%8F%B2%E7%95%8C%E9%9D%A2%20.png)

(4)图书借阅界面

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E5%9B%BE%E4%B9%A6%E5%80%9F%E9%98%85%E7%95%8C%E9%9D%A2.png)

(5)图书归还界面

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E5%9B%BE%E4%B9%A6%E5%BD%92%E8%BF%98%E7%95%8C%E9%9D%A2.png)

(6)失败弹窗界面

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E5%A4%B1%E8%B4%A5%E5%BC%B9%E7%AA%97%E7%95%8C%E9%9D%A2.png)

(7)成功弹窗界面

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E6%88%90%E5%8A%9F%E5%BC%B9%E7%AA%97%E7%95%8C%E9%9D%A2.png)

(7)登录界面

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2.png)

(8)馆藏查询界面

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E9%A6%86%E8%97%8F%E6%9F%A5%E8%AF%A2%E7%95%8C%E9%9D%A2%20.png)

(10)馆藏查询结果弹窗界面

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E9%A6%86%E8%97%8F%E6%9F%A5%E8%AF%A2%E7%BB%93%E6%9E%9C%E5%BC%B9%E7%AA%97%E7%95%8C%E9%9D%A2.png)

(11)验证密码界面

![1655494134977](https://github.com/lijianxing66628/LibraryManagementMonitoringSystem/blob/main/images/%E9%AA%8C%E8%AF%81%E5%AF%86%E7%A0%81%E7%95%8C%E9%9D%A2.png)

## 4.不足之处
（1）界面太丑
