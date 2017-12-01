package com.test.simple.mapper;

import com.test.simple.model.SysRole;
import com.test.simple.model.SysUser;
import org.apache.ibatis.session.SqlSession;
import org.junit.Assert;
import org.junit.Test;

import java.util.*;

public class UserMapperTest extends BaseMapperTest {

    @Test
    public void testSelectById() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            SysUser user = userMapper.selectById(1L);

            Assert.assertNotNull(user);
            Assert.assertEquals("admin", user.getUserName());

        } finally {
            sqlSession.close();
        }
    }

    @Test
    public void testSelectAll() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            List<SysUser> userList = userMapper.selectAll();

            Assert.assertNotNull(userList);

            Assert.assertTrue(userList.size() > 0);
        } finally {
            sqlSession.close();
        }
    }

    @Test
    public void testSelectRoleByUserId() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            List<SysRole> userRoleList = userMapper.selectRoleByUserId(1L);
            Assert.assertNotNull(userRoleList);
        } finally {
            sqlSession.close();
        }
    }

    @Test
    public void testInsert() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);

            //创建user对象
            SysUser user = new SysUser();
            user.setUserName("test1");
            user.setUserPassword("123456");
            user.setUserEmail("test1@test1.com");
            user.setUserInfo("test info");
            user.setHeadImg(new byte[]{1, 2, 3});
            user.setCreateTime(new Date());

            //result是执行sql影响的行数
            int result = userMapper.insert(user);

            Assert.assertEquals(1, result);

            //id为null，没有给id赋值，并且没有配置回写id的值
            Assert.assertNull(user.getId());
            sqlSession.commit(); //提交到数据库
        } finally {
            //回滚测试
//            sqlSession.rollback();
            sqlSession.close();
        }
    }

    @Test
    public void testInsert2() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            //创建user对象
            SysUser user = new SysUser();
            user.setUserName("test1");
            user.setUserPassword("123456");
            user.setUserEmail("test1@test1.com");
            user.setUserInfo("test info");
            user.setHeadImg(new byte[]{1, 2, 3});
            user.setCreateTime(new Date());

            //result是执行sql影响的行数
            int result = userMapper.insert2(user);

            Assert.assertEquals(1, result);

            //因为id回写，所以id不为null
            Assert.assertNotNull(user.getId());
            sqlSession.commit();
        } finally {
            sqlSession.close();
        }
    }

    @Test
    public void testUpdateById() {
        SqlSession sqlSession = getSqlSession();

        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);

            SysUser user = userMapper.selectById(1L);

            Assert.assertEquals("admin", user.getUserName());

            //更新数据
            user.setUserInfo("admin test");

            userMapper.updateById(user);

            sqlSession.commit();
        } finally {
            sqlSession.close();
        }
    }

    @Test
    public void testDeleteById() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);

            int result = userMapper.deleteById(1006L);

            sqlSession.commit();
        } finally {
            sqlSession.close();
        }
    }

    @Test
    public void testSelectByUser() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);

            //只查询用户名
            SysUser query = new SysUser();
            query.setUserName("ad");
            List<SysUser> userList = userMapper.selectByUser(query);
            Assert.assertTrue(userList.size() > 0);

            //只查询用户邮箱
            query = new SysUser();
            query.setUserEmail("test@mybatis.tk");
            userList = userMapper.selectByUser(query);
            Assert.assertTrue(userList.size() > 0);

            //当同时查询用户名和邮箱
            query = new SysUser();
            query.setUserEmail("test@mybatis.tk");
            query.setUserName("ad");
            userList = userMapper.selectByUser(query);
            Assert.assertTrue(userList.size() == 0);


        } finally {
            sqlSession.close();
        }
    }

    @Test
    public void testSelectByIdOrUserName() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);


            //只查询用户名
            SysUser query = new SysUser();
            query.setId(1L);
            query.setUserName("admin");
            SysUser user = userMapper.selectByIdOrUserName(query);
            Assert.assertNotNull(user);

            //没有id
            query.setId(null);
            user = userMapper.selectByIdOrUserName(query);
            Assert.assertNotNull(user);

            //id和name都为空时
            query.setUserName(null);
            user = userMapper.selectByIdOrUserName(query);
            Assert.assertNull(user);

        } finally {
            sqlSession.close();
        }
    }

    @Test
    public void testSelectByIdList() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            List<Long> idList = new ArrayList<Long>();
            idList.add(1L);
            idList.add(1001L);

            List<SysUser> userList = userMapper.selectByIdList(idList);
            Assert.assertEquals(2, userList.size());
        } finally {
            sqlSession.close();
        }
    }

    @Test
    public void testInsertList() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);

            List<SysUser> userList = new ArrayList<SysUser>();
            for (int i = 0; i < 2; i++) {
                SysUser user = new SysUser();
                user.setUserName("test" + i);
                user.setUserPassword("123456");
                user.setUserEmail("test@test.com");
                userList.add(user);
            }

            int result = userMapper.insertList(userList);
            sqlSession.commit();

            Assert.assertEquals(2, result);
        } finally {
            sqlSession.close();
        }
    }

    @Test
    public void testUpdateByMap() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            Map<String, Object> map = new HashMap<String, Object>();
            //查询条件，同样也是更新字段
            map.put("id", 1L);

            map.put("user_email", "admin@admin.com");
            map.put("user_password", "123456");

            int result = userMapper.updateByMap(map);
            sqlSession.commit();
        } finally {
            sqlSession.close();
        }
    }

    /**
     * 一对一映射
     */
    @Test
    public void testSelectUserAndRoleById() {
        SqlSession sqlSession = getSqlSession();
        try {
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
            SysUser user = userMapper.selectUserAndRoleById2(1001L);

            Assert.assertNotNull(user);
            Assert.assertNotNull(user.getRole());
        } finally {
            sqlSession.close();
        }
    }
}
