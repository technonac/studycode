<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Add Product Form</title>
</head>
<body>
<form method="post" action="pdf">
    <h1>Create PDF
        <span>Please use this form to enter the text</span>
    </h1>
    <label>
        <span>Text :</span>
        <input type="text" name="text"
               placeholder="Text for PDF"/>
    </label>
    <label>
        <span>&nbsp;</span>
        <input type="submit"/>
    </label>
</form>
</body>
</html>