package com.example.tags2;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.tagext.JspFragment;
import javax.servlet.jsp.tagext.SimpleTagSupport;
import java.io.IOException;
import java.io.StringWriter;

public class ToUpperCaseTag extends SimpleTagSupport {
    @Override
    public void doTag() throws JspException, IOException {
        StringWriter writer = new StringWriter();
        //将标签体内容读入该writer,标签体为JspFragment的形式
        JspFragment jspFragment = getJspBody();
        //通过invoke输出到指定的writer中,即getJspContext().getOut()
        jspFragment.invoke(writer);
        String content = writer.getBuffer().toString(); //标签体的内容
        getJspContext().getOut().print(content.toUpperCase());
        super.doTag();
    }
}
