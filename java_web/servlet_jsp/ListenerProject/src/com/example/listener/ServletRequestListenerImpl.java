package com.example.listener;

import javax.servlet.ServletRequestEvent;
import javax.servlet.ServletRequestListener;
import javax.servlet.http.HttpServletRequest;

/**
 * 监听request的创建和销毁 用户每次请求都会回调
 */
public class ServletRequestListenerImpl implements ServletRequestListener {
    @Override
    public void requestDestroyed(ServletRequestEvent sre) {
        HttpServletRequest request = (HttpServletRequest) sre.getServletRequest();
        Long start = (Long) request.getAttribute("dateCreated");
        long end = System.currentTimeMillis();
        System.out.println("requestDestroyed,ip = " + request.getRemoteAddr() + ", cost = " + (end - start) + "ms");
    }

    @Override
    public void requestInitialized(ServletRequestEvent sre) {
        HttpServletRequest request = (HttpServletRequest) sre.getServletRequest();
        String uri = request.getRequestURI();
        request.setAttribute("dateCreated", System.currentTimeMillis());
        System.out.println("requestInitialized, ip = " + request.getRemoteAddr() + ", url = " + uri);
    }
}
