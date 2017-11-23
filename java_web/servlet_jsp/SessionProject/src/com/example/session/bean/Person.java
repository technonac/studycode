package com.example.session.bean;

import java.util.Date;

public class Person {
    private String username;
    private String password;
    private int age;
    private Date birthday;

    public Person(String username, String password, int age, Date birthday) {
        this.username = username;
        this.password = password;
        this.age = age;
        this.birthday = birthday;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public int getAge() {
        return age;
    }

    public Date getBirthday() {
        return birthday;
    }

}
