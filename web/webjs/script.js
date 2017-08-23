//对象
var person = {
    name: "json",
    age: 5
};

//数组
var a = [1, 2, 3, 4, 5, 6];
//window
function window_test() {
    var screenTop = window.screenTop;
    var screenLeft = window.screenLeft;
    // alert("screenTop = " + screenTop + ", screenLeft = " + screenLeft);
    // window.moveTo(0, 0); //可能被禁用
    var innerHeight = window.innerHeight;
    var innerWidth = window.innerWidth;
    var outerHeight = window.outerHeight;
    var outerWidth = window.outerWidth;
    console.log("(innerHeight,innerWidth) = " + innerHeight + " , " + innerWidth)
    console.log("(outerHeight,outerWidth) = " + outerHeight + " , " + outerWidth)

    console.log("clientWidth = " + document.documentElement.clientWidth);
    console.log("clientHeight = " + document.documentElement.clientHeight);

    // window.resizeTo(200, 200);

    //打开新窗口
    // var wroxwin = window.open("http://t.10jqka.com.cn");
    // wroxwin.opener.alert("imok"); //opener指向原来调用open()的window

    var timeoutid = setTimeout(function () {
        alert("Time out");
    }, 1000);

    clearTimeout(timeoutid); //去掉超时

    var intervalid = setInterval(function () {
        var element = document.getElementById("show_something");
        var now = new Date();
        element.innerText = now.toLocaleTimeString();
    }, 1000);

    // clearInterval(intervalid);
}
function location_test() {
    console.log(window.location === document.location);
    console.log("hash = " + location.hash);
    console.log("host = " + location.host);
    console.log("hostname = " + location.hostname);
    console.log("href = " + location.href);
    console.log("pathname = " + location.pathname);
    console.log("port = " + location.port);
    console.log("protocol = " + location.protocol);
    console.log("search = " + location.search);

    var queryStringArgs = getQueryStringArgs();
    console.log(queryStringArgs['_ijt']);
    // location.replace() //不能回到前一个页面
    // location.assign("http://t.10jqka.com.cn");
    //location.reload(); //重新加载（有可能从缓存中加载）
    // location.reload(true); //重新加载（从服务器重新加载）
}

function getQueryStringArgs() {

    //get query string without the initial ?
    var qs = (location.search.length > 0 ? location.search.substring(1) : ""),

        //object to hold data
        args = {},

        //get individual items
        items = qs.length ? qs.split("&") : [],
        item = null,
        name = null,
        value = null,

        //used in for loop
        i = 0,
        len = items.length;

    //assign each item onto the args object
    for (i = 0; i < len; i++) {
        item = items[i].split("=");
        name = decodeURIComponent(item[0]);
        value = decodeURIComponent(item[1]);

        if (name.length) {
            args[name] = value;
        }
    }

    return args;
}
function navigator_test() {
    console.log("appCodeName = " + navigator.appCodeName);
    console.log("appName = " + navigator.appName);
    console.log("appVersion = " + navigator.appVersion);
    console.log("cookieEnabled = " + navigator.cookieEnabled);
    console.log("javaEnabled() = " + navigator.javaEnabled());
    console.log("language = " + navigator.language);
    console.log("mimeTypes = " + navigator.mimeTypes);
    console.log("onLine = " + navigator.onLine);
    console.log("platform = " + navigator.platform);
    console.log("plugins = " + navigator.plugins);
    console.log("product = " + navigator.product);
    console.log("systemLanguage = " + navigator.systemLanguage);
    console.log("userAgent = " + navigator.userAgent);
    console.log("userLanguage = " + navigator.userLanguage);
    console.log("vendor = " + navigator.vendor);
    console.log("-- Plugins list --");
    for (var i = 0; i < navigator.plugins.length; i++) {
        var plugin = navigator.plugins[i];
        console.log(plugin.name);
    }

    console.log("--------------------");

    console.log("-- mimeTypes list --");
    for (var i = 0; i < navigator.mimeTypes.length; i++) {
        var type = navigator.mimeTypes[i];
        console.log(type);
    }
    console.log("--------------------");

}

function screen_test() {

}

function history_test() {
    // history.go(-1);
    history.go("http://t.10jqka.com.cn"); //查询历史记录跳转，没有记录则不执行
    // history.back();
    // history.forward();
    console.log(history.length);
}