
function success(data) {
    console.log(data)
    line = []
    branch = []
    data = data['data']
    for (var i=0; i<data.length; i++) {
        line.push(data[i]['line']['rate'])
        branch.push(data[i]['branch']['rate'])
    }
    drawLine('line', line)
    drawLine('branch', branch)
}

function fail(data) {
    console.log(data)
}

function http(url, data, method, success, fail) {
    data = method == 'GET' ? data : JSON.stringify(data)
    $.ajax({
        url: url,
        type: method,
        dataType: 'json',
        contentType: 'application/json; charset=UTF-8',
        data: data,
        success: success,
        error: fail
    });
}

function drawLine(id, data) {
//    基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById(id));
    console.log(myChart)
//    指定配置项及数据
    var option = {
        xAxis: {                //X轴
            type: 'category',
            data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: data,
            type: 'line',
            smooth: true
        }]
    };

//    使用刚指定的配置项和数据绘制图表
    myChart.setOption(option);
}

function search() {
    var data = {
        'collection': 'coverage',
        'limit': 10,
        'skip': 0
    }
    console.log(data)
    var url = 'http://127.0.0.1:9999/api/v1/search'
    http(url, data, 'GET', success, fail)
}

$(function () {
    search()
});