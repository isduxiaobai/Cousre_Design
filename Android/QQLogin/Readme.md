# 移动应用开发--实现QQ登录界面

## 实验目的
```html
1．掌握Android中布局的概念和用法
2．熟练掌握Android中Button、ImageView、EditText以及Toast的基本使用。
3. 熟练掌握偏好设置的用法
```
## 实验要求
```html
1. 界面需要做简单屏幕适配（weight属性）
2. 用户名明文显示且只能是数字
3. 密码必须是密文显示，字符数字都可以。
4. 用户名或密码空，点击登录提示“用户名密码不能为空”
5. 用户名和密码为指定时,点击按钮提示登录成功。
6. 登录成功后，将用户名和密码保存在偏好设置中，
7. 退出QQ再次打开，记住用户名密码并显示出来
```
## 运行环境
```html
Android Studio Bumblebee | 2021.1.1 Patch 2
Build #AI-211.7628.21.2111.8193401, built on February 17, 2022
Runtime version: 11.0.11+0-b60-7590822 x86_64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
macOS 12.0.1
GC: G1 Young Generation, G1 Old Generation
Memory: 1280M
Cores: 4
Registry: external.system.auto.import.disabled=true
Non-Bundled Plugins: eu.inmite.android.plugin.butterknifezelezny (1.6.0)

API 19:Android 4.4(KitKat)

pixel 5 API 30

```
<img width="1000" alt="image" src="https://user-images.githubusercontent.com/94150810/170317224-eeee5b82-cb1f-4fcb-a0ec-76ac2d1d60a3.png">

## 项目框架
<img width="357" alt="image" src="https://user-images.githubusercontent.com/94150810/170318485-056e8c44-ad41-4db9-b9b3-4c0558236850.png">

## 运行效果图
### 实现功能：用户名或密码空，点击登录提示“用户名密码不能为空”
<img width="380" alt="image" src="https://user-images.githubusercontent.com/94150810/170318559-cf687365-742a-47c2-bd81-7ee991e0d0dd.png">

### 实现功能：用户名明文显示且只能是数字 密码必须是密文显示，字符数字都可以。
<img width="182" alt="image" src="https://user-images.githubusercontent.com/94150810/170318578-49525972-c165-47a2-9c4b-0ada3efd32bc.png">
<img width="171" alt="image" src="https://user-images.githubusercontent.com/94150810/170318618-aad96f8c-3a6c-424b-b93b-7f17a05e4f5d.png">

###  实现功能：用户名和密码为指定时,点击按钮提示登录成功。
<img width="196" alt="image" src="https://user-images.githubusercontent.com/94150810/170318649-75149d7e-9069-46b7-8420-ed6d96a9c702.png">

### 实现功能：登录成功后，将用户名和密码保存在偏好设置中       退出QQ再次打开，记住用户名密码并显示出来
<img width="331" alt="image" src="https://user-images.githubusercontent.com/94150810/170318673-b15e9251-87d2-435d-8c59-9233f1cc80c0.png">
