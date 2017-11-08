<%--
fn方法库
fn:methodName

fmt标签库
<prfix:tagName/>

--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<html>
<head>
    <title>fn</title>
</head>
<body>
<div>
    <c:if test="${fn:containsIgnoreCase(header['User-Agent'], 'windows')}">
        you are using window os
    </c:if>
    <br/>
    <c:if test="${fn:endsWith('abc.jpg','jpg')}">
        endwith test
    </c:if>
</div>

<div>
    ${fn:split('abc,def',',' )}<br/>
    ${fn:length('abcd')}<br/>
</div>
</body>
</html>
