package com.example.tags;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.tagext.BodyTagSupport;
import java.io.IOException;

public class ToLowerCaseTag extends BodyTagSupport {
    @Override
    public int doEndTag() throws JspException {
        String content = getBodyContent() == null ? "" : getBodyContent().getString();
        try {
            pageContext.getOut().println(content == null ? "" : content.toLowerCase());
        } catch (IOException e) {
            e.printStackTrace();
        }
        return EVAL_PAGE;
    }
}
