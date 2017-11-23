package com.example.tags;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.JspWriter;
import javax.servlet.jsp.PageContext;
import javax.servlet.jsp.tagext.Tag;
import java.io.IOException;
import java.util.ResourceBundle;

public class Copyright implements Tag {
    private Tag parent; //父标签
    private PageContext pageContext; //jsp内容


    @Override
    public void setPageContext(PageContext pageContext) {
        this.pageContext = pageContext;
    }

    @Override
    public void setParent(Tag tag) {
        this.parent = tag;
    }

    @Override
    public Tag getParent() {
        return this.parent;
    }

    /**
     * 标签开始时执行
     *
     * @return
     * @throws JspException
     */
    @Override
    public int doStartTag() throws JspException {
        return SKIP_BODY;
    }

    /**
     * 标签结束时执行
     *
     * @return
     * @throws JspException
     */
    @Override
    public int doEndTag() throws JspException {
        JspWriter out = pageContext.getOut();
        try {
            out.println("<div>");
            out.println(ResourceBundle.getBundle("copyright").getString("copyright"));
            out.println("</div>");
        } catch (IOException e) {
            e.printStackTrace();
        }
        return EVAL_PAGE;
    }

    @Override
    public void release() {

    }
}
