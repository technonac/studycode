package com.example;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

import java.text.DateFormat;
import java.text.SimpleDateFormat;

public class MySaxHandler extends DefaultHandler {

    private static DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    private String content;


    @Override
    public void characters(char[] ch, int start, int length) throws SAXException {
        super.characters(ch, start, length);
        content = new String(ch, start, length);
    }

    @Override
    public void endElement(String uri, String localName, String qName) throws SAXException {
        super.endElement(uri, localName, qName);
        if ("title".equals(qName)) {
            System.out.println("title = " + content);
        } else if ("author".equals(qName)) {
            System.out.println("author = " + content);
        } else if ("email".equals(qName)) {
            System.out.println("email = " + content);
        } else if ("date".equals(qName)) {
            System.out.println("date = " + content);
        }

    }

    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        super.startElement(uri, localName, qName, attributes);
        if ("article".equals(qName)) {
            System.out.println("找到article节点 -- category =  " + attributes.getValue("category"));
        }
    }
}
