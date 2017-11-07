<%--
  Created by IntelliJ IDEA.
  User: and
  Date: 2017/11/7
  Time: 13:44
  To change this template use File | Settings | File Templates.
--%>
<!-- jsp指令-->
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!-- jsp脚本-->

<%-- jsp特有注释--%>
<%
    /**
     * 多行
     */
    //单行注释
    String greeting = "hello jsp !";
%>

<%!
    //jsp声明方法块
%>
<html>
<head>
    <title>Title</title>
</head>
<body>
<div>
    <%= greeting %>
</div>
<div>
    <%
        out.println("out.println().....");
    %>
</div>
</body>
</html>
