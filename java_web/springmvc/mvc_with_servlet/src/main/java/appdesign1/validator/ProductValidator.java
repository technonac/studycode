package appdesign1.validator;

import appdesign1.form.ProductForm;

import java.util.ArrayList;
import java.util.List;

public class ProductValidator {

    public List<String> validate(ProductForm productForm) {
        List<String> errors = new ArrayList<String>();

        String name = productForm.getName();
        if (name == null || name.trim().length() == 0) {
            errors.add("Product must have a name");
        }

        String price = productForm.getPrice();
        if (price == null || price.trim().length() == 0) {
            errors.add("Product must have a price");
        } else {
            try {
                Float.parseFloat(price);
            } catch (NumberFormatException e) {
                errors.add("Invalid price value");
            }
        }
        return errors;
    }
}
