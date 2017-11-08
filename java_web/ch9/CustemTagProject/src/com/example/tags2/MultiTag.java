package com.example.tags2;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.tagext.SimpleTag;
import javax.servlet.jsp.tagext.SimpleTagSupport;
import java.io.IOException;

/**
 * JSP 2.X
 */
public class MultiTag extends SimpleTagSupport {
    private int num1;
    private int num2;

    @Override
    public void doTag() throws JspException, IOException {
        getJspContext().getOut().write(num1 + " * " + num2 + " = " + (num1 * num2));
        super.doTag();
    }

    public int getNum1() {
        return num1;
    }

    public void setNum1(int num1) {
        this.num1 = num1;
    }

    public int getNum2() {
        return num2;
    }

    public void setNum2(int num2) {
        this.num2 = num2;
    }
}
