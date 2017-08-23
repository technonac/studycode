/**
 * Created by and on 2017/6/7.
 */
function dom_test() {
    console.log("nodeType = " + document.nodeType);
    console.log("nodeName = " + document.nodeName);
    console.log("nodeValue = " + document.nodeValue);
    var html = document.documentElement; //取得对<html>的引用
    console.log(html === document.childNodes[0]); //true
    console.log(html === document.firstChild); //true
    var body = document.body;

    console.log("title = " + document.title);
    console.log("URL = " + document.URL);
    console.log("referrer = " + document.referrer);
    console.log("domain = " + document.domain);
    console.log(document.implementation);

    // document.write(new Date().toString());

    // var element = document.getElementById("myList");
    // console.log(element.childNodes.length);
}

/**
 * dom 扩展
 */
function dom_ext_test() {
    var body = document.querySelector("body");
    console.log(body.nodeName);
    var mydiv = document.querySelector("#myList");
    console.log(mydiv.nodeName);
    var all = document.querySelectorAll(".selected");
    var activeElement = document.activeElement;

    console.log("charset = " + document.charset);

    var innertest = document.querySelector("#inner-test");
    console.log("innerHTML = " + innertest.innerHTML);
    console.log("outerHTML = " + innertest.outerHTML);
    console.log("innerText = " + innertest.innerText);
    innertest.style.background = "#a7ecf6";
    console.log("cssText = " + innertest.style.cssText);
}