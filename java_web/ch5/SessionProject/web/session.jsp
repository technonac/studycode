<%@ page import="java.text.DateFormat" %>
<%@ page import="java.text.SimpleDateFormat" %>
<%@ page import="com.example.session.bean.Person" %>
<%@ page import="java.util.Date" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%!
    DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
%>
<%
    String message = "";
    response.setCharacterEncoding("UTF-8");
    Person[] persons = {
            new Person("test1", "test1", 17, dateFormat.parse("1999-9-9")),
            new Person("test2", "test2", 18, dateFormat.parse("1999-9-9")),
            new Person("test3", "test3", 19, dateFormat.parse("1999-9-9")),
    };
    if ("POST".equals(request.getMethod())) {
        for (Person person : persons) {
            if (person.getUsername().equalsIgnoreCase(request.getParameter("username")) &&
                    person.getUsername().equalsIgnoreCase(request.getParameter("password"))) {

                //登录成功
                session.setAttribute("person", person);
                session.setAttribute("loginTime", new Date());

                response.sendRedirect(request.getContextPath() + "/welcome.jsp");
                return;
            }
        }
        message = "用户名密码不匹配,登录失败.";
    }
%>
<html>
<head>
    <title>session</title>
</head>
<body>
<div>
    <%= message %>
</div>
<div>
    <form action="session.jsp" method="post">
        <div>
            <span>account: </span><input type="text" name="username">
        </div>
        <div>
            <span>password: </span><input type="text" name="password">
        </div>
        <input type="submit" value="submit">
    </form>
</div>
</body>
</html>
