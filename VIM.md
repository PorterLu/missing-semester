# VIM

## vimtutor

### Lesson1

1. 使用`h`:左； `j`:down; 	`k`:up;	l:`right`
2. vim + filename 打开文件
3. `q!` 用于退出； `wq`用于保存并且退出
4. `i` 进入insert模式，并且`A`也会进入insert模式，并且自动将光标移动到下一行。

### Lesson2

	1. `dw` 可以删去一个单词
	1. `d$` 删除至行尾
	1. `dd` 删除一整行
	1. 重复动作，如`2w` 可以移动两个单词的位置
	1. opertator + [number] + motion, 如`d2w`
	1. 直接键入0，可以移动光标到行首
	1. 键入u，可以undo之前的行为

### Lesson3

1. delete掉一个行之后，键入`p` 可以将删除的数据直接拷贝到光标处

​	2.键入`r`可以直接替换一个字符

​	3.`c`可以执行change动作，直接删除一个单词，并进入insert模式

### Lesson4

1. 键入`ctrl + g` 可以显示当前所在行

2. 键入`G`可以直接到达文件尾, 键入`gg` 可以直接到达文件的头部
3. 键入`/`，可以进行搜索
4. 在括号处，键入`%`，可以自动找到匹配的括号
5. 在命令模式下，
   * 键入`s/old/new/g` 可以进行全局替换
   * 键入`#,#/old/new/g`可以指定范围进行版本替换
   * 键入`%s/old/new/g`可以进行全局替换

### Lesson5

 	1. 在命令模式下，键入`!` 可以直接执行shell命令
 	2. `w + filename`直接将文件内容输出到filename中
 	3. 通过`v`进行选择后，在命令模式下进行`w`可以将选择的内容输出到文件
 	4. `r + filename` 可以将文件的内容输入到光标处

### Lesson6

1. `o`可以进行insert模式，不过光标会自动出现在下一行
2. `a`可以直接在光标后进行insert,`A`会在一行的行尾进行assert
3. `y` 可以对`v`的内容进行拷贝，最后通过`p`进行输出
4. `R`可以直接进入替换模式，对光标处的数据进行替换

### Lesson7

	1. 键入`help`可以打开帮助界面
	1. 通过`ctrl + w` 可以进行窗口跳转
	1. `vimrc`可以对vim进行配置

## 多窗口

使用`sp` 和 `vsp` 进行打开

## 宏

1. 使用`q`将上一个字符可以进行宏录制，再次键入`q`可以停止宏的录制。录制完成后可以使用`@` + 字符，重放这个宏

2. 使用一个数字 + `@` + 宏编号可以重复调用宏。

3. 使用`q字符q` 可以清除一个宏
4. 宏也可以进行递归

## 配置VIM

```shell
mkdir -p ~/.vim/pack/vendor/start
cd ~/.vim/pack/vendor/start
git clone https://github.com/ctrlpvim/ctrlp.vim
```

配置`~/.vimrc`中加入

```shell
set runtimepath^=~/.vim/pack/vendor/start/ctrlp.vim 
```

同时配置使用`ctrl + P` 打开

```shell
 let g:ctrlp_map ='<c-p>' 
 let g:ctrlp_cmd = 'CtrlP'
 let g:ctrlp_working_path_mode = 'ra' #设置默认路径为当前路径
```

安装插件管理工具

```shell
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

添加`~/.vimrc`

```shell
 call plug#begin()
 Plug 'preservim/NERDTree' #需要安装的插件 NERDTree
 Plug 'wikitopian/hardmode'  #安装 hardmode
 call plug#end()
```

进入VIM，使用`:PlugInstall`进行安装

```shell
:NERDTree
```

可以打开管理窗口。

