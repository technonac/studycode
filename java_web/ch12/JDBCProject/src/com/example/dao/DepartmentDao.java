package com.example.dao;

import com.example.bean.Department;
import com.example.util.DBManager;

/**
 * database access objects
 */
public class DepartmentDao {

    public static int insert(Department department) {
        String sql = "INSERT INTO tb_department (name) VALUES (?)";
        return DBManager.executeUpdate(sql, department.getName());

    }
}
