<%@ page import="java.util.Locale" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%
    request.setAttribute("localeList", Locale.getAvailableLocales());
%>
<html>
<head>
    <title>setLocale</title>
</head>
<body>
<table border="1px" cellspacing="0" cellpadding="0">
    <tr>
        <th>Locale</th>
        <th>Language</th>
        <th>Date and Time</th>
        <th>Number</th>
        <th>currency</th>
    </tr>
    <jsp:useBean id="date" class="java.util.Date"></jsp:useBean>
    <c:forEach var="locale" items="${localeList}">
        <fmt:setLocale value="${locale}"/>
        <tr>
            <td>${locale.displayName}</td>
            <td>${locale.displayLanguage}</td>
            <td><fmt:formatDate value="${date}"/></td>
            <td><fmt:formatNumber value="10000.5"/></td>
            <td><fmt:formatNumber value="10000.5" type="currency"/></td>
            <td></td>
        </tr>
    </c:forEach>
</table>
</body>
</html>
