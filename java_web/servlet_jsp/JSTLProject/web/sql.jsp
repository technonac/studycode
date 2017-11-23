<%--
  基础jstl sql的操作
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<%@ taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql" %>
<sql:setDataSource
        driver="com.mysql.jdbc.Driver"
        user="root"
        password="root"
        url="jdbc:mysql://localhost:3306/jstl?characterEncoding=UTF-8"
        var="dataSource"
        scope="page"
/>

<!-- 查询语句-->
<sql:query var="result" dataSource="${dataSource}" scope="page">
    select * from table_name
</sql:query>
<sql:query var="result" dataSource="${dataSource}" scope="page" sql="select * from table_name">
</sql:query>
<c:forEach var="row" items="${result.rows}">

</c:forEach>

<!-- 更新语句-->
<sql:update var="result" dataSource="${dataSource}">
    insert into table_name (name,brithday) values(?,?)
    <sql:param value="hello"></sql:param>
    <sql:dateParam value="" type="timestamp"></sql:dateParam>

</sql:update>

<!-- 事物语句 -->
<sql:transaction dataSource="${dataSource}">

</sql:transaction>
<html>
<html>
<head>
    <title>sql</title>
</head>
<body>

</body>
</html>
