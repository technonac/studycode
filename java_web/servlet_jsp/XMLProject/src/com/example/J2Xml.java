package com.example;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;
import java.io.File;

/**
 * java对象转化成xml marshal
 */
public class J2Xml {

    public static void main(String[] args) {
        File xmlFile = new File("test.xml");
        try {
            JAXBContext context = JAXBContext.newInstance(Article.class);

            Marshaller marshaller = context.createMarshaller();

            Article article = new Article();
            article.setAuthor("tomcat");
            article.setDate("19700101");
            article.setEmail("tomcat@tomcat.com");
            article.setTitle("tomtom");
            marshaller.marshal(article, xmlFile);

        } catch (JAXBException e) {
            e.printStackTrace();
        }
    }
}
