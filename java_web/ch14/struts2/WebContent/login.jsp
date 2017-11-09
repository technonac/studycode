<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="struts" uri="/struts-tags" %>
<html>
<head>
    <title>Login</title>
</head>
<body>
<struts:form action="login">
    <struts:label value="Login"></struts:label>
    <struts:textfield name="account" label="username"></struts:textfield>
    <struts:password name="password" label="password"></struts:password>
    <struts:submit value="login"></struts:submit>
</struts:form>
</body>
</html>
