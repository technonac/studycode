<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<html>
<head>
    <title>Add Product Form</title>
    <style type="text/css">@import url("<c:url value="/css/main.css"/>");</style>
</head>
<body>
<div id="global">
    <form:form commandName="product" action="save-product" method="post" enctype="multipart/form-data">
        <fieldset>
            <legend>Add a product</legend>
            <p>
                <label for="name">Product Name:</label>
                <form:input id="name" path="name" cssErrorClass="error"/>
                <form:errors path="name" cssClass="error"/>
            </p>
            <p>
                <label for="description">Description:</label>
                <form:input id="description" path="description"/>
            </p>
            <p>
                <label for="price">Price:</label>
                <form:input id="price" path="price" cssErrorClass="error"/>
            </p>
            <p>
                <label for="image">Product Image</label>
                <input type="file" id="image" name="images" multiple>
            </p>
            <p id="buttons">
                <input type="reset" id="reset" tabindex="4">
                <input type="submit" id="submit" tabindex="5" value="Add Product">
            </p>
        </fieldset>
    </form:form>
</div>
</body>
</html>
