# Git

## Git数据模型

### 快照

​	Git将顶级目录中的文件和文件夹作为集合，并通过一系列快照来管理其历史记录。在Git的术语里，文件被称为Blob对象，也就是一组数据。目录则被称之为树，它将名字和Blob或者树对象进行映射。快照就是被追踪的最顶层的树

```markdown
<root> (tree)
|
+- foo (tree)
|	|
|	+ bar.txt(blob, content = "hello world")
|
+- baz.txt(blob, content = "git is wonderful")
```

### 关联快照

​	在Git中，历史记录是由快照组成的有向无环图，这意味着每个快照都有一系列的父辈，注意快照具有多个”父辈“而并非一个，因为某个快照可能由多个父辈而来。在Git中这些快照被称为提交。

```
o <-- o <-- o <-- o <---- o
			^			 /
			 \			v
			  --- o <-- o
```

