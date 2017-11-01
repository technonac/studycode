/**
 * Created by and on 2017/6/16.
 */
$(document).ready(function () {


    console.log("ready!!!");

    $('#submit').click(function () {
        if ($('#user').val() == "" || $('#pwd').val() == "") {
            $('#tips').text("请输入用户名/密码 ");
            $('#tips').show();
        }
        $.post(
            'form_test.php',
            {
                name: $('#user').val(),
                password: $('#pwd').val()
            },
            function (data) {
                console.log(data);
            });
    });


    $('#ajax-get').click(function () {

        $.ajax({
            url: 'http://t.10jqka.com.cn/api.php?method=game.showNotice&id=71&cookie=123',
            method: 'get',
        }).done(function (data) {
            alert(data);
        });
    });
});