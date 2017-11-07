<%--
  Created by IntelliJ IDEA.
  User: and
  Date: 2017/11/7
  Time: 18:55
  To change this template use File | Settings | File Templates.
  el表达式 expression language
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>el</title>
</head>
<body>
<div>${param.foo}</div>
<div>${param["foo"]}</div>
<div>${header.host}</div>
<div>${1+2}</div>
<div>${1>2}</div>
<div>${empty ""}</div>
</body>
</html>
