## Shell脚本

## 变量	

​	在bash为变量赋值的语句是`foo = bar`, 访问变量中存储的值，它的语法是$foo。需要注意的是, `foo = bar` 这样使用空格隔开是不能正常工作的，因为shell会将`=`和`bar`作为foo的参数。

​	Bash中通过`'`或者`"`来定义字符串，但是它们的含义并不相同。以`'`定义字符串为原义字符串，其中的变量不会被转化，但是使用`"`定义的字符串会将变量值进行替换。

```shell
foo=bar
echo "$foo"
echo '$foo'
```

## 控制流

​	bash也支持`if`, `case`,`while`和`for`这些控制流关键字。同样地，bash也支持函数，它可以接受参数，并给予参数进行操作。

```shell
mcd(){
	mkdir -p "$1"
	cd "$1"
}
```

参数说明如下：

* `$0`: 脚本名
* `$1` 到 `$9` 脚本的参数。`$1`是第一个参数，依此类推
* `$@`: 所有参数
* `$#`: 参数个数
* `$?`:上一个命令的返回值
* `$$`: 当前脚本的进程识别码
* `!!`: 完整的上一条命令

* `$_`:上一个命令的最后一个参数

短路运算有下列的例子：

```shell
false || echo "Oops, fail"
true  || echo "Will not be printed"
true  && echo "Things went well"
false && echo "Will not be printed"
false ; echo "This will always run"
```

```shell
echo "Starting program at $(date)"
echo "Running program $0 with $# argument with pid $$"

for file in "$@"; do
	grep foobar "$file" > /dev/null 2> /dev/null
	if [[ $? -ne 0 ]]; then
		echo "File $file does not have any foobar, adding one"
		echo "# foobar" >> "$file"
	fi
done
```

​	`grep foobar “$file” > /dev/null 2 > /dev/null` 可以将输出结果输出到空设备，同时将错误的信息也输入到空设备。

​	这里`$(date)`会先执行`date` 命令进行输出，同时如果`<(CMD)`会CMD并将结果输出到一个临时的文件。

## 通配符

* 可以使用`?` 和 `*` 分别匹配一个或者任意个字符。
* `{}`可以进行说明一段公共的子串

```shell
convert image.{png, jpg}
```

## shell工具

### tldr	

​	tldr可以输出比man更友好的信息。

### 查找文件

```shell
find . -name src -type d ##查找src目录下的所有目录
find . -path '*/test/*.py' -type f
find . -mtime -1 		 ##查找修改时间小于1天的所有文件
find . -size +500k -size -10M -name '*.tar.gz'
```

​	除了列出所寻找的文件外，find还能对找到的文件进行操作，这能简化一些步骤。

```shell
find . -name '*.tmp' -exec rm {} \;
find . -name '*.png' -exec convert {} {}.jpg \; 
```

​	如上的命令，可以使用`{}`代表找到的文件，同`-exec`参数执行对应的命令。

### 查找代码

​	grep命令：

* `-C`可以查找上下文
* `-v`可以进行反向匹配
* `-R`会进入文件夹进行递归匹配

### 查找shell命令

```shell
histroy | grep find
```

### 文件夹导航

​	`ln -s` 可以进行连接创建

## 题目

1. 使用`-a`, `-h`, `-lt` ,`--color=auto` 进行ls的输出配置

2. 

```shell
#!/bin/bash
macro(){
	echo "$(pwd)" > $HOME/macro_history.log
	echo "save pwd $(pwd)"
}

polo(){
	cd "$(cat "$HOME/macro_history.log")"
}
```

3. 

其中&是一个描述符，如果1或者2前面不加&，会被当成一个普通文件

* 1>&2, 意思是将标准输出重定向到标准错误
* 2>&1, 意思是将标准错误重定向到标准输出
* &>filename, 意思是将标准输出和标准错误都重定向到文件filename中

```shell
n=$(( RANDOM % 100 ))

if [[ n -eq 42 ]]; then
	echo "Something went wrong"
	>&2 echo "The error was using magic numbers"
	exit 1
fi

echo "Everything went according to plan"
```

```shell
count=1
while true
do 
	./buggy.sh 2> out.log
	if [[ $? -ne 0 ]]; then
		echo "failed after $count times"
		cat out.log
		break
	fi
	((count++))
done
```

4. 

```shell
  find . -type f -name "*.html" | xargs -d '\n'  tar -cvzf html.zip
```

5.

```shell
find . -type f -mmin -60 -print0 | xargs -0 ls -lt | head -10
```



