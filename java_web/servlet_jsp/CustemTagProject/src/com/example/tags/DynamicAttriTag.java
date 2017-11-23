package com.example.tags;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.JspWriter;
import javax.servlet.jsp.tagext.DynamicAttributes;
import javax.servlet.jsp.tagext.TagSupport;
import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class DynamicAttriTag extends TagSupport implements DynamicAttributes {
    private Map<String, String> map = new HashMap<>();

    @Override
    public int doEndTag() throws JspException {
        JspWriter out = pageContext.getOut();
        Iterator<String> iterator = map.keySet().iterator();
        while (iterator.hasNext()) {
            String key = iterator.next();
            String value = map.get(key);
            try {
                out.println(key + " = " + value + "<br/>");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return super.doEndTag();
    }

    @Override
    public void setDynamicAttribute(String uri, String key, Object value) throws JspException {

        map.put(key, String.valueOf(value));
    }
}
