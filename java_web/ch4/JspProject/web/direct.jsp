<%--
  Created by IntelliJ IDEA.
  User: and
  Date: 2017/11/7
  Time: 14:37
  To change this template use File | Settings | File Templates.

  Server Version: Apache Tomcat/8.5.11
  Servlet Version: 3.1
  JSP Version: 2.3

  jsp 指令
  格式
  <%@ directive {attr = value} %>

--%>
<%--page指令--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page pageEncoding="UTF-8" %>
<%@ page import="java.util.ArrayList" %>
<%--是否内置session对象，默认为true--%>
<%--<%@ page session="true" %>--%>
<%--<%@ page extends="java" %>--%>
<%--<%@ page autoFlush="true" %>--%>
<%--<%@ page buffer="8kb" %>--%>
<%--是否线程安全，true则多个线程同时运行该jsp程序，false则只运行一个线程，其他线程等待--%>
<%--<%@ page isThreadSafe="false" %>--%>

<%--<%@ page isErrorPage="false" %>--%>
<%--<%@ page errorPage="index.jsp" %>--%>
<%@ page info="something here that can approach from Servlet.getServletInfo()" %>
<%--去掉指令前后的空白字符--%>
<%@page trimDirectiveWhitespaces="true" %>

<%--<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>--%>
<%
    ArrayList<String> list = new ArrayList<>();
    list.add("aa");
    list.add("bb");
    list.add("cc");
    list.add("dd");
%>
<html>
<head>
    <title>direct</title>
</head>
<body>
Server Version: <%= application.getServerInfo() %><br>
Servlet Version: <%= application.getMajorVersion() %>.<%= application.getMinorVersion() %><br/>
JSP Version: <%= JspFactory.getDefaultFactory().getEngineInfo().getSpecificationVersion() %> <br/>

<%--include指令，先包含，后编译--%>
<%@ include file="somthing_include.jsp" %>

<%--include行为，先运行，后包含--%>
<jsp:include page="somthing_include.jsp"/>

<div>
    <%--<c:forEach var="item" items="${list}">--%>
        <%--<c:out value="item"></c:out>--%>
    <%--</c:forEach>--%>
</div>
</body>
</html>
