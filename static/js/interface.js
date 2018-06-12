var editor = null

function add_parameter() {
    $('#p_section').show();
    $('#p_section').append('<div class="row">key:<input class="p_key">value:<input class="p_val"></div>')
}

function add_header() {
    $('#h_section').show();
    $('#h_section').append('<div class="row">h_key:<input class="h_key">h_value:<input class="h_val"></div>')
}

function success(data){
    console.log(data)
    $('#r_section').show();
    $('#r_section').append('<div>' + JSON.stringify(data['data']) + '</div>')
    alert(data['message'])
}

function fail(data){
    console.log(data)
}

function get_parameters(){
    var data={
        'param':{},
        'header':{},
        'code':editor.getValue(),
    }

    data['method'] = $('#method').val();
    data['url'] = $('#url').val();

    $('.h_key').each(function(index,element){
        var key = $('.h_key').eq(index).val();
        var value = $('.h_val').eq(index).val();
        data['header'][key] = value
    })

    $('.p_key').each(function(index,element){
        var key = $('.p_key').eq(index).val();
        var value = $('.p_val').eq(index).val();
        data['param'][key] = value;
    })

    console.log(data);
    return data
}

function http(url, data, method, success, fail) {
    data = method == 'GET' ? data : JSON.stringify(data)        //将data转化为json字符串
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

function send_request(){
    var data = get_parameters()
    console.log(data)
    var url = "/interface/handler"
    http(url,data,'POST',success,fail)
}

function ace_editor() {
    //初始化对象
    var editor = ace.edit("editor");        //获取editorid并初始化对象
    //设置风格和语言（更多风格和语言，请到github上相应目录查看）
    editor.setTheme("ace/theme/clouds");
    editor.getSession().setMode("ace/mode/python");
    return editor;
}

$(function () {
    editor = ace_editor();          //页面加载时初始化editor

    $('#p_section').hide();
    $('#h_section').hide();
    $('#r_section').hide();

    $('#param').click(add_parameter);
    $('#header').click(add_header);
    $('#send').click(send_request)
});

