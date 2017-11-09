package com.example.struts2.action;

import com.opensymphony.xwork2.ActionSupport;

public class LoginAction extends ActionSupport {
    private String account;
    private String password;

    /**
     * struts2 action的主方法，提交数据后会调用该方法
     *
     * @return
     */
    public String execute() {
        if ("admin".equalsIgnoreCase(account) && "123456".equalsIgnoreCase(password)) {
            return SUCCESS;
        }
        return LOGIN;

    }

    public String getAccount() {
        return account;
    }

    public void setAccount(String account) {
        this.account = account;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String login(){
    	return execute();
    }
}
