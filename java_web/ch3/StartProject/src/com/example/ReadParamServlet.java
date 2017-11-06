package com.example;

import javax.annotation.Resource;
import javax.servlet.ServletConfig;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;


public class ReadParamServlet extends HttpServlet {

    //resource inject 资源注入
    @Resource(name = "hello")
    private String hello; //注入的字符串

    @Resource(name = "i")
    private int i;

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
        String initParameter = getInitParameter("initParamName");
        Enumeration<String> initParameterNames = getInitParameterNames();

        //方法2
        ServletConfig servletConfig = getServletConfig();
        String initParameter1 = servletConfig.getInitParameter("hello");


        //获取context param
        ServletContext servletContext = getServletConfig().getServletContext();
        String uploadFolder = servletContext.getInitParameter("upload folder");
        String realPath = servletContext.getRealPath(uploadFolder);

        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<head><title>First ReqServlet</title></head>");
        out.println("<body>");
        out.println("init-param  initParamName = " + initParameter + "<br/>");
        out.println("context param  uploadFolder = " + uploadFolder + "<br/>");
        out.println("realPath = " + realPath + "<br/>");
        out.println("Resource Inject hello = " + hello + "<br/>");
        out.println("Resource Inject  i = " + i + "<br/>");

        out.println("</body>");
        out.println("</html>");
    }
}
