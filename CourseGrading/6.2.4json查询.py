"""
【问题描述】
　　JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式，可以用来描述半结构化的数据。JSON 格式中的基本单元是值 (value)，出于简化的目的本题只涉及 2 种类型的值：
　　* 字符串 (string)：字符串是由双引号 " 括起来的一组字符（可以为空）。如果字符串的内容中出现双引号 "，在双引号前面加反斜杠，也就是用 \" 表示；如果出现反斜杠 \，则用两个反斜杠 \\ 表示。反斜杠后面不能出现 " 和 \ 以外的字符。例如：""、"hello"、"\"\\"。
　　* 对象 (object)：对象是一组键值对的无序集合（可以为空）。键值对表示对象的属性，键是属性名，值是属性的内容。对象以左花括号 { 开始，右花括号 } 结束，键值对之间以逗号 , 分隔。一个键值对的键和值之间以冒号 : 分隔。键必须是字符串，同一个对象所有键值对的键必须两两都不相同；值可以是字符串，也可以是另一个对象。例如：{}、{"foo": "bar"}、{"Mon": "weekday", "Tue": "weekday", "Sun": "weekend"}。
　　除了字符串内部的位置，其他位置都可以插入一个或多个空格使得 JSON 的呈现更加美观，也可以在一些地方换行，不会影响所表示的数据内容。例如，上面举例的最后一个 JSON 数据也可以写成如下形式。
　　{
　　"Mon": "weekday",
　　"Tue": "weekday",
　　"Sun": "weekend"
　　}
　　给出一个 JSON 格式描述的数据，以及若干查询，编程返回这些查询的结果。
【输入形式】
　　第一行是两个正整数 n 和 m，分别表示 JSON 数据的行数和查询的个数。
　　接下来 n 行，描述一个 JSON 数据，保证输入是一个合法的 JSON 对象。
　　接下来 m 行，每行描述一个查询。给出要查询的属性名，要求返回对应属性的内容。只需要支持顶层的查询。保证查询的格式都是合法的。
【输出形式】
　　对于输入的每一个查询，按顺序输出查询结果，每个结果占一行。
　　查询结果必定是字符串的值，输出该字符串。
　　如果查询结果不存在，则输出 NOTEXIST。
【样例输入】
10 2
{
"firstName": "John",
"lastName": "Smith",
"address": {
"streetAddress": "2ndStreet",
"city": "NewYork",
"state": "NY"
},
"esc\\aped": "\"hello\""
}
firstName
secondName
【样例输出】
John
NOTEXIST
【提示】
对于一段json文本，上述样例输入中的第2到第11行组成的文本，调用json模块的loads方法可以生成json对象（也就是python的字典）。写法如：
import json
json_dict = json.loads(json_text)
上述代码中，json_text是一段完整的json文本。
利用json.loads方法，你无须特别处理如下符号：\", \\  。
"""
import json
n, m = input().split()
n = int(n)
m = int(m)
json_text = {}
for i in range(n):
    text = input()
    if ":" in text:
        text = text.split(":")
json_dict = json.loads(json_text)
print(json_dict)
