
function drawLine(id, data) {
    var myChart = echarts.init(document.getElementById(id));
    console.log(myChart)
    var option = {
        xAxis: {
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
    myChart.setOption(option);
}

function http(url, data, method, success, fail) {
    data = method == 'GET' ? data : JSON.stringify(data)
    console.log(data);
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