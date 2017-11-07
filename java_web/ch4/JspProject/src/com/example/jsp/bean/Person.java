package com.example.jsp.bean;

/**
 * java bean 行为是一组与javabean相关的行为，包括usebean,setproperty,getproperty
 * Java bean 就是普通的java类，也被称为 POJO(普通java对象)
 * Plain Ordinary Java Object
 */
public class Person {
    private String name;
    private int age;
    private String sex;
    private boolean secret;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public boolean isSecret() {
        return secret;
    }

    public void setSecret(boolean secret) {
        this.secret = secret;
    }
}
