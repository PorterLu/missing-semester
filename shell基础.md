# shell基础

## shell环境

​	shell是一个编程环境，所以它具备变量、条件、循环和函数。当在shell中执行命令时，实际上是在执行一个简短的代码。如果要执行某一个指令，shell会去咨询环境变量。

```shell
echo $PATH
which echo
```

​	shell会在$PATH中寻找所要执行的程序，如果确定某个程序名代表某个程序，也可以使用which程序进行指定。

## 基本命令

​	ls、cd、mv、cp、mkdir等等。

## 重定向和管道

​	重定向可以将流定位到文件，同时管道可以将一个程序的输出作为另外一个程序的输入

## 根用户

```shell
sudo find -L /sys/class/backlight -maxdepth 2 -name "*brightness"
cd /sys/class/backlight/thinkpad_screen
sudo echo 3 > brightness
```

## 习题答案

```shell
./semester | grep last-modified > ~/last-modified.txt
```

