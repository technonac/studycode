web程序部署在tomcat的/webapps目录下，一个webapps文件夹可以部署多个不同的web应用.webapps/web1,webapps/web2

web程序文件结构
/ web应用根目录
/WEB-INF/ 不能通过浏览器直接访问
/WEB-INF/web.xml web程序最主要的配置文件
/WEB-INF/classes/ class类文件都放在该目录下
/WEB-INF/lib/ jar文件都放在改目录下

servlet的生命周期
1.服务器加载servlet
2.servlet构造函数
3.@PostConstruct修饰的方法
4.init(ServletConfig)方法
5.service()方法
6.destroy()方法
7.@PreDestroy()方法 指的servlet销毁
8.服务器卸载servlet
