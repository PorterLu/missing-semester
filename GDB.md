# GDB

## 启动GDB

使用`gdb + 可执行文件名` 就可以启动gdb。

## 断点

设置断点可以直接通过`b 函数名`的方法进行设置。也可通过如下的方法进行设置

```
break 函数名
break 行号
break 文件名:行号
break 文件名:函数名
break +偏移量
break -偏移量
break *地址
```

## 运行

可以直接键入`run`或者`start`开始运行。

## 显示栈帧

`backtrace`命令可以在遇到断点而暂停执行时显示栈帧，也可以使用`bt`或者`info stack`

`bt N` 可以显示前N个栈帧，同时`bt -N`可以显示最后N个栈帧，如果加上`full`还会显示局部变量。

## 显示寄存器

可以直接键入`info reg`，还可以通过`p $eax` 等直接输出某个寄存器的值

```
p/格式 变量 可以控制输出的格式
x 显示16进制格式
d 显示10进制格式
u 显示无符号10进制数
o 显示8进制数
t 显示为二进制
a 地址
c 显示为ascii码
s 显示为字符串
i 显示为机器语言
```

## 扫描内存

使用`x $pc`就可以显示pc处内存中存储的值，格式可以使用p的格式

## 反汇编

使用`disas`可以进行反汇编，可以使用`disas $pc $pc+50` 进行反汇编

## 单步执行

使用`next`可以继续执行源代码中的下一条执行，`nexti`不会进入函数

## 继续执行

使用`continue` 可以运行程序知道下一个断点，加上num，可以表示越过几个断点。

## 监视点

 `watch <表达式>` 还可使用`awatch`和`rwatch`监视被访问被读取时进行暂停。

## 删除断点

可以使用`d`命令删除断点和监视点

## 生成core文件

使用`generate-core-file`生成核心转储文件

## record and replay

gdb 可以记录程序的当前执行状态并进行返回，使用record full 可以开启记录功能。  
* record goto begin： Go to the beginning of the execution log.
* record goto end： Go to the end of the execution log.
* record goto n： Go to instruction number n in the execution log. 
