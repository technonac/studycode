<%@ page import="java.text.DateFormat" %>
<%@ page import="java.text.SimpleDateFormat" %>
<%@ page import="com.example.session.bean.Person" %>
<%@ page import="java.util.Date" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%!
    DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
%>
<%
    Person person = (Person) session.getAttribute("person");
    Date loginTime = (Date) session.getAttribute("loginTime");
%>
<html>
<head>
    <title>welcome</title>
</head>
<body>
<div>
    <span>session id : </span> <span> <%= session.getId() %></span>
</div>
<div>
    <span>getLastAccessedTime: </span> <span> <%= session.getLastAccessedTime() %></span>
</div>
<div>
    <span>getMaxInactiveInterval: </span> <span> <%= session.getMaxInactiveInterval() %></span>
</div>
<div>
    <span>username : </span> <span> <%= person.getUsername() %></span>
</div>
<div>
    <span>login time : </span> <span> <%= loginTime %></span>
</div>
<div>
    <span>age : </span> <span> <%= person.getAge() %></span>
</div>
<div>
    <span>brithday : </span> <span> <%= dateFormat.format(person.getBirthday()) %></span>
</div>
</body>
</html>
