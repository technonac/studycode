<%@ page contentType="text/html;charset=UTF-8" language="java" isErrorPage="true" %>
<%
    request.setCharacterEncoding("UTF-8");
    response.setCharacterEncoding("UTF-8");
    if ("POST".equals(request.getMethod())) {
        Cookie usernameCookie = new Cookie("username", request.getParameter("username"));
        Cookie visittimesCookie = new Cookie("visitTimes", "0");
        response.addCookie(usernameCookie);
        response.addCookie(visittimesCookie);

        response.sendRedirect(request.getContextPath() + "/cookie.jsp");
        return;
    }
%>
<html>
<head>
    <title>login</title>
</head>
<body>
<div class="exception-info">
    <%= exception.getMessage() %>
</div>
<form action="login.jsp" method="post">
    <div>
        <input type="text" name="username">
    </div>
    <div>
        <input type="text" name="password">
    </div>
    <div>
        <input type="submit" value="OK">
    </div>
</form>
</body>
</html>
