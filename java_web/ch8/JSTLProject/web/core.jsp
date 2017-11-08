<%@ page import="java.util.HashMap" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%
    request.setAttribute("map", new HashMap<>());
    request.setAttribute("somethingremove", new HashMap<>());
%>
<html>
<head>
    <title>jstl</title>
</head>
<body>
<div class="cout">
    action = <c:out value="${param.action}" escapeXml="true"></c:out>
</div>
<div class="if">
    <c:if test="${param.action == 'hello'}">
        <c:out value="Hello c:if"></c:out>
    </c:if>
</div>
<div class="ifelse">
    <c:choose>
        <c:when test="${param.action == 'hello'} ">
            <c:out value="c:when"></c:out>
        </c:when>
        <c:otherwise>
            <c:out value="c:otherwise"></c:out>
        </c:otherwise>
    </c:choose>
</div>
<div class="foreach">
    <table border="1px" cellpadding="0" cellspacing="0">
        <thead>
        <tr>
            <td>num</td>
            <td>varStatus.index</td> <!-- 当前是第几个对象，从0开始-->
            <td>varStatus.count</td> <!-- 已经遍历了多少对象，从1开始-->
            <td>varStatus.first</td> <!-- 是否是第1个对象-->
            <td>varStatus.last</td> <!-- 是否是最后一个对象 -->
            <td>varStatus.current</td> <!-- 当前的被遍历的对象-->
            <td>varStatus.begin</td> <!-- foreach begin的值-->
            <td>varStatus.end</td> <!-- foreach end-->
            <td>varStatus.step</td> <!-- foreach step-->
        </tr>
        </thead>

        <c:forEach var="num" begin="0" end="3" step="1" varStatus="varStatus">
            <tr>
                <td>${num}</td>
                <td>${varStatus.index}</td>
                <td>${varStatus.count}</td>
                <td>${varStatus.first}</td>
                <td>${varStatus.last}</td>
                <td>${varStatus.current}</td>
                <td>${varStatus.begin}</td>
                <td>${varStatus.end}</td>
                <td>${varStatus.step}</td>
            </tr>
        </c:forEach>
    </table>
</div>

<div class="foreach-map">
    <c:forEach var="item" items="${map}">
        <strong>${item.key} </strong> = ${item.value} <br/>
    </c:forEach>
</div>

<div class="fortoken">
    <c:forTokens items="abc,def,ghi" delims="," var="item">
        <strong>${item}</strong>
    </c:forTokens>
</div>

<!-- var只能设置integer double float string等-->
<div class="cset">
    <c:set var="totalCount" value="${totalCount +1}" scope="application"></c:set>
    <span>总访问次数: ${totalCount}</span><br/>

    <!-- 将参数action 放到map中-->
    <c:set target="${map}" property="name" value="${param.name}"></c:set>
    ${map.name}
</div>

<div class="remove">
    <c:remove var="somethingremove"></c:remove>
    ${somethingremove == null? "somethingremove is removed" : "somethingremove not remove"}
</div>

<div class="catch">
    <c:catch var="e">
        <c:set target="somebean" property="someproperty">some value</c:set>
    </c:catch>
    <c:if test="${e != null}">
        catch some exception ${e.cause},message : ${e.message}
    </c:if>
</div>
</body>
</html>
