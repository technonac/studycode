<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<%@ taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<sql:setDataSource
        driver="com.mysql.jdbc.Driver"
        user="root"
        password="root"
        url="jdbc:mysql://localhost:3306/databaseweb?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC&characterEncoding=UTF-8"
        var="dataSource"
        scope="page"
/>
<html>
<head>
    <title>operate</title>
</head>
<body>


<c:if test="${param.action == 'add'}">
    <sql:update dataSource="${dataSource}" var="result" scope="request">
        INSERT INTO tb_person (name,english_name,age,sex,birthday,description) values(?,?,?,?,?,?)
        <sql:param>${param.name}</sql:param>
        <sql:param>${param.englishName}</sql:param>
        <sql:param>${param.age}</sql:param>
        <sql:dateParam value="${param.birthday}"></sql:dateParam>
        <sql:param>${param.description}</sql:param>
    </sql:update>
    <div>
        insert affect rows ${result}....
    </div>
</c:if>
<c:if test="${param.action == 'del'}">
    <sql:update dataSource="${dataSource}" var="result" scope="request">
        DELETE FROM tb_person WHERE ID IN(?)
        <sql:param>${param.id}</sql:param>
    </sql:update>
    <div>
        delte affect rows ${result}....
        <c:redirect url="listperson.jsp"/>
    </div>
</c:if>

</body>
</html>
