package com.example.tags2;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.tagext.JspFragment;
import javax.servlet.jsp.tagext.SimpleTagSupport;
import java.io.IOException;
import java.io.StringWriter;

public class MultiAttributeTag extends SimpleTagSupport {
    private JspFragment body1; //标签体1
    private JspFragment body2; //标签体2

    @Override
    public void doTag() throws JspException, IOException {
        StringWriter writer1 = new StringWriter();
        StringWriter writer2 = new StringWriter();

        for (int i = 0; i < 5; i++) {
            body1.invoke(writer1); //将body1输出到writer1
        }

        for (int i = 0; i < 3; i++) {
            body2.invoke(writer2); //将body1输出到writer1
        }
        getJspContext().getOut().print("<div>body1 " + writer1.getBuffer().toString() + "</div>");
        getJspContext().getOut().print("<div>body2 " + writer2.getBuffer().toString() + "</div>");
        super.doTag();
    }

    public void setBody1(JspFragment body1) {
        this.body1 = body1;
    }

    public void setBody2(JspFragment body2) {
        this.body2 = body2;
    }
}
