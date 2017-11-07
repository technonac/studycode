package com.example;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

public class FirstServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        log("exec doPost()");
        execute(request, response);
    }

    /**
     * 执行doGet前会限制性getLastModified(),返回-1 表示需要时刻更新，总是执行该函数
     *
     * @param request
     * @param response
     * @throws ServletException
     * @throws IOException
     */
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        log("exec doGet()");
        execute(request, response);
    }

    /**
     * 返回该Servlet生成文档的更新时间时间戳，对GET方式访问邮箱
     * 实时更新 返回-1，默认为-1
     *
     * @param req
     * @return
     */
    @Override
    protected long getLastModified(HttpServletRequest req) {
        log("exec getLastModified()");
        return super.getLastModified(req);
    }

    private void execute(HttpServletRequest request, HttpServletResponse response) throws IOException {
        request.setCharacterEncoding("UTF-8");
        response.setCharacterEncoding("UTF-8");

        String requestURI = request.getRequestURI();
        String method = request.getMethod();
        String param = request.getParameter("param");

        response.setContentType("text/html");

        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<head><title>First ReqServlet</title></head>");
        out.println("<body>");
        out.println("request requestURI = " + requestURI + "<br/>");
        out.println("request method = " + method + "<br/>");
        out.println("request param = " + param + "<br/>");
        out.println("<script>document.write('本页面最后更新时间: ' + document.lastModified);</script");
        out.println("</body>");
        out.println("</html>");
    }
}
