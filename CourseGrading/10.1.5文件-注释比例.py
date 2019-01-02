"""
【问题描述】
一个好的程序要有一定比例的注释。编写一个程序统计一个C源文件中注释所占的百分比。百分比计算公式为：程序注释中字符总数（/*和*/除外的所有字符）除以程序文件中总字符数（程序文件中的所有字符）。
注：只考虑/*  */内的注释，而且要考虑注释跨行的情况。不要考虑其它情况，比如//打头的行注释，比如/*或*/作为字符串的子串的情况。
【输入形式】
从当前目录下的filein.c源程序文件获得输入。
【输出形式】
向控制台输出注释所占百分比，百分数无小数（小数部分直接截掉，不要四舍五入），后跟百分号%。
【样例输入】
假设filein.c的内容为：
void main()
{
FILE * in;
/*Open the file*/
if((in=fopen("in.txt","r"))==NULL)
{
printf("Can&rsquo;t open in.txt!");
return;
}
/*Close the file,
and return.*/
fclose(in);
}
【样例输出】
22%
【样例说明】
filein.c文件的总字符数为179，注释中的字符数为41，则注释所占百分比为22%。
【评分标准】
该题要求输出注释所占百分比，共有5个测试点。
"""
with open("filein.c") as codes:
    c = codes.read()

words = ""
for i in range(len(c)):
    if c[i] == "/" and c[i + 1] == "*":
        start = i + 2
    if c[i] == "*" and c[i + 1] == "/":
        end = i - 1
    words += c[start : end]
print(len(c))
print(len(words))


