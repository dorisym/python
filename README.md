# python
我的自学py笔记

git推送流程：本地->暂存区->远程仓库


git pull 拉代码

git status 查看修改了哪些文件

git diff 确认修改内容，本地和远程仓库对比 文件修改的内容

git add .  添加本地文件到暂存区

git commit -m "xxxx" 为本次提交写一个备注

git push origin 本地分支:远程分支  将暂存区的代码提交到远程仓库

git checkout -b 新分支名  基于当前分支创建并切换到新分支

git checkout -b 本地分支名 origin/远程分支名  基于远程分支创建并切换到新分支，新分支和远程分支一样

杨萌@DESKTOP-B9K8JG3 MINGW64 /e/notes/pythoncode/python (master1)
$ git push origin '':master1   删除远程分支master1  

git checkout -D 本地分支名   删除本地分支（删除的分支不能是当前的分支）

和远程仓库的某个分支对比 git diff origin/master 
和本地对比的时候不加origin， git diff master

复习
拉代码
再拉一下
oncemore
