<%@ page import="java.util.Enumeration" %><%--
  Created by IntelliJ IDEA.
  User: and
  Date: 2017/11/7
  Time: 13:44
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>index</title>
</head>
<body>
<%
    Enumeration<String> parameterNames = request.getParameterNames();
    while (parameterNames.hasMoreElements()) {
        String name = parameterNames.nextElement();
        String value = request.getParameter(name);
%>
<div><%=name %> = <%= value%>
</div>
<%
    }
%>
</body>
</html>
