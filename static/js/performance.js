var editor = null

function success(data){
    console.log(data)
}

function fail(data){
    console.log(data)
}

function get_parameters(){
    var data={
        'host':$('#host').val(),
        'user':$('#user').val(),
        'qps':$('#qps').val(),
        'count':$('#number').val(),
        'code':editor.getValue(),
    }

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

function start(){
    var data = get_parameters()
    console.log(data)
    var url = "/performance/handler"
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
    $('#send').click(start)
});

