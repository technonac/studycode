package com.example;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;


public class ReadParamServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException,
            IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException,
            IOException {

        request.setCharacterEncoding("UTF-8");
        response.setCharacterEncoding("UTF-8");
        response.setContentType("text/html");

        //获取web.xml中配置的init-param
        //方法1
        String initParameter = getInitParameter("hello");
        Enumeration<String> initParameterNames = getInitParameterNames();

        //方法2
        ServletConfig servletConfig = getServletConfig();
        String initParameter1 = servletConfig.getInitParameter("hello");


        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<head><title>First ReqServlet</title></head>");
        out.println("<body>");
        out.println("init-param  hello = " + initParameter + "<br/>");
        out.println("</body>");
        out.println("</html>");
    }
}
