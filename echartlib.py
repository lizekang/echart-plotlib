
# coding: utf-8

# In[1]:


from IPython.display import HTML


# In[27]:


class echartlib(object):
    def __init__(self, width=600, height=450):
        self.head = """
            <div id="mychart" style="width:"""+str(width)+"""px; height:"""+str(height)+"""px;"></div>
            <script>
            require.config({
                paths:{
                    echarts:"//cdn.bootcss.com/echarts/3.2.3/echarts.min",
                }
            })
            require(['echarts'], function(ec){
                var mychart = ec.init(document.getElementById('mychart'));
                var option;
        """

        self.tail = """
                mychart.setOption(option);
            })
            </script>
        """
    
    def plot_else(self, data_name, xAxis_data, yAxis_data, title=None):
        option = {
            "title" : {
                "text": '',
                "subtext": "",
                "x":"center"
            },
            "calculable" : "true",
            "legend": {
                "x":"right",
                "orient" : 'vertical',
                "data":["CLPRB"],
                "textStyle": {
                   "fontSize": 12
                }
            },
            "series" : [
                {
                    "name":"CLPRB",
                    "type":"line",
                    "stack": "总量",
                    "itemStyle": {"normal": {"areaStyle": {"type": "default"}, "label": {"textStyle": {"fontSize": 20}}}},
                    "data":[]
                }
            ],
            "toolbox": {
                "x":'left',
                "show" :"true",
                "orient":"vertical",
                "feature" : {
                    "mark" : {"show": "false"},
                    "dataView" : {"show": "false", "readOnly": "false"},
                    "magicType" : {"show": "false", "type": ["line", "stack", "tiled", "bar"]},
                    "restore" : {"show": "false"},
                    "saveAsImage" : {"show": "true"}
                }
            },
            "tooltip" : {
                "trigger": "axis"
            },

            "xAxis" : [
                {
                    "type" : "category",
                    "boundaryGap" : "false",
                    "data" : []
                }
            ],
            "yAxis" : [
                {
                    "type" : "value"
                }
            ]
        }
        if title:
            option["title"]["text"] = title
        option["legend"]["data"] = data_name
        option["xAxis"][0]["data"] = xAxis_data
        series = []

        for i in range(len(data_name)):
            series_per = {
                "name":"",
                "type":'line',
                "stack": '总量',
                "itemStyle": {"normal": {"areaStyle": {"type": 'default'}}},
                "data":[]
            }
            series_per["name"] = data_name[i]
            series_per["data"] = yAxis_data[i]
            series.append(series_per)
        option["series"] = series
        return self.head+"option="+str(option)+self.tail
    
    def plot_line(self, data_name, xAxis_data, yAxis_data, title=None):
        option = {
            "title" : {
                "text": '',
                "subtext": "",
                "x":"center"
            },
            "tooltip" : {
                "trigger": 'axis'
            },
            "legend": {
                "x":"right",
                "orient" : 'vertical',
                "data":['最高气温'],
                "textStyle": {
                   "fontSize": 12
                }
            },
            "toolbox": {
                "x":'left',
                "show" : "true",
                "orient":"vertical",
                "feature" : {
                    "mark" : {"show": "true"},
                    "dataView" : {"show": "true", "readOnly": "false"},
                    "magicType" : {"show": "true", "type": ['line', 'bar',"tiled"]},
                    "restore" : {"show": "true"},
                    "saveAsImage" : {"show": "true"}
                }
            },
            "calculable" : "true",
            "xAxis" : [
                {
                    "type" : 'category',
                    "boundaryGap" : "false",
                    "data" : ['周一','周二','周三','周四','周五','周六','周日']
                }
            ],
            "yAxis" : [
                {
                    "type" : 'value'
                }
            ],
            "series" : [
                {
                    "name":'最高气温',
                    "type":'line',
                    "data":[11, 11, 15, 13, 12, 13, 10]
                }
            ]
        }
        if title:
            option["title"]["text"] = title
        option["legend"]["data"] = data_name
        option["xAxis"][0]["data"] = xAxis_data
        series = []
        for i in range(len(data_name)):
            series_per = {
                "name":"",
                "type":'line',
                "data":[]
            }
            series_per["name"] = data_name[i]
            series_per["data"] = yAxis_data[i]
            series.append(series_per)
        option["series"] = series
        return self.head+"option="+str(option)+self.tail
    
    def plot_pie(self, data_name, data, title=None):
        option = {
            "title" : {
                "text": '',
                "subtext": '',
                "x":'center'
            },
            "tooltip" : {
                "trigger": 'item',
                "formatter": "{a} <br/>{b} : {c} ({d}%)"
            },
            "legend": {
                
                "orient" : 'vertical',
                "x":'right',
                "data":[]
            },
            "toolbox": {
                "x":'left',
                "orient" : 'vertical',
                "show" : "true",
                "feature" : {
                    "mark" : {"show": "true"},
                    "dataView" : {"show": "true", "readOnly": "false"},
                    "magicType" : {
                        "show": "true", 
                        "type": ['pie']
                    },
                    "restore" : {"show": "true"},
                    "saveAsImage" : {"show": "true"}
                }
            },
            "calculable" : "true",
            "series" : [
                {
                    "name": "",
                    "type":'pie',
                    "radius" : '55%',
                    "center": ['50%', '60%'],
                    "data":[]
                }
            ]
        }
        option["legend"]["data"] = data_name
        series_data = []
        for i in range(len(data_name)):
            temp = {}
            temp["value"] = int(data[i])
            temp["name"] = data_name[i]
            series_data.append(temp)
        option["series"][0]["data"] = series_data
        return self.head+"option="+str(option)+self.tail

