
function success(data) {
    console.log(data)
}

function fail(data) {
    console.log(data)
}

function browser() {
    var html = '\
    <div class="row" command="browser">\
        <label>打开：</label>\
        <input type="text" placeholder="http://www.testfan.com/">\
    </div>\
    '
    $('#cases').append(html)
}

function find() {
    var html = '\
    <div class="row" command="find">\
        <label>使用：</label>\
        <select>\
            <option value="xpath">xpath</option>\
            <option value="css selector">css selector</option>\
            <option value="name">name</option>\
        </select>\
        <label>参数：</label>\
        <input type="text">\
    </div>\
    '
    $('#cases').append(html)
}

function keys() {
    var html = '\
    <div class="row" command="keys">\
        <label>填写：</label>\
        <input type="text">\
    </div>\
    '
    $('#cases').append(html)
}

function action() {
    var html = '\
    <div class="row" command="action">\
        <label>动作：</label>\
        <select>\
            <option value="click">click</option>\
        </select>\
    </div>\
    '
    $('#cases').append(html)
}

function add_element() {
    var command = $('#option').val()
    if (command == 'browser') {
        browser();
    } else if (command == 'find') {
        find();
    } else if (command == 'keys') {
        keys()
    } else if (command == 'action') {
        action()
    } else {
        alert("错误的方法！")
    }
}

function parse_parameters(html) {
    var data = {}
    var command = $(html).attr("command")
    if (command == 'browser') {
        data['command'] = 'browser';
        data['parameters'] = {
            'url': $(html).find('input').val()
        }
    } else if (command == 'find') {
        data['command'] = 'find';
        data['parameters'] = {
            'by': $(html).find('select').val(),
            'value': $(html).find('input').val()
        }
    } else if (command == 'keys') {
        data['command'] = 'keys';
        data['parameters'] = {
            'value': $(html).find('input').val()
        }
    } else if (command == 'action') {
        data['command'] = 'action';
        data['parameters'] = {
            'action': $(html).find('select').val()
        }
    }else {
        console.log("错误的HTML！")
    }
    console.log(data)
    return data;
}

function run() {
    var list = $('#cases').find('div');
    var data = {
        'commands': []
    };
    $(list).each(function(index, item){
        var command = parse_parameters(item)
        data['commands'].push(command)
    });
    console.log(data)
    var url = 'http://127.0.0.1:9999/function/api';
    http(url, data, 'POST', success, fail);
}

$(function () {
    $('#command').click(add_element);
    $('#run').click(run);
});