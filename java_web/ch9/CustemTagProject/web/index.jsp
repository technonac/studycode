<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="mytaglib" uri="http://mycompany.com/tags" %>
<%@ taglib prefix="cfn" uri="http://mycompany.com/function" %>
<html>
<head>
    <title>custom tag</title>
</head>
<body>
<mytaglib:copyright>
    sjksjksjkjsk
</mytaglib:copyright>

<mytaglib:hello name="tom"/><br/>
<mytaglib:hello name="${pageContext.request.remoteAddr}"/><br/>
<mytaglib:hello name="${cookie}"/><br/>
<mytaglib:toLowerCase>TO LOWER CASE IN TAG BODY</mytaglib:toLowerCase><br/>
</body>
<div>
    dynamicAttribute: <br/>
    <mytaglib:dynamicAttribute att1="value1" att2="value2"/>
</div>

<div>
    mutltag : <mytaglib:multi num1="9" num2="9"></mytaglib:multi>
</div>
<div>
    <mytaglib:toUpperCase>
        to upper case in tag body
    </mytaglib:toUpperCase>
</div>

<div>
    <mytaglib:multiAttribute>
        <jsp:attribute name="body1"> im body1 </jsp:attribute>
        <jsp:attribute name="body2"> im body2 </jsp:attribute>
    </mytaglib:multiAttribute>
</div>

<div>
    ${cfn:length("abcd")}
</div>
</html>
