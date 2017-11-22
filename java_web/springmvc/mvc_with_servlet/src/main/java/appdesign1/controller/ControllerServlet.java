package appdesign1.controller;

import appdesign1.action.SaveProductionAction;
import appdesign1.form.ProductForm;
import appdesign1.model.Product;
import appdesign1.validator.ProductValidator;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.List;

//@WebServlet(name = "ControllerServlet", urlPatterns = {"/input-product", "save-product"})
public class ControllerServlet extends HttpServlet {

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException,
            IOException {
        process(request, response);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException,
            IOException {
        process(request, response);
    }

    private void process(HttpServletRequest request, HttpServletResponse response) throws ServletException,
            IOException {
        String uri = request.getRequestURI();  // uri: /contextName/resourceName
        int lastIndex = uri.lastIndexOf('/');
        String action = uri.substring(lastIndex + 1);
        //execute an action
        String dispatchUrl = null;
        if ("input-product".equals(action)) {
            // no action class,just forward
            dispatchUrl = "/jsp/ProductForm.jsp";
        } else if ("save-product".equals(action)) {
            //create form
            ProductForm productForm = new ProductForm();

            //populate action properties
            productForm.setName(request.getParameter("name"));
            productForm.setDescription(request.getParameter("description"));
            productForm.setPrice(request.getParameter("price"));

            //validate ProductForm
            ProductValidator productValidator = new ProductValidator();
            List<String> errors = productValidator.validate(productForm);

            if (errors.isEmpty()) {
                //create model
                Product product = new Product();
                product.setName(productForm.getName());
                product.setDescription(productForm.getDescription());
                try {
                    product.setPrice(new BigDecimal(productForm.getPrice()));
                } catch (NumberFormatException e) {
                    e.printStackTrace();
                }
                //execute action method
                SaveProductionAction saveProductionAction = new SaveProductionAction();
                saveProductionAction.save(product);
                //store model in a scope variable for the view
                request.setAttribute("product", product);
                dispatchUrl = "/jsp/ProductDetails.jsp";
            } else {
                request.setAttribute("errors", errors);
                dispatchUrl = "/jsp/ProductForm.jsp";
            }
        }

        //forward to a view
        if (dispatchUrl != null) {
            RequestDispatcher rd = request.getRequestDispatcher(dispatchUrl);
            rd.forward(request, response);
        }
    }
}
