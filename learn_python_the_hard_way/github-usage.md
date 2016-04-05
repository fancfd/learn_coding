# 本地代码上传到github

## 注册github账号

## github配置

### 设置公钥，并测试

- 本地生成密钥对

        $ ssh-keygen -t dsa

- 上传公钥

    到GitHub中，点击右上角的account settings，然后选择左边栏中的SSH Keys添加SSH Key，粘贴刚才复制的内容到Key文本框中，title文本框随意填写

- 测试公钥

         $ ssh git@github.com

### 配置用户名与电子邮件

    git config --global user.name “YourName”
    git config --global user.email “YouEmailAddress”

## 在Github上建立github仓库
Learn Ruby The Hard Way

## 创建本地仓库并上传代码到GitHub

* 新建Text文件夹作为仓库根目录（文件夹名字随意命名）

* 将需要上传的代码文件加入到Text根目录

* 在根目录下建立仓库，先进入到Text根目录下，再输入```git init```（初始化一个仓库）

* 将所有文件添加到仓库，输入下面命令：```git add .```

* 提交，输入下面命令：
```
git commit -m “CommitInfo”
```

* 添加源到GitHub
```
git remote add origin git@github.com:YourName/YourRepositroy.git
```

* 上传源到GitHub

```
git push -u origin master
```
