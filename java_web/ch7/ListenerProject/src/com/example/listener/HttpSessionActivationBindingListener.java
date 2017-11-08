package com.example.listener;

import javax.servlet.http.*;
import java.io.Serializable;

public class HttpSessionActivationBindingListener implements HttpSessionActivationListener,
        HttpSessionBindingListener, Serializable {

    /**
     * 当对象被放到session里回调
     *
     * @param event
     */
    @Override
    public void valueBound(HttpSessionBindingEvent event) {
        HttpSession session = event.getSession();
        String name = event.getName();
        System.out.println(this + "被绑定到session " + session.getId() + "的 " + name + "属性上");
    }

    /**
     * 当对象被从session里移除时执行该方法
     *
     * @param event
     */
    @Override
    public void valueUnbound(HttpSessionBindingEvent event) {
        HttpSession session = event.getSession();
        String name = event.getName();
        System.out.println(this + "被从session " + session.getId() + "的 " + name + "属性上移除");
    }

    /**
     * 服务器关闭时，会将session里的内容保存到硬盘上
     *
     * @param se
     */
    @Override
    public void sessionWillPassivate(HttpSessionEvent se) {
        HttpSession session = se.getSession();
        System.out.println("sessionWillPassivate ,session id =" + session.getId());
    }

    /**
     * 服务器重新启动时，会将session内容从硬盘上重新加载
     *
     * @param se
     */
    @Override
    public void sessionDidActivate(HttpSessionEvent se) {
        HttpSession session = se.getSession();
        System.out.println("sessionDidActivate ,session id =" + session.getId());
    }
}
