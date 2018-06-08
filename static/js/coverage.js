
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