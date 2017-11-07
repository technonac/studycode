<%--
  Created by IntelliJ IDEA.
  User: and
  Date: 2017/11/7
  Time: 16:34
  To change this template use File | Settings | File Templates.
  java bean的使用
  scope介绍
  page:只在在jsp有效 默认
  request:当前请求有效
  session:当前用户有效
  application:当前web应用程序内有效

--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>usebean.jsp</title>
</head>
<body>
<%--创建Person类的对象 person--%>
<jsp:useBean id="person" class="com.example.jsp.bean.Person" scope="page"/>
<%--设置person的所有属性，属性值从request中自动取得,*表示所有的属性--%>
<jsp:setProperty name="person" property="*"/>

<div>
    <span>name = </span>
    <jsp:getProperty name="person" property="name"/>
</div>

<div>
    <span>age = </span>
    <jsp:getProperty name="person" property="age"/>
</div>
<div>
    <span>sex = </span>
    <jsp:getProperty name="person" property="sex"/>
</div>

</body>
</html>
