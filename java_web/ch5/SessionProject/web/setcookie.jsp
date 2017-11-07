<%@ page import="java.net.URLEncoder" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<%!
    public boolean isNull(String str) {
        return str == null || str.trim().length() == 0;
    }
%>
<%
    request.setCharacterEncoding("UTF-8");
    if ("POST".equals(request.getMethod())) {
        String name = request.getParameter("name");
        String value = request.getParameter("value");
        String maxAge = request.getParameter("maxAge");
        String domain = request.getParameter("domain");
        String path = request.getParameter("path");
        String comment = request.getParameter("comment");
        String secure = request.getParameter("secure");

        if (!isNull(name)) {
            Cookie cookie = new Cookie(URLEncoder.encode(name, "UTF-8"), URLEncoder.encode(value, "UTF-8"));
            if (!isNull(maxAge)) {
                cookie.setMaxAge(Integer.parseInt(maxAge));
            }
            if (!isNull(domain)) {
                cookie.setDomain(domain);
            }
            if (!isNull(path)) {
                cookie.setDomain(path);
            }
            if (!isNull(comment)) {
                cookie.setDomain(comment);
            }
            if (!isNull(secure)) {
                cookie.setDomain(secure);
            }
            response.addCookie(cookie);
        }
    }
%>
<html>
<head>
    <title>set cookie</title>
</head>
<body>
<div>
    <p>current cookie : </p>
    <script type="text/javascript">
        document.write(document.cookie);
    </script>
</div>
<div>create new cookie :</div>
<div>
    <form action="setcookie.jsp" method="post">
        <div>
            <span>name: </span> <input type="text" name="name">
        </div>
        <div>
            <span>value: </span> <input type="text" name="value">
        </div>
        <div>
            <span>maxAge: </span> <input type="text" name="maxAge">
        </div>
        <div>
            <span>domain: </span> <input type="text" name="domain">
        </div>
        <div>
            <span>path: </span> <input type="text" name="path">
        </div>
        <div>
            <span>comment: </span> <input type="text" name="comment">
        </div>
        <div>
            <span>secure: </span> <input type="text" name="secure">
        </div>

        <div>
            <input type="submit" value="submit">
            <input type="button" value="refresh" onclick="location='setcookie.jsp'">
        </div>


    </form>
</div>
</body>
</html>
