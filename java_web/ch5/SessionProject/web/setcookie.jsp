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
</body>
</html>
