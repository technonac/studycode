<%--
  Created by IntelliJ IDEA.
  User: and
  Date: 2017/11/7
  Time: 15:46
  To change this template use File | Settings | File Templates.
  jsp行为 jsp actions
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java"
%>
<html>
<head>
    <title>JSP Actions</title>
</head>
<body>
<jsp:include page="somthing_include.jsp" flush="false"/>


<jsp:forward page="index.jsp">
    <jsp:param name="user" value="abc"/>
    <jsp:param name="param1" value="value1"/>
</jsp:forward>

</body>
</html>
