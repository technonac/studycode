<%@ page import="java.util.TimeZone" %>
<%@ page import="java.util.Map" %>
<%@ page import="java.util.HashMap" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%
    Map<String, TimeZone> hashMap = new HashMap<>();
    String[] availableIDs = TimeZone.getAvailableIDs();
    for (String id : availableIDs) {
        hashMap.put(id, TimeZone.getTimeZone(id));
    }
    request.setAttribute("timezoneIds", TimeZone.getAvailableIDs());
    request.setAttribute("timezone", hashMap);

%>
<html>
<head>
    <title>timezone</title>
</head>
<body>
<jsp:useBean id="date" class="java.util.Date"/>
<fmt:setLocale value="zh_CN"/>
<div>
    <%= TimeZone.getDefault().getDisplayName() %>
    <fmt:formatDate value="${date}" type="both"/>
</div>
<div>
    <table border="1px" cellpadding="0" cellspacing="0">
        <tr>
            <th>时区id</th>
            <th>时区</th>
            <th>现在时间</th>
            <th>时差</th>
        </tr>
        <c:forEach var="id" items="${timezoneIds}" varStatus="status">
            <tr>
                <td>${id}</td>
                <td>${timezone[id].displayName}</td>
                <td>
                    <fmt:timeZone value="${id}">
                        <fmt:formatDate value="${date}" type="both" timeZone="${id}"/>
                    </fmt:timeZone>
                </td>
                <td>${ timezone[id].rawOffset / 60 / 60 /1000 }</td>
            </tr>
        </c:forEach>
    </table>
</div>
</body>
</html>
