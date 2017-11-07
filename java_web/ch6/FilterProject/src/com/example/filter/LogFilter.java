package com.example.filter;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class LogFilter implements Filter {

    private String filterName = "";

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        filterName = filterConfig.getFilterName();
        System.out.println("start filter: " + filterName);
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException,
            ServletException {

        HttpServletRequest req = (HttpServletRequest) request;
        HttpServletResponse res = (HttpServletResponse) response;

        long startTime = System.currentTimeMillis();
        String requestURI = req.getRequestURI();

        //执行下一个filter或者servlet
        chain.doFilter(request, response);

        long endTime = System.currentTimeMillis();
        System.out.println(req.getRemoteAddr() + ", url = " + requestURI + ", cost = " + (endTime - startTime) + "ms");

    }

    @Override
    public void destroy() {
        System.out.println("destroy filter: " + filterName);

    }
}
