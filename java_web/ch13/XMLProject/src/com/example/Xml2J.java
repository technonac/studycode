package com.example;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import java.io.File;

/**
 * xml转换为java对象 unmarshal
 */
public class Xml2J {
    public static void main(String[] args) {
        File xmlFile = new File("test.xml");
        try {
            JAXBContext context = JAXBContext.newInstance(Article.class);
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Article article = (Article) unmarshaller.unmarshal(xmlFile);
            System.out.println(article);

        } catch (JAXBException e) {
            e.printStackTrace();
        }
    }
}
