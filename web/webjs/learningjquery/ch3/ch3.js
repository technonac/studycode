/**
 * window.onload $(document).ready()区别
 *
 * (1)当文档完全下载到浏览器中时，会触发window.onload事件。这意味着页面上的全部元素对JavaScript而言都是可以操作的，
 * 这种情况对编写功能性的代码非常有利，因为无需考虑加载的次序。
 *
 * (2)另一方面，通过$(document).ready()注册的事件处理程序，则会在DOM完全就绪并可以使用时调用。
 * 虽然这也意味着所有元素对脚本而言都是可以访问的，但是，却不意味着所有关联的文件都已经下载完毕。
 * 换句话说，当HTML下载完成并解析为DOM树之后，代码就可以运行。
 *
 *
 * 为了保证JavaScript代码执行以前页面已经应用了样式，
 * 最好是在<head>元素中把<link rel="stylesheet">标签和<style>标签放在<script>标签前面。
 **/
//简写 不推荐
$(function () {

});


$(document).ready(function () {

});

