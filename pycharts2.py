from pyecharts import  Bar
attr = ["{}月".format(i) for i in range(1,13)]
v1 = [2.0,4.9,5.0,6.0,7.0,8.0,4.5,8.6,9.6,5.4,7.6,8.5]
v2 = [2.8,4.1,8.0,7.0,9.0,4.0,2.5,9.6,7.6,3.4,9.6,4.5]
bar=Bar("柱状图示例")
bar.add("蒸发量",attr,v1,mark_line=["average"],mark_point=["max","min"])
bar.add("降水量",attr,v2,mark_line=["average"],mark_point=["max","min"])
bar.show_config()
bar.render("ss.html")