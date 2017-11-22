<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title>Add Product Form</title>
</head>
<body>
<form method="post" action="save-product">
    <h1>Add Product
        <span>Please use this form to enter product details</span>
    </h1>
    <div id="errors">
        ${empty requestScope.errors? "" : "<p id='errors'>"
                += "Error(s)!"
                += "<ul>"}
        <!--${requestScope.errors.stream().map(
          x -> "--><li>"+=x+="</li><!--").toList()}-->
        ${empty requestScope.errors? "" : "</ul></p>"}
    </div>
    <div>
        <label>
            <span>Product Name :</span>
            <input id="name" type="text" name="name"
                   placeholder="The complete product name"
                   value="${form.name}"/>
        </label>
    </div>
    <div>
        <label>
            <span>Description :</span>
            <input id="description" type="text" name="description"
                   placeholder="Product description"
                   value="${form.description}"/>
        </label>
    </div>
    <div>
        <label>
            <span>Price :</span>
            <input id="price" name="price" type="number" step="any"
                   placeholder="Product price in #.## format"
                   value="${form.price}"/>
        </label>
    </div>
    <div>
        <label>
            <span>&nbsp;</span>
            <input type="submit"/>
        </label>
    </div>
</form>
</body>
</html>