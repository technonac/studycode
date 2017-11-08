<%@ page import="com.example.bean.PersonalInfo" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Listener test</title>
</head>
<body>
<%
    PersonalInfo personalInfo = (PersonalInfo) session.getAttribute("personalInfo");
    if (personalInfo == null) {
        personalInfo = new PersonalInfo();
        personalInfo.setName("helloooo");
        session.setAttribute("personalInfo", personalInfo);
        out.println("成功创建对象,sessionId = " + session.getId());
    } else {
        out.println("对象已经存在,sessionId = " + session.getId());
    }
%>
</body>
</html>
