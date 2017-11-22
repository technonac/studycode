package di.service;

import di.util.PDFUtil;

public class PDFService {
    public void createPDF(String path, String input) {
        PDFUtil.createDocument(path, input);
    }
}
