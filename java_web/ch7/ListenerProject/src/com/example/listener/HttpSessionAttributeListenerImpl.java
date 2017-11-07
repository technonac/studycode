package com.example.listener;

import javax.servlet.http.HttpSession;
import javax.servlet.http.HttpSessionAttributeListener;
import javax.servlet.http.HttpSessionBindingEvent;

/**
 * 监听 对象属性的变化
 */
public class HttpSessionAttributeListenerImpl implements HttpSessionAttributeListener {

    @Override
    public void attributeAdded(HttpSessionBindingEvent se) {
        HttpSession session = se.getSession();
        String name = se.getName();
        Object value = se.getValue();
        System.out.println("attributeAdded - name = " + name + ",value = " + value);
    }

    @Override
    public void attributeRemoved(HttpSessionBindingEvent se) {
        HttpSession session = se.getSession();
        String name = se.getName();
        Object value = se.getValue();
        System.out.println("attributeRemoved - name = " + name + ",value = " + value);
    }

    @Override
    public void attributeReplaced(HttpSessionBindingEvent se) {
        HttpSession session = se.getSession();
        String name = se.getName();
        Object oldValue = se.getValue();
        Object value = session.getAttribute(name);
        System.out.println("attributeReplaced - name = " + name + ",oldValue = " + oldValue + ",value = " + value);
    }
}
