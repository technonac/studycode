web程序部署在tomcat的/webapps目录下，一个webapps文件夹可以部署多个不同的web应用.webapps/web1,webapps/web2

web程序文件结构
/ web应用根目录
/WEB-INF/ 不能通过浏览器直接访问
/WEB-INF/web.xml web程序最主要的配置文件
/WEB-INF/classes/ class类文件都放在该目录下
/WEB-INF/lib/ jar文件都放在改目录下