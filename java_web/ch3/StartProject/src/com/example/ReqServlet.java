package com.example;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.security.Principal;
import java.util.Locale;


public class ReqServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        response.setCharacterEncoding("UTF-8");

        response.setContentType("text/html");

        String authType = request.getAuthType();
        String localAddr = request.getLocalAddr(); //服务器ip
        String localName = request.getLocalName(); //服务器名称
        int localPort = request.getLocalPort(); //tomcat端口号

        Locale locale = request.getLocale(); //用户的语言环境
        String contextPath = request.getContextPath();
        String method = request.getMethod();
        String pathInfo = request.getPathInfo();
        String pathTranslated = request.getPathTranslated();
        String protocol = request.getProtocol();
        String queryString = request.getQueryString(); //？后面的字符串

        String remoteAddr = request.getRemoteAddr(); //客户端ip
        int remotePort = request.getRemotePort(); //客户端端口
        String remoteUser = request.getRemoteUser();

        String requestURI = request.getRequestURI();
        StringBuffer requestURL = request.getRequestURL();
        String scheme = request.getScheme();
        String serverName = request.getServerName();
        int serverPort = request.getServerPort();
        String servletPath = request.getServletPath(); //servlet的请求路径
        Principal userPrincipal = request.getUserPrincipal();

        String accept = request.getHeader("accept");
        String referer = request.getHeader("referer"); //从哪个页面点击链接到了本页
        String userAgent = request.getHeader("user-agent");

        String serverInfo = getServletContext().getServerInfo(); //服务器信息

        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<head><title>ReqServlet</title></head>");
        out.println("<body>");
        out.println("authType = " + authType + "<br/>");
        out.println("localAddr = " + localAddr + "<br/>");
        out.println("localName = " + localName + "<br/>");
        out.println("localPort = " + localPort + "<br/>");
        out.println("locale = " + locale + "<br/>");
        out.println("contextPath = " + contextPath + "<br/>");
        out.println("method = " + method + "<br/>");
        out.println("pathInfo = " + pathInfo + "<br/>");
        out.println("pathTranslated = " + pathTranslated + "<br/>");
        out.println("protocol = " + protocol + "<br/>");
        out.println("queryString = " + queryString + "<br/>");
        out.println("remoteAddr = " + remoteAddr + "<br/>");
        out.println("remotePort = " + remotePort + "<br/>");
        out.println("remoteUser = " + remoteUser + "<br/>");
        out.println("requestURI = " + requestURI + "<br/>");
        out.println("requestURL = " + requestURL + "<br/>");
        out.println("scheme = " + scheme + "<br/>");
        out.println("serverName = " + serverName + "<br/>");
        out.println("serverPort = " + serverPort + "<br/>");
        out.println("servletPath = " + servletPath + "<br/>");
        out.println("userPrincipal = " + userPrincipal + "<br/>");
        out.println("accept = " + accept + "<br/>");
        out.println("referer = " + referer + "<br/>");
        out.println("userAgent = " + userAgent + "<br/>");
        out.println("serverInfo = " + serverInfo + "<br/>");
        out.println("</body>");
        out.println("</html>");


    }
}
