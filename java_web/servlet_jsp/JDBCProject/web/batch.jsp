<%@ page import="java.sql.*" %><%--
批量操作
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<html>
<head>
    <title>Title</title>
</head>
<body>
<%
    Connection conn = null;
    PreparedStatement preparedStatement = null; //可以使用不完整sql语句

    try {
        DriverManager.registerDriver(new com.mysql.jdbc.Driver());
        conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/databaseweb?useUnicode=true&useJDBCCompliantTimezoneShift=true" +
                        "&useLegacyDatetimeCode=false&serverTimezone=UTC&characterEncoding=UTF-8",
                "root", "root");

        preparedStatement = conn.prepareStatement("INSERT INTO tb_person (name,english_name,age,sex,birthday,description) VALUES(?,?,?,?,?,?)");

        for (int i = 0; i < 5; i++) {
            int index = 1;
            preparedStatement.setString(index++, "name" + i);
            preparedStatement.setString(index++, "english" + i);
            preparedStatement.setInt(index++, 20);
            preparedStatement.setString(index++, "male");
            preparedStatement.setDate(index++, new Date(System.currentTimeMillis()));
            preparedStatement.setString(index++, "description" + i);
            preparedStatement.addBatch();
        }
        int[] result = preparedStatement.executeBatch();
    } catch (SQLException e) {
        e.printStackTrace();
    } finally {
        if (preparedStatement != null) {
            preparedStatement.close();
        }
        if (conn != null) {
            conn.close();
        }
    }


%>
</body>
</html>
