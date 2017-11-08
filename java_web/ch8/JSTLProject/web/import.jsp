<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!-- 直接将整个网页import进来 -->
<%--<c:import url="http://www.baidu.com" charEncoding="UTF-8"></c:import>--%>

<%--<c:import var="baidu" url="http://www.baidu.com" charEncoding="UTF-8" scope="request"></c:import>--%>
<%--<c:out value="${baidu}" escapeXml="true"></c:out>--%>

<%--<c:url value="/core.jsp"/>--%>

<c:redirect url="core.jsp">
    <c:param name="action" value="hello"></c:param>
    <c:param name="name" value="tome"></c:param>
</c:redirect>