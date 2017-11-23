<%--
  Created by IntelliJ IDEA.
  User: and
  Date: 2017/11/7
  Time: 14:23
  To change this template use File | Settings | File Templates.
  jsp 基本流程控制
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<div class="if-statement">
    <%
        String param = request.getParameter("param");
        if ("1".equals(param)) {
    %>
    <p>this is if param = 1 print....</p>
    <%
    } else if ("2".equals(param)) {
    %>
    <p>this is if param = 2 print....</p>
    <%
    } else if ("return".equals(param)) {
        return; //会导致后面html代码都不会输出
    } else {
    %>
    <p>no param</p>
    <%
        }
    %>
</div>
<div class="for-statement">
    <table border="1px">
        <tr>
            <%
                for (int i = 0; i < 10; i++) {
            %>
            <td>
                <%= i %>
            </td>
            <%
                }
            %>
        </tr>
    </table>
</div>
</body>
</html>
