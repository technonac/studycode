/**
 * Created by and on 2017/6/9.
 */

window.addEventListener("load", function () {
    var form1 = document.getElementById("form1");
    form1.addEventListener("submit", function () {
        //阻止默认事件
        event.preventDefault();
        alert("event type " + event.type);
        form1.submit();
    })
});