
var editor = null;

function ace_editor() {
    //初始化对象
    var editor = ace.edit("editor");
    //设置风格和语言（更多风格和语言，请到github上相应目录查看）
    editor.setTheme("ace/theme/clouds");
    editor.getSession().setMode("ace/mode/python");
    return editor;
}

function get_parameters() {

    var data = {
        'param': {},
        'header': {},
        'code': editor.getValue()
    }

    console.log(editor.getValue())

    data['method'] = $('#method').val();

    data['url'] = $('#url').val();

    $('.h_key').each(function (index, element) {
        var key = $('.h_key').eq(index).val();
        var value = $('.h_value').eq(index).val();
        data['header'][key] = value;
    })

    $('.p_key').each(function (index, element) {
        var key = $('.p_key').eq(index).val();
        var value = $('.p_value').eq(index).val();
        data['param'][key] = value;
    })

    console.log(data);
    return data;
}

function add_header() {
    $('#h_section').show();
    $('#h_section').append('<div class="row">key:<input class="h_key">value:<input class="h_value"></div>')
}

function add_parameter() {
    $('#p_section').show()
    $('#p_section').append('<div class="row">key:<input class="p_key">value:<input class="p_value"></div>')
}

function success(data) {
    console.log(data)
    $('#r_section').show();
    $('#r_section').append('<div>' + JSON.stringify(data['data']) + '</div>')
    alert(data['message'])
}

function fail(data) {
    console.log(data)
}

function send_request() {
    var data = get_parameters();
    var url = "http://127.0.0.1:9999/interface/handler"
    http(url, data, 'POST', success, fail)
}

$(function () {
    editor = ace_editor();

    $('#p_section').hide();
    $('#h_section').hide();
    $('#r_section').hide();

    $('#param').click(add_parameter);
    $('#header').click(add_header);
    $('#send').click(send_request);
});