package com.test.simple.mapper;

import com.test.simple.model.SysRole;
import com.test.simple.model.SysUser;

import java.util.List;
import java.util.Map;

public interface UserMapper {

    SysUser selectById(Long id);

    List<SysUser> selectAll();

    List<SysRole> selectRoleByUserId(Long userId);

    int insert(SysUser sysUser);

    /**
     * useGenerateKeys
     *
     * @param sysUser
     * @return
     */
    int insert2(SysUser sysUser);

    /**
     * selectKey方式
     *
     * @param sysUser
     * @return
     */
    int insert3(SysUser sysUser);

    int updateById(SysUser sysUser);

    int deleteById(Long id);

    List<SysUser> selectByUser(SysUser sysUser);

    SysUser selectByIdOrUserName(SysUser sysUser);

    List<SysUser> selectByIdList(List<Long> idList);

    int insertList(List<SysUser> userList);

    int updateByMap(Map<String, Object> map);


    SysUser selectUserAndRoleById(Long id);

    SysUser selectUserAndRoleById2(Long id);
}
