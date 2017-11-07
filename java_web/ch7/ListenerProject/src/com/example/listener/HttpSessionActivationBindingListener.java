package com.example.listener;

import javax.servlet.http.HttpSessionActivationListener;
import javax.servlet.http.HttpSessionBindingEvent;
import javax.servlet.http.HttpSessionBindingListener;
import javax.servlet.http.HttpSessionEvent;
import java.io.Serializable;

public class HttpSessionActivationBindingListener implements HttpSessionActivationListener,
        HttpSessionBindingListener, Serializable {

    @Override
    public void valueBound(HttpSessionBindingEvent event) {

    }

    @Override
    public void valueUnbound(HttpSessionBindingEvent event) {

    }

    @Override
    public void sessionWillPassivate(HttpSessionEvent se) {

    }

    @Override
    public void sessionDidActivate(HttpSessionEvent se) {

    }
}
