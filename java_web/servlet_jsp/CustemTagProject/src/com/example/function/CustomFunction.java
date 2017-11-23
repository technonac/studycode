package com.example.function;

import java.util.Collection;

/**
 * 自定义方法
 */
public class CustomFunction {
    public static int length(Object obj) {
        if (obj == null) {
            return 0;
        } else if (obj instanceof StringBuffer) {
            return length(((StringBuffer) obj).toString());
        } else if (obj instanceof String) {
            return ((String) obj).getBytes().length;
        } else if (obj instanceof Collection) {
            return ((Collection) obj).size();
        }
        return 0;
    }
}
