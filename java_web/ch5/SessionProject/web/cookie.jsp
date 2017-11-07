<%@ page contentType="text/html;charset=UTF-8" language="java" errorPage="login.jsp" %>
<%
    request.setCharacterEncoding("UTF-8");
    String username = "";
    int visitTimes = 0;
    Cookie[] cookies = request.getCookies();
    if (cookies != null) {
        for (int i = 0; i < cookies.length; i++) {
            Cookie cookie = cookies[i];
            if ("username".equals(cookie.getName())) {
                username = cookie.getValue();
            } else if ("visitTimes".equals(cookie.getName())) {
                visitTimes = Integer.parseInt(cookie.getValue());
            }
        }
    }
    if (username == null || username.trim().equals("")) {
        throw new Exception("您还没有登录，请先登录.");
    }

    Cookie visitTimesCookie = new Cookie("visitTimes", Integer.toString(++visitTimes));
    response.addCookie(visitTimesCookie); //覆盖cookie

%>
<html>
<head>
    <title>cookie</title>
</head>
<body>
<form action="login.jsp" method="post">
    <div>
        <span>您的账号 = </span><span><%= username %></span>
    </div>
    <div>
        <span>登录次数 = </span><span><%= visitTimes %></span>
    </div>
    <input type="button" value="refresh" onclick="location = '<%= request.getRequestURI()%>?ts='+ new Date().getTime();">
</form>
</body>
</html>
