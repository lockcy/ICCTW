zip brute-attack

虽然对于传统zip压缩包加密已经有了比较完备的工具AZPR，但还是想写个脚本，可能这样更真实一点，下课回来写的比较仓促，代码也比较烂，凑合着看，有什么bug记得跟我说，在部分参考python绝技的情况下完成的。

注：

zip压缩包放在与脚本同一目录下

目前只有生成字典爆破。

如果自己有字典的话可以把字典命名为pass.txt放在脚本同目录下

如果有时间会加入掩码和明文爆破等
语法是python zipattack.py -f zipname -d  dictionary
