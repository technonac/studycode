package com.example.util;

import java.sql.*;
import java.util.Objects;

public class DBManager {

    public static Connection getConnection() throws SQLException {
        return getConnection("databaseweb", "root", "root");
    }

    public static Connection getConnection(String dbName, String user, String pwd) throws SQLException {
        String uri = "jdbc:mysql://localhost:3306/" + dbName + "?useUnicode=true&useJDBCCompliantTimezoneShift=true" +
                "&useLegacyDatetimeCode=false&serverTimezone=UTC&characterEncoding=UTF-8";
        //注册驱动
        DriverManager.registerDriver(new com.mysql.jdbc.Driver());
        //获取连接
        return DriverManager.getConnection(uri, user, pwd);
    }

    public static void setParams(PreparedStatement preStmt, Object... params) throws SQLException {
        if (params == null || params.length == 0) {
            return;
        }
        int length = params.length;
        for (int i = 0; i < length; i++) {
            Object param = params[i];
            if (param == null) {
                preStmt.setNull(i, Types.NULL);
            } else if (param instanceof Integer) {
                preStmt.setInt(i, (Integer) param);
            } else if (param instanceof String) {
                preStmt.setString(i, (String) param);
            } else if (param instanceof Double) {
                preStmt.setDouble(i, (Double) param);
            } else if (param instanceof Long) {
                preStmt.setLong(i, (Long) param);
            } else if (param instanceof Timestamp) {
                preStmt.setTimestamp(i, (Timestamp) param);
            } else if (param instanceof Boolean) {
                preStmt.setBoolean(i, (Boolean) param);
            } else if (param instanceof Date) {
                preStmt.setDate(i, (Date) param);
            }
        }
    }

    public static int executeUpdate(String sql) {
        return executeUpdate(sql, new Object[]{});
    }

    public static int executeUpdate(String sql, Object... params) {
        Connection conn = null;
        PreparedStatement preparedStatement = null;
        try {
            conn = getConnection();
            preparedStatement = conn.prepareStatement(sql);
            return preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return 0;
    }
}
