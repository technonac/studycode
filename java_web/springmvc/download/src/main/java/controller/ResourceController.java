package controller;

import domain.Login;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

@Controller
public class ResourceController {

    private static final Log logger = LogFactory.getLog(ResourceController.class);

    @RequestMapping(value = "/login")
    public String login(@ModelAttribute Login login, HttpSession httpSession, Model model) {
        model.addAttribute("login", new Login());

        if ("test".equals(login.getUserName()) && "test".equals(login.getPassword())) {
            httpSession.setAttribute("loggedIn", Boolean.TRUE);
            return "Main";
        } else {
            return "LoginForm";
        }
    }

    @RequestMapping(value = "/download-resource")
    public String downloadResource(HttpSession session, HttpServletRequest request, HttpServletResponse response,
                                   Model model) {
        if (session == null || session.getAttribute("loggedIn") == null) {
            model.addAttribute("login", new Login());
            return "LoginForm";
        }

        String dataDirectory = request.getServletContext().getRealPath("/WEB-INF/data");

        Path file = Paths.get(dataDirectory, "secret.pdf");
        if (Files.exists(file)) {
            response.setContentType("application/pdf");
            response.addHeader("Content-Disposition", "attachment; filename=secret.pdf");

            try {
                Files.copy(file, response.getOutputStream());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return null;
    }
}
