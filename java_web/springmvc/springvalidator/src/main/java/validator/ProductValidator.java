package validator;

import domain.Product;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;

import java.math.BigDecimal;
import java.time.LocalDate;

public class ProductValidator implements Validator {
    @Override
    public boolean supports(Class<?> aClass) {
        return Process.class.isAssignableFrom(aClass);
    }

    @Override
    public void validate(Object o, Errors errors) {
        Product product = (Product) o;

        ValidationUtils.rejectIfEmpty(errors, "name", "productName.required");
        ValidationUtils.rejectIfEmpty(errors, "price", "price.required");
        ValidationUtils.rejectIfEmpty(errors, "productionDate", "productionDate.required");

        BigDecimal price = product.getPrice();
        if (price != null && price.compareTo(BigDecimal.ZERO) < 0) {
            errors.rejectValue("price", "price.negative");
        }

        LocalDate productionDate = product.getProductionDate();
        if (productionDate != null) {
            if(productionDate.isAfter(LocalDate.now())){
                errors.rejectValue("productionDate","productionDate.invalid");
            }
        }
    }
}
