<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<%@ taglib prefix="x" uri="http://java.sun.com/jsp/jstl/xml" %>

<html>
<head>
    <title>xml</title>
</head>
<body>
<div class="parse">
    <!-- 相当于java中的SAXParser、DOMParser  -->
    <x:parse var="content">
        <student description="im a description">
            <name>Tom</name>
            <age>20</age>
        </student>
    </x:parse>
    Desc: <x:out select="$content/student/@description"/><br/>
    name: <x:out select="$content/student/name"/><br/>
    age: <x:out select="$content/student/age"/><br/>
    <%--
    $开头为jstl或者jsp自定义的变量
    /表示父子关系或者所属关系
    @表示属性
    名称前什么都没有表示是节点
    --%>
</div>
<div class="parse-equal">
    <c:set var="xmltoparse">
        <student description="im a description">
            <name>Tom</name>
            <age>20</age>
        </student>
    </c:set>
    <x:parse var="content" doc="${xmltoparse}"/>
    <%--doc:要解析的xml内容--%>
    <%--var:解析后的xml对象--%>
</div>

<div class="foreach">
    <x:forEach select="$content">

    </x:forEach>
</div>
</body>
</html>
