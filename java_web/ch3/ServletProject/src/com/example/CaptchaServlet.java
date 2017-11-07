package com.example;

import com.sun.image.codec.jpeg.JPEGCodec;
import com.sun.image.codec.jpeg.JPEGImageEncoder;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.Random;

public class CaptchaServlet extends HttpServlet {

    //不包括O,0,1,I
    public static final char[] CHARS = {
            '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'J', 'K', 'L', 'M', 'N', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W',
            'X', 'Y', 'Z',
    };

    public static Random random = new Random();

    public static String getRandomString() {
        StringBuffer buffer = new StringBuffer();
        for (int i = 0; i < 6; i++) {
            buffer.append(CHARS[random.nextInt(CHARS.length)]);
        }
        return buffer.toString();
    }

    public static Color getRandomColor() {
        return new Color(random.nextInt(255), random.nextInt(255), random.nextInt(255));
    }

    public static Color getReverseColor(Color c) {
        return new Color(255 - c.getRed(), 255 - c.getGreen(), 255 - c.getBlue());
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException,
            IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException,
            IOException {
        response.setContentType("image/jpeg");
        String randomString = getRandomString();

        request.getSession(true).setAttribute("randomString", randomString); //放到session中

        int width = 100;
        int height = 30;
        Color color = getRandomColor(); //随机颜色，用于背景色
        Color reverseColor = getReverseColor(color); //反色 用于前景色

        BufferedImage bi = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB); //创建一个彩色图片
        Graphics2D g = bi.createGraphics(); //获取绘图对象
        g.setFont(new Font(Font.SANS_SERIF, Font.BOLD, 16)); //设置字体
        g.setColor(color); //设置颜色
        g.fillRect(0, 0, width, height); //绘制背景
        g.setColor(reverseColor); //设置颜色
        g.drawString(randomString, 18, 20);
        for (int i = 0, n = random.nextInt(100); i < n; i++) { //最多100个噪点
            g.drawRect(random.nextInt(width), random.nextInt(height), 1, 1); //随机噪点
        }

        ServletOutputStream out = response.getOutputStream();
        JPEGImageEncoder encoder = JPEGCodec.createJPEGEncoder(out); //转成jpeg格式
        encoder.encode(bi); //对图片进行编码
        out.flush();
    }
}
