<%@ page import="java.sql.*" %>
<%--
基本jdbc的操作
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%
    Connection conn = null;
    Statement statement = null;
    ResultSet rs = null;

    try {
        //注册驱动
        DriverManager.registerDriver(new com.mysql.jdbc.Driver());

        //获取数据库连接
        conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/databaseweb?useUnicode=true&useJDBCCompliantTimezoneShift=true" +
                        "&useLegacyDatetimeCode=false&serverTimezone=UTC&characterEncoding=UTF-8",
                "root", "root");

        //获取statement, 该对象用于执行sql,相当于控制台
        statement = conn.createStatement();

        //使用statement对象执行select返回结果集
        rs = statement.executeQuery("SELECT * FROM tb_person ORDER BY id");
%>
<html>
<head>
    <title>list person</title>
</head>
<body>
<div>
    <a href="addperson.jsp">添加</a>
</div>
<div>
    <form action="operateperson.jsp">
        <table border="1px" cellpadding="0" cellspacing="0">
            <tr>
                <th>id</th>
                <th>name</th>
                <th>eng.name</th>
                <th>gender</th>
                <th>age</th>
                <th>brithday</th>
                <th>comment</th>
                <th>create_time</th>
                <th>operate</th>
            </tr>

            <%
                //遍历结果集
                while (rs.next()) {
                    int id = rs.getInt("id");
                    int age = rs.getInt("age");
                    String name = rs.getString("name");
                    String english_name = rs.getString("english_name");
                    String sex = rs.getString("sex");
                    String description = rs.getString("description");
                    Date birthday = rs.getDate("birthday");
                    Timestamp create_time = rs.getTimestamp("create_time");
            %>
            <tr>
                <td>
                    <%= id %>
                </td>
                <td>
                    <%= name %>
                </td>
                <td>
                    <%= english_name %>
                </td>
                <td>
                    <%= sex %>
                </td>
                <td>
                    <%= age %>
                </td>
                <td>
                    <%= description %>
                </td>
                <td>
                    <%= birthday %>
                </td>
                <td>
                    <%= create_time %>
                </td>
                <td>
                    <a href="operateperson.jsp?action=del&id=<%= id %>">删除</a>
                    <a href="operateperson.jsp?action=edit&id=<%= id %>">修改</a>
                </td>
            </tr>

            <%
                }
            %>
        </table>
    </form>
</div>
</body>
</html>

<%

    } catch (SQLException e) {
        e.printStackTrace();
    } finally {
        if (rs != null) {
            rs.close();
        }

        if (statement != null) {
            statement.close();
        }

        if (conn != null) {
            conn.close();
        }
    }

%>
