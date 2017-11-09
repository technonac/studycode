package com.example;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import java.io.File;
import java.io.IOException;

/**
 * 负责解析xml
 * JAXP = The Java API for XML Parsing
 * 将xml映射为java对象
 * JAXB = Java Architecture for XML Binding
 */
public class DomParse {

    public static void main(String[] args) {
        File xmlFile = new File("articles.xml");
        DocumentBuilderFactory builderFactory = DocumentBuilderFactory.newInstance();
        try {
            DocumentBuilder documentBuilder = builderFactory.newDocumentBuilder();
            Document document = documentBuilder.parse(xmlFile);

            Element root = document.getDocumentElement(); //返回该xml文档的根元素
            System.out.println("根元素: " + root.getNodeName());

            NodeList childNodes = root.getChildNodes(); //获取根元素下面的子节点
            int length = childNodes.getLength();
            for (int i = 0; i < length; i++) {
                Node node = childNodes.item(i);
                if ("article".equals(node.getNodeName())) {
                    String category = node.getAttributes().getNamedItem("category").getNodeValue();
                    System.out.println("找到 article节点 -- category = " + category);
                    NodeList nodeDetail = node.getChildNodes(); //获得<article>下的节点
                    for (int j = 0; j < nodeDetail.getLength(); j++) {
                        Node detail = nodeDetail.item(j);
                        if ("title".equals(detail.getNodeName())) {
                            System.out.println("title = " + detail.getTextContent());
                        } else if ("author".equals(detail.getNodeName())) {
                            System.out.println("author = " + detail.getTextContent());
                        } else if ("email".equals(detail.getNodeName())) {
                            System.out.println("email = " + detail.getTextContent());
                        } else if ("date".equals(detail.getNodeName())) {
                            System.out.println("date = " + detail.getTextContent());
                        }

                    }
                }
            }

        } catch (ParserConfigurationException e) {
            e.printStackTrace();
        } catch (SAXException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}
