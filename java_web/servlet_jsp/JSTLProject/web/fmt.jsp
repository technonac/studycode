<%--
  Created by IntelliJ IDEA.
  User: and
  Date: 2017/11/8
  Time: 15:23
  To change this template use File | Settings | File Templates.
  fmt= format
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<fmt:requestEncoding value="UTF-8"/>
<html>
<head>
    <title>fmt</title>
</head>
<body>
<%--<fmt:setLocale value="en"/>--%>
<fmt:bundle basename="messages">
    <fmt:message key="prompt.hello">
        <fmt:param value=" jstl fmt"></fmt:param>
    </fmt:message>
</fmt:bundle>

</body>
</html>
